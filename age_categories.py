AGE_GROUPS = {
    "kids": {"label": "Kids", "min": 5, "max": 10, "intensity": "Low", "intensity_level": 1},
    "teens": {"label": "Teens", "min": 11, "max": 20, "intensity": "Low-Medium", "intensity_level": 2},
    "adults": {"label": "Adults", "min": 21, "max": 55, "intensity": "Medium", "intensity_level": 3},
    "seniors": {"label": "Seniors", "min": 56, "max": 120, "intensity": "Low", "intensity_level": 1}
}

AGE_RANGE_OPTIONS = [
    {"value": "5-10", "label": "5-10 years", "age": 8},
    {"value": "11-20", "label": "11-20 years", "age": 16},
    {"value": "21-35", "label": "21-35 years", "age": 25},
    {"value": "36-55", "label": "36-55 years", "age": 45},
    {"value": "56+", "label": "56+ years", "age": 60}
]


def normalize_age(age):
    if age is None:
        return None
    if isinstance(age, str):
        age = age.strip()
        if not age:
            return None
        for option in AGE_RANGE_OPTIONS:
            if age.lower() == option["value"].lower() or age.lower() == option["label"].lower():
                return option["age"]
        try:
            return int(age)
        except ValueError:
            return None
    return int(age)


def get_age_group(age):
    age = normalize_age(age)
    if age is None:
        return "adults"
    for key, group in AGE_GROUPS.items():
        if group["min"] <= age <= group["max"]:
            return key
    return "adults"


def get_age_label(age):
    return AGE_GROUPS[get_age_group(age)]["label"]


def get_intensity(age):
    return AGE_GROUPS[get_age_group(age)]["intensity"]


def get_intensity_level(age):
    return AGE_GROUPS[get_age_group(age)]["intensity_level"]


def get_duration_recommendation(age):
    group = get_age_group(age)
    durations = {
        "kids": "15 mins",
        "teens": "20-25 mins",
        "adults": "25-35 mins",
        "seniors": "20-25 mins"
    }
    return durations.get(group, "25 mins")
