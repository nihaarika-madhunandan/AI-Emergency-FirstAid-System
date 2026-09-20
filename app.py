from flask import Flask, render_template, request, redirect, session, jsonify
import os
import json
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

from age_categories import get_age_label, get_duration_recommendation, normalize_age
from activities import get_exercises_by_age, get_yoga_by_age, get_meditation_by_age, get_safety_warning as get_activity_safety
from ai_service import get_enhanced_first_aid, analyze_injury_image
from menstrual_health import list_menstrual_problems, get_menstrual_guidance

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

USERS_FILE = 'users.json'

INJURY_TYPES = [
    "Cut/Laceration", "Burn (Minor/Moderate)", "Severe Burn",
    "Fracture (Bone Break)", "Sprain", "Strain", "Bruise/Contusion",
    "Wound (Deep)", "Puncture Wound", "Snake Bite", "Insect Bite",
    "Animal Bite", "Chemical Burn", "Electrical Burn",
    "Heat Exhaustion", "Heat Stroke", "Frostbite", "Hypothermia",
    "Poisoning", "Choking", "Allergic Reaction", "Shock",
    "Unconsciousness", "Severe Bleeding", "Eye Injury"
]

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

users = load_users()


def is_logged_in():
    return 'user' in session


def session_user_name():
    if not is_logged_in():
        return None
    return users.get(session['user'], {}).get('name', 'User')


def record_module_visit(module):
    if not is_logged_in():
        return
    username = session['user']
    if username not in users:
        return
    if 'preferences' not in users[username]:
        users[username]['preferences'] = {'last_injury_type': '', 'injury_history': []}
    users[username]['preferences'].setdefault('module_visits', {})
    module = module.lower()
    visits = users[username]['preferences']['module_visits']
    visits[module] = visits.get(module, 0) + 1
    save_users(users)


def build_module_stats(user_data):
    visits = (user_data.get('preferences') or {}).get('module_visits', {})
    modules = ['exercise', 'meditation', 'relaxation', 'menstrual', 'first_aid']
    stats = {m: visits.get(m, 0) for m in modules}
    total = sum(stats.values())
    if total:
        for m in modules:
            stats[m] = int(round(stats[m] / total * 100))
    stats['total'] = total
    return stats


def detect_injury(injury_text, injury_dropdown):
    text = injury_text.lower()

    if "severe bleeding" in text or "hemorrhage" in text or "gushing" in text:
        return "Severe Bleeding"
    elif "cut" in text or "laceration" in text or "bleeding" in text:
        return "Cut/Laceration"
    elif "snake" in text:
        return "Snake Bite"
    elif "fracture" in text or "bone" in text or "broken" in text or "broke" in text or "break" in text:
        return "Fracture (Bone Break)"
    elif "sprain" in text or "twisted" in text:
        return "Sprain"
    elif "strain" in text or "pulled" in text:
        return "Strain"
    elif "bruise" in text or "contusion" in text:
        return "Bruise/Contusion"
    elif "puncture" in text or "stab" in text:
        return "Puncture Wound"
    elif "animal" in text or "dog bite" in text or "cat bite" in text:
        return "Animal Bite"
    elif "insect" in text or "bug bite" in text or "sting" in text:
        return "Insect Bite"
    elif "chemical" in text or "acid" in text:
        return "Chemical Burn"
    elif "electrical" in text or "electric" in text:
        return "Electrical Burn"
    elif "heat" in text and "exhaustion" in text:
        return "Heat Exhaustion"
    elif "heat" in text and "stroke" in text:
        return "Heat Stroke"
    elif "frost" in text or "freezing" in text:
        return "Frostbite"
    elif "hypothermia" in text or "exposure" in text:
        return "Hypothermia"
    elif "poison" in text:
        return "Poisoning"
    elif "choking" in text or "cannot breathe" in text:
        return "Choking"
    elif "allergic" in text or "allergy" in text or "hives" in text:
        return "Allergic Reaction"
    elif "shock" in text:
        return "Shock"
    elif "unconscious" in text or "fainted" in text or "passed out" in text:
        return "Unconsciousness"
    elif "deep" in text and "wound" in text:
        return "Wound (Deep)"
    elif "eye" in text:
        return "Eye Injury"
    elif "burn" in text or "scald" in text:
        if "severe" in text or "third" in text or "3rd" in text:
            return "Severe Burn"
        return "Burn (Minor/Moderate)"

    if injury_dropdown:
        return injury_dropdown

    return "General Injury"

@app.route('/')
def home():
    if 'user' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    user_data = users.get(session['user'], {})
    record_module_visit('dashboard')
    return render_template('dashboard.html', user_name=user_data.get('name', 'User'),
                           module_stats=build_module_stats(user_data))

@app.route('/first-aid')
def first_aid():
    record_module_visit('first_aid')
    return render_template(
        'first_aid.html',
        injury_types=INJURY_TYPES,
        logged_in=is_logged_in(),
        user_name=session_user_name()
    )


@app.route('/menstrual-health', methods=['GET', 'POST'])
def menstrual_health():
    if 'user' not in session:
        return redirect('/login')
    record_module_visit('menstrual')
    selected = None
    guidance = None
    if request.method == 'POST':
        selected = (request.form.get('problem') or '').strip()
        guidance = get_menstrual_guidance(selected)
    return render_template(
        'menstrual_health.html',
        problems=list_menstrual_problems(),
        selected=selected,
        guidance=guidance,
        logged_in=is_logged_in(),
        user_name=session_user_name()
    )

@app.route('/exercises')
def exercises():
    if 'user' not in session:
        return redirect('/login')
    record_module_visit('exercise')
    user_data = users.get(session['user'], {})
    age = user_data.get('age')
    if not age:
        return render_template('exercises.html', exercises=None, age_required=True,
                               user_name=user_data.get('name', 'User'))
    exercise_data = get_exercises_by_age(age)
    return render_template('exercises.html', exercises=exercise_data['exercises'],
                           age_group=get_age_label(age), intensity=exercise_data['intensity'],
                           duration=exercise_data['duration'],
                           safety_warning=get_activity_safety(age),
                           user_name=user_data.get('name', 'User'), age_required=False)

@app.route('/meditation')
def meditation():
    if 'user' not in session:
        return redirect('/login')
    record_module_visit('meditation')
    user_data = users.get(session['user'], {})
    age = user_data.get('age')
    if not age:
        return render_template('meditation.html', meditations=None, age_required=True,
                               user_name=user_data.get('name', 'User'))
    meditation_data = get_meditation_by_age(age)
    return render_template('meditation.html', meditations=meditation_data['meditations'],
                           age_group=get_age_label(age), intensity=meditation_data['intensity'],
                           safety_warning=get_activity_safety(age),
                           user_name=user_data.get('name', 'User'), age_required=False)

@app.route('/relaxation')
def relaxation():
    if 'user' not in session:
        return redirect('/login')
    record_module_visit('relaxation')
    user_data = users.get(session['user'], {})
    age = user_data.get('age')
    
    yoga_data = None
    age_label = None
    intensity = None
    duration = None
    safety_warning = None
    
    if age:
        yoga_data = get_yoga_by_age(age)
        age_label = get_age_label(age)
        intensity = yoga_data['intensity']
        duration = get_duration_recommendation(age)
        safety_warning = get_activity_safety(age)
        
    return render_template('relaxation.html', activities=yoga_data,
                           age_group=age_label, intensity=intensity,
                           duration=duration,
                           safety_warning=safety_warning,
                           user_name=user_data.get('name', 'User'), age_required=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        phone = request.form['phone'].strip()
        age = request.form['age'].strip()
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if len(password) < 6:
            return render_template('register.html', error="Password must be at least 6 characters")

        if username in users:
            return render_template('register.html', error="Username already exists")

        users[username] = {
            'name': name,
            'email': email,
            'phone': phone,
            'age': age,
            'password': generate_password_hash(password),
            'preferences': {
                'last_injury_type': '',
                'injury_history': []
            }
        }
        save_users(users)
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        stored = users.get(username, {}).get('password')
        if stored:
            if stored.startswith(('pbkdf2:', 'scrypt:')):
                valid = check_password_hash(stored, password)
            else:
                valid = stored == password
                if valid:
                    users[username]['password'] = generate_password_hash(password)
                    save_users(users)
        else:
            valid = False

        if valid:
            session['user'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/api/save-age', methods=['POST'])
def save_age():
    if 'user' not in session:
        return jsonify({"error": "Not logged in"}), 401
    data = request.get_json() or {}
    age = normalize_age(data.get('age'))
    age_range = data.get('age_range')
    if age is None:
        age = normalize_age(age_range)
    if age is None:
        return jsonify({"error": "Age required"}), 400
    username = session['user']
    if username in users:
        users[username]['age'] = str(age)
        users[username]['age_range'] = age_range or get_age_label(age)
        if 'preferences' not in users[username]:
            users[username]['preferences'] = {'last_injury_type': '', 'injury_history': []}
        save_users(users)
        return jsonify({"success": True, "age_group": get_age_label(age)})
    return jsonify({"error": "User not found"}), 404

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('image')
    injury_text = request.form.get('injury_text', '')
    injury_dropdown = request.form.get('injury_dropdown', '')
    kit = request.form.get('kit', 'yes')
    kit_type = request.form.get('kit_type', 'basic')

    ai_analysis = None
    if file and file.filename:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        ai_analysis = analyze_injury_image(filepath)

    if injury_dropdown and not injury_text:
        injury = injury_dropdown
    elif injury_text and not injury_dropdown:
        injury = detect_injury(injury_text, injury_dropdown)
    elif injury_text and injury_dropdown:
        injury = injury_dropdown
    elif ai_analysis:
        injury = ai_analysis['injury_type']
    else:
        injury = "General Injury"

    refine_text = "" if injury_dropdown else injury_text

    ai_severity = None
    ai_confidence = None
    if ai_analysis and not injury_text and not injury_dropdown:
        ai_severity = ai_analysis.get('severity')
        ai_confidence = ai_analysis.get('confidence')

    result = get_enhanced_first_aid(injury, refine_text, kit, kit_type, ai_severity, ai_confidence)

    if is_logged_in():
        username = session['user']
        if username in users:
            if 'preferences' not in users[username]:
                users[username]['preferences'] = {'last_injury_type': '', 'injury_history': []}
            users[username]['preferences']['last_injury_type'] = result['injury_type']
            history = users[username]['preferences'].get('injury_history', [])
            if result['injury_type'] not in history:
                history.append(result['injury_type'])
                if len(history) > 10:
                    history = history[-10:]
            users[username]['preferences']['injury_history'] = history
            save_users(users)

    return render_template('result.html', result=result['steps'], injury=result['injury_type'],
                           severity=result['severity'], confidence=result['confidence'],
                           severity_color=result['severity_color'],
                           severity_icon=result['severity_icon'],
                           immediate_actions=result['immediate_actions'],
                           ai_analysis=ai_analysis,
                           logged_in=is_logged_in(),
                           user_name=session_user_name())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)