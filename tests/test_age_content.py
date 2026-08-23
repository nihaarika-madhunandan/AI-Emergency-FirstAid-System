import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from age_categories import get_age_group, get_age_label
from activities import get_exercises_by_age, get_yoga_by_age, get_meditation_by_age


def test_age_groups_include_expected_ranges():
    assert get_age_group(8) == 'kids'
    assert get_age_group(16) == 'teens'
    assert get_age_group(25) == 'adults'
    assert get_age_group(60) == 'seniors'
    assert get_age_label(8) == 'Kids'


def test_content_is_age_specific():
    exercises = get_exercises_by_age(8)
    yoga = get_yoga_by_age(8)
    meditation = get_meditation_by_age(8)

    assert 'Morning Fun Workout' in exercises['exercises']['morning']['title']
    assert yoga['yoga']['title'] == 'Fun Yoga for Kids'
    assert meditation['meditations']['breathwork']['title'] == 'Fun Breathing Games'
