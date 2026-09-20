import os
import sys
import json
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app, users
from menstrual_health import get_menstrual_guidance


def setup_function():
    users.clear()
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret'


def test_guest_can_open_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Emergency First Aid' in response.data
    assert b'Menstrual Health' not in response.data


def test_guest_can_access_first_aid_without_login():
    client = app.test_client()
    response = client.get('/first-aid', follow_redirects=False)
    assert response.status_code == 200
    assert b'Emergency Assessment' in response.data
    assert response.headers.get('Location') in (None, '')


def test_guest_can_complete_first_aid_workflow():
    client = app.test_client()
    response = client.post('/analyze', data={
        'injury_dropdown': 'Sprain',
        'injury_text': '',
        'kit': 'yes',
        'kit_type': 'basic',
    }, follow_redirects=False)
    assert response.status_code == 200
    assert b'Sprain' in response.data
    assert b'Treatment Steps' in response.data
    assert b'Back to Dashboard' not in response.data


def test_guest_cannot_access_dashboard_wellness_or_menstrual():
    client = app.test_client()
    assert client.get('/dashboard', follow_redirects=False).status_code == 302
    assert '/login' in client.get('/dashboard', follow_redirects=False).headers['Location']
    assert '/login' in client.get('/exercises', follow_redirects=False).headers['Location']
    assert '/login' in client.get('/meditation', follow_redirects=False).headers['Location']
    assert '/login' in client.get('/relaxation', follow_redirects=False).headers['Location']
    assert '/login' in client.get('/menstrual-health', follow_redirects=False).headers['Location']
    assert client.post('/api/save-age', json={'age': 25}).status_code == 401


def test_authenticated_user_reaches_dashboard_and_menstrual(tmp_path, monkeypatch):
    users_file = tmp_path / 'users.json'
    monkeypatch.setattr('app.USERS_FILE', str(users_file))
    client = app.test_client()
    client.post('/register', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '123',
        'age': '25',
        'username': 'guestflowuser',
        'password': 'secret12',
    }, follow_redirects=False)
    login = client.post('/login', data={
        'username': 'guestflowuser',
        'password': 'secret12',
    }, follow_redirects=False)
    assert login.status_code == 302
    assert '/dashboard' in login.headers['Location']
    dash = client.get('/dashboard')
    assert dash.status_code == 200
    assert b'Daily Exercises' in dash.data
    assert b'Menstrual Health' in dash.data
    
    mh_page = client.get('/menstrual-health')
    assert mh_page.status_code == 200
    assert b'Menstrual Health Guidance' in mh_page.data

    result = client.post('/menstrual-health', data={'problem': 'heavy_bleeding'})
    assert result.status_code == 200
    body = result.data.decode('utf-8')
    assert 'Heavy menstrual bleeding' in body
    assert 'not a diagnosis' in body.lower() or 'cannot diagnose' in body.lower()


def test_menstrual_guidance_is_not_a_diagnosis():
    guidance = get_menstrual_guidance('irregular')
    assert guidance is not None
    assert guidance['serious'] is True
    joined = ' '.join(guidance['seek_care']).lower()
    assert 'cannot tell you why' in joined or 'not a diagnosis' in joined
    assert 'diagnosis' in joined or 'cannot' in joined
