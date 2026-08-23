SEVERITY_KEYWORDS = {
    "severe": [
        "unconscious", "not breathing", "severe bleeding", "gushing", "artery",
        "deep wound", "organ", "bone sticking", "compound fracture", "third degree",
        "3rd degree", "electrical", "chemical", "poison", "venom", "allergic",
        "swelling face", "difficulty breathing", "chest pain", "heart attack",
        "stroke", "paralysis", "spinal", "head injury", "concussion"
    ],
    "moderate": [
        "deep cut", "deep", "second degree", "2nd degree", "blister", "blistering",
        "fracture", "broken bone", "sprain", "swelling", "bleeding", "wound",
        "painful", "sting", "bite", "burn", "redness", "infection", "fever"
    ],
    "mild": [
        "scrape", "scratch", "cut", "paper cut", "bruise", "minor", "small",
        "light", "superficial", "surface", "graze", "rash", "itch"
    ]
}

def analyze_severity(injury_type, description=""):
    description = description.lower()
    text = f"{injury_type.lower()} {description}"

    severe_score = sum(1 for kw in SEVERITY_KEYWORDS["severe"] if kw in text)
    moderate_score = sum(1 for kw in SEVERITY_KEYWORDS["moderate"] if kw in text)
    mild_score = sum(1 for kw in SEVERITY_KEYWORDS["mild"] if kw in text)

    severe_types = ["Severe Burn", "Severe Bleeding", "Shock", "Unconsciousness",
                    "Poisoning", "Choking", "Allergic Reaction", "Heat Stroke",
                    "Electrical Burn", "Chemical Burn", "Head Injury"]
    moderate_types = ["Fracture", "Burn (Minor/Moderate)", "Wound (Deep)",
                      "Puncture Wound", "Snake Bite", "Animal Bite", "Hypothermia",
                      "Frostbite", "Heat Exhaustion", "Sprain", "Eye Injury"]
    mild_types = ["Cut/Laceration", "Strain", "Bruise/Contusion", "Insect Bite"]

    if injury_type in severe_types:
        severe_score += 2
    elif injury_type in moderate_types:
        moderate_score += 2
    elif injury_type in mild_types:
        mild_score += 1

    if severe_score > 0 and severe_score >= moderate_score:
        return {"severity": "Severe", "confidence": min(0.95, 0.6 + severe_score * 0.1)}
    elif moderate_score > 0:
        return {"severity": "Moderate", "confidence": min(0.90, 0.5 + moderate_score * 0.1)}
    elif mild_score > 0:
        return {"severity": "Mild", "confidence": min(0.85, 0.4 + mild_score * 0.1)}

    if injury_type in severe_types:
        return {"severity": "Severe", "confidence": 0.7}
    if injury_type in moderate_types:
        return {"severity": "Moderate", "confidence": 0.65}

    return {"severity": "Mild", "confidence": 0.5}

def get_severity_color(severity):
    colors = {"Mild": "#4CAF50", "Moderate": "#FF9800", "Severe": "#F44336"}
    return colors.get(severity, "#4CAF50")

def get_severity_icon(severity):
    icons = {"Mild": "🟢", "Moderate": "🟡", "Severe": "🔴"}
    return icons.get(severity, "🟢")

def get_immediate_actions(severity, injury_type):
    actions = ["Stay calm and assess the situation"]
    if severity == "Severe":
        actions.append("Call emergency services immediately")
        actions.append("Do not move the injured person unless necessary")
        actions.append("Monitor breathing and consciousness")
        actions.append("Control severe bleeding with direct pressure")
    elif severity == "Moderate":
        actions.append("Seek medical attention as soon as possible")
        actions.append("Keep the injured area immobilized")
        actions.append("Apply basic first aid while waiting")
    else:
        actions.append("Clean and dress the wound properly")
        actions.append("Monitor for signs of infection")
        actions.append("Rest and allow natural healing")
    actions.append("Avoid home remedies for serious injuries")
    return actions
