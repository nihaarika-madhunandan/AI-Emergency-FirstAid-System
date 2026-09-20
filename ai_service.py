import os
from severity_analyzer import analyze_severity, get_immediate_actions, get_severity_color, get_severity_icon

INJURY_TYPE_MAPPING = {
    "cut": "Cut/Laceration", "laceration": "Cut/Laceration", "bleeding": "Cut/Laceration",
    "burn": "Burn (Minor/Moderate)", "scald": "Burn (Minor/Moderate)",
    "severe burn": "Severe Burn", "third degree": "Severe Burn", "3rd degree": "Severe Burn",
    "fracture": "Fracture (Bone Break)", "broken": "Fracture (Bone Break)", "broke": "Fracture (Bone Break)", "break": "Fracture (Bone Break)", "bone": "Fracture (Bone Break)",
    "sprain": "Sprain", "twisted": "Sprain",
    "strain": "Strain", "muscle pull": "Strain",
    "bruise": "Bruise/Contusion", "contusion": "Bruise/Contusion",
    "deep wound": "Wound (Deep)", "deep cut": "Wound (Deep)",
    "puncture": "Puncture Wound", "stab": "Puncture Wound",
    "snake": "Snake Bite", "snakebite": "Snake Bite",
    "insect": "Insect Bite", "bug bite": "Insect Bite", "mosquito": "Insect Bite",
    "animal": "Animal Bite", "dog bite": "Animal Bite", "cat bite": "Animal Bite",
    "chemical": "Chemical Burn", "acid": "Chemical Burn",
    "electrical": "Electrical Burn", "electric": "Electrical Burn",
    "heat exhaustion": "Heat Exhaustion", "dehydrated": "Heat Exhaustion",
    "heat stroke": "Heat Stroke", "sunstroke": "Heat Stroke",
    "frostbite": "Frostbite", "freezing": "Frostbite",
    "hypothermia": "Hypothermia", "exposure": "Hypothermia",
    "poison": "Poisoning", "poisonous": "Poisoning", "toxic": "Poisoning",
    "choking": "Choking", "cannot breathe": "Choking",
    "allergic": "Allergic Reaction", "allergy": "Allergic Reaction", "hives": "Allergic Reaction",
    "shock": "Shock", "pale": "Shock", "dizzy": "Shock",
    "unconscious": "Unconsciousness", "fainted": "Unconsciousness", "passed out": "Unconsciousness",
    "severe bleeding": "Severe Bleeding", "hemorrhage": "Severe Bleeding",
    "eye": "Eye Injury", "eye injury": "Eye Injury"
}

AI_FIRST_AID_STEPS = {
    "Cut/Laceration": {
        "mild": ["Wash hands thoroughly", "Clean wound with water and mild soap", "Apply antiseptic cream", "Cover with sterile bandage", "Change dressing daily"],
        "moderate": ["Apply direct pressure to stop bleeding", "Clean wound thoroughly with antiseptic", "Apply sterile gauze dressing", "Secure with medical tape", "Monitor for signs of infection"],
        "severe": ["Call emergency services immediately", "Apply firm pressure with sterile cloth", "Elevate injured area above heart", "Do not remove embedded objects", "Keep pressure until help arrives"]
    },
    "Burn (Minor/Moderate)": {
        "mild": ["Cool burn under cool running water for 10 mins", "Do not apply ice directly", "Apply aloe vera or burn cream", "Cover loosely with sterile gauze", "Take over-the-counter pain relief if needed"],
        "moderate": ["Cool under running water for 15-20 mins", "Remove jewelry or tight items near burn", "Apply medical burn ointment", "Cover with non-stick dressing", "Seek medical evaluation"],
        "severe": ["Call emergency services immediately", "Do not remove clothing stuck to burn", "Cover with cool, moist sterile cloth", "Monitor for signs of shock", "Keep person warm and calm"]
    },
    "Severe Burn": {
        "mild": ["Cool under running water for 20 mins", "Cover with sterile burn dressing", "Take pain medication", "Seek immediate medical attention"],
        "moderate": ["Call emergency services", "Cool burn with water if possible", "Cover loosely with sterile cloth", "Do not apply any creams or ointments", "Monitor breathing and consciousness"],
        "severe": ["Call 911 or emergency services immediately", "Ensure airway is clear", "Cover with clean, dry sheet", "Do not immerse in water", "Monitor for shock and breathing difficulties"]
    },
    "Fracture (Bone Break)": {
        "mild": ["Immobilize the injured area", "Apply ice wrapped in cloth", "Keep elevated", "Use splint if trained", "Visit doctor for X-ray"],
        "moderate": ["Do not move the injured limb", "Apply splint above and below fracture", "Apply ice pack (not directly on skin)", "Keep person still and calm", "Transport to emergency room"],
        "severe": ["Call emergency services", "Do not move the person", "Control any bleeding with pressure", "Keep person warm and still", "Monitor consciousness and breathing"]
    },
    "Sprain": {
        "mild": ["Rest the injured joint", "Apply ice for 15-20 mins every 2-3 hours", "Compress with elastic bandage", "Elevate the injured area", "Take over-the-counter pain relief"],
        "moderate": ["Follow R.I.C.E. protocol (Rest, Ice, Compression, Elevation)", "Use crutches if needed for leg sprain", "Apply compression bandage firmly but not too tight", "Avoid weight bearing", "See doctor if pain persists"],
        "severe": ["Keep joint completely immobilized", "Apply ice and elevation", "Do not attempt to bear weight", "Seek immediate medical evaluation", "X-ray may be needed to rule out fracture"]
    },
    "Strain": {
        "mild": ["Rest the affected muscle", "Apply ice for 15-20 mins", "Gentle stretching when pain subsides", "Take anti-inflammatory medication", "Gradually return to activity"],
        "moderate": ["Rest completely for 24-48 hours", "Ice therapy every 2-3 hours", "Compression with bandage", "Elevate if possible", "Physical therapy may be needed"],
        "severe": ["Seek medical attention", "Do not use the affected muscle", "Apply ice and elevation", "Crutches if leg is affected", "Follow doctor's treatment plan"]
    },
    "Bruise/Contusion": {
        "mild": ["Apply ice pack immediately", "Elevate the bruised area", "Rest the affected area", "Apply arnica cream if available", "Bruise will fade naturally in 1-2 weeks"],
        "moderate": ["Ice therapy for first 48 hours", "Apply warm compress after 48 hours", "Gentle massage around (not on) bruise", "Monitor for unusual swelling", "See doctor if bruise is large and painful"],
        "severe": ["Seek medical evaluation", "Apply ice and elevation", "Do not massage the area", "Watch for signs of internal bleeding", "May require imaging tests"]
    },
    "Wound (Deep)": {
        "mild": ["Clean wound gently with water", "Apply antiseptic solution", "Cover with sterile dressing", "Keep dry for 24 hours", "Monitor for infection signs"],
        "moderate": ["Control bleeding with pressure", "Clean wound thoroughly with saline", "Apply antiseptic", "Use sterile gauze and bandage", "Seek medical attention for possible stitches"],
        "severe": ["Call emergency services", "Apply firm pressure to stop bleeding", "Do not remove any embedded objects", "Keep wound covered with sterile cloth", "Monitor for signs of shock"]
    },
    "Puncture Wound": {
        "mild": ["Wash wound with soap and water", "Apply antiseptic", "Cover with bandage", "Watch for signs of infection", "Keep tetanus shot up to date"],
        "moderate": ["Clean wound thoroughly", "Soak in warm water for 15-20 mins", "Apply antibiotic ointment", "Cover with sterile dressing", "See doctor for tetanus booster if needed"],
        "severe": ["Seek emergency medical care", "Do not remove deep object", "Control bleeding around object", "Keep person still", "Update tetanus vaccination status"]
    },
    "Snake Bite": {
        "mild": ["Stay calm and still", "Keep bitten area below heart level", "Remove jewelry near bite", "Clean wound with soap and water", "Go to hospital immediately"],
        "moderate": ["Call emergency services", "Keep person calm and still", "Immobilize bitten limb", "Do not cut the wound or suck venom", "Remove tight clothing/jewelry near bite"],
        "severe": ["Call 911 immediately", "Keep person lying down and still", "Monitor breathing and consciousness", "Note snake appearance for identification", "Start CPR if needed"]
    },
    "Insect Bite": {
        "mild": ["Remove stinger if visible (scrape it out)", "Wash area with soap and water", "Apply cold compress", "Use calamine lotion or antihistamine cream", "Take oral antihistamine if itchy"],
        "moderate": ["Apply ice to reduce swelling", "Take oral antihistamine", "Apply hydrocortisone cream", "Monitor for allergic reaction", "See doctor if swelling increases"],
        "severe": ["Call emergency services if allergic reaction", "Use epinephrine auto-injector if available", "Monitor breathing and pulse", "Keep person lying down", "Seek immediate medical help"]
    },
    "Animal Bite": {
        "mild": ["Wash wound with soap and water for 10 mins", "Apply antiseptic", "Cover with clean bandage", "Check rabies vaccination status of animal", "See doctor for wound evaluation"],
        "moderate": ["Clean wound thoroughly", "Control any bleeding", "Apply antibiotic ointment", "Cover with sterile dressing", "Go to hospital for rabies prophylaxis"],
        "severe": ["Call emergency services", "Control bleeding with pressure", "Do not clean deep wounds extensively", "Keep person calm", "Rabies and tetanus treatment needed"]
    },
    "Chemical Burn": {
        "mild": ["Remove contaminated clothing carefully", "Flush area with cool water for 20 mins", "Do not apply any creams or ointments", "Cover loosely with sterile gauze", "Seek medical evaluation"],
        "moderate": ["Remove contaminated clothing and jewelry", "Flush with water continuously for 30 mins", "Do not neutralize the chemical yourself", "Cover with clean, dry cloth", "Go to emergency room"],
        "severe": ["Call emergency services", "Continue flushing with water until help arrives", "Remove contaminated clothing if possible", "Monitor breathing if chemical was inhaled", "Bring chemical container to hospital"]
    },
    "Electrical Burn": {
        "mild": ["Ensure power source is turned off", "Check for entry and exit wounds", "Clean burn area gently", "Cover with sterile dressing", "Seek medical evaluation"],
        "moderate": ["Call emergency services", "Do not approach if person is still connected to source", "Check for burns at entry and exit points", "Monitor heart rhythm", "Keep person lying down"],
        "severe": ["Call 911 immediately", "Do not touch person until power is off", "Check breathing and pulse", "Start CPR if needed", "Treat for shock and burns"]
    },
    "Heat Exhaustion": {
        "mild": ["Move to cool/shaded area", "Drip cold water slowly", "Remove excess clothing", "Apply cool cloths to skin", "Rest until symptoms subside"],
        "moderate": ["Move to air-conditioned area", "Lie down and elevate feet", "Drink electrolyte solution", "Apply ice packs to armpits/neck/groin", "Seek medical attention if not improving"],
        "severe": ["Call emergency services", "Move to cool area immediately", "Cool body with ice packs", "Monitor consciousness", "Do not give fluids if confused or unconscious"]
    },
    "Heat Stroke": {
        "mild": ["Move to cool area immediately", "Remove outer clothing", "Apply cool water to skin", "Fan the person", "Seek urgent medical evaluation"],
        "moderate": ["Call emergency services", "Immerse in cool water if possible", "Apply ice packs to neck, armpits, groin", "Monitor body temperature", "Do not give fluids if confused"],
        "severe": ["Call 911 immediately", "Cool body by any means available", "Ice packs on major pulse points", "Monitor breathing and consciousness", "Prepare to start CPR if needed"]
    },
    "Frostbite": {
        "mild": ["Move to warm area", "Remove wet clothing", "Warm affected area in warm water (37-39°C)", "Do not rub or massage", "Drink warm fluids"],
        "moderate": ["Move to warm environment", "Immerse in warm water (not hot)", "Do not break blisters", "Cover with sterile gauze between fingers/toes", "Seek medical attention"],
        "severe": ["Seek emergency medical care", "Do not thaw if risk of refreezing", "Wrap affected area in sterile cloth", "Do not rub or apply direct heat", "Pain medication may be needed"]
    },
    "Hypothermia": {
        "mild": ["Move to warm environment", "Remove wet clothing", "Wrap in warm blankets", "Drink warm (not hot) beverages", "Stay dry and insulated"],
        "moderate": ["Call emergency services", "Move person gently to warm area", "Remove wet clothing carefully", "Apply warm compresses to core (chest, neck, groin)", "Do not warm arms and legs first"],
        "severe": ["Call 911 immediately", "Handle person very gently", "Do not give alcohol or caffeine", "Monitor breathing and pulse", "Start CPR if needed"]
    },
    "Poisoning": {
        "mild": ["Call poison control center", "Do not induce vomiting unless instructed", "Identify what was ingested", "Have the container ready", "Follow poison control instructions"],
        "moderate": ["Call emergency services or poison control", "Do not give anything by mouth", "Save vomit sample if possible", "Identify poison and amount", "Follow medical instructions exactly"],
        "severe": ["Call 911 immediately", "Check breathing and consciousness", "Do not induce vomiting", "Save poison container for identification", "Start CPR if unconscious and not breathing"]
    },
    "Choking": {
        "mild": ["Encourage coughing forcefully", "Stay calm and lean forward", "Do not slap on back if coughing", "Monitor breathing closely", "Seek help if unable to clear airway"],
        "moderate": ["Perform abdominal thrusts (Heimlich maneuver)", "Give 5 back blows between shoulder blades", "Alternate back blows and abdominal thrusts", "Call for emergency help", "Continue until object is dislodged"],
        "severe": ["Call 911 immediately", "Perform Heimlich maneuver", "If person becomes unconscious, start CPR", "Check mouth for visible object", "Continue until help arrives"]
    },
    "Allergic Reaction": {
        "mild": ["Take oral antihistamine", "Apply cold compress to affected areas", "Monitor for worsening symptoms", "Avoid known allergens", "Rest and stay hydrated"],
        "moderate": ["Take antihistamine immediately", "Apply hydrocortisone cream for rash", "Use inhaler if breathing difficulty", "Monitor closely for anaphylaxis", "Seek medical attention if worsening"],
        "severe": ["Call 911 immediately", "Use epinephrine auto-injector if available", "Lie person flat and elevate legs", "Monitor breathing and pulse", "Start CPR if needed"]
    },
    "Shock": {
        "mild": ["Have person lie down", "Elevate legs about 12 inches", "Keep person warm with blanket", "Do not give anything by mouth", "Reassure and stay with person"],
        "moderate": ["Call emergency services", "Lay person on back with elevated legs", "Keep warm with blankets", "Monitor breathing and pulse", "Do not move if spinal injury suspected"],
        "severe": ["Call 911 immediately", "Keep person lying down and still", "Control any external bleeding", "Maintain body warmth", "Monitor consciousness and breathing"]
    },
    "Unconsciousness": {
        "mild": ["Check responsiveness - shake and shout", "Call for help", "Check breathing and pulse", "Place in recovery position if breathing", "Stay with person until help arrives"],
        "moderate": ["Call emergency services", "Check airway, breathing, circulation", "Place in recovery position", "Monitor vital signs", "Loosen tight clothing"],
        "severe": ["Call 911 immediately", "Check breathing - start CPR if absent", "Use AED if available", "Do not give anything by mouth", "Continue CPR until help arrives"]
    },
    "Severe Bleeding": {
        "mild": ["Apply direct pressure with sterile cloth", "Elevate injured area", "Apply pressure bandage", "Keep person calm and still", "Monitor for signs of shock"],
        "moderate": ["Apply firm direct pressure", "Use tourniquet only as last resort", "Keep pressure for 10-15 minutes", "Do not remove blood-soaked dressings", "Add more dressings on top"],
        "severe": ["Call 911 immediately", "Apply direct pressure continuously", "Use tourniquet if trained and necessary", "Keep person lying down and warm", "Monitor consciousness and breathing"]
    },
    "Eye Injury": {
        "mild": ["Do not rub the eye", "Rinse gently with clean water", "Apply cold compress for swelling", "Avoid bright light", "See doctor if symptoms persist"],
        "moderate": ["Do not touch or press the eye", "Cover eye with paper cup or shield", "Do not rinse if object is embedded", "Seek immediate eye care", "Avoid movement of the eye"],
        "severe": ["Call emergency services", "Do not remove any object stuck in eye", "Cover both eyes to minimize movement", "Keep person calm and still", "Do not apply pressure to the eye"]
    }
}

def analyze_injury_image(image_path):
    try:
        import google.generativeai as genai
        import PIL.Image
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            img = PIL.Image.open(image_path)
            response = model.generate_content([
                "Analyze this injury image. Identify: 1) Type of injury 2) Severity (Mild/Moderate/Severe) 3) Brief description. Be concise.",
                img
            ])
            analysis = response.text
            return _parse_ai_response(analysis)
        else:
            return _rule_based_image_analysis(image_path)
    except ImportError:
        return _rule_based_image_analysis(image_path)
    except Exception:
        return _rule_based_image_analysis(image_path)

def _parse_ai_response(text):
    text_lower = text.lower()
    for injury_key, injury_name in sorted(INJURY_TYPE_MAPPING.items(), key=lambda x: -len(x[0])):
        if injury_key in text_lower:
            detected = injury_name
            break
    else:
        detected = "General Injury"

    if "severe" in text_lower or "critical" in text_lower or "serious" in text_lower:
        severity = "Severe"
    elif "moderate" in text_lower:
        severity = "Moderate"
    else:
        severity = "Mild"

    return {
        "injury_type": detected,
        "severity": severity,
        "confidence": 0.85,
        "description": text[:200] + "..." if len(text) > 200 else text,
        "source": "ai"
    }

def _rule_based_image_analysis(image_path):
    return {
        "injury_type": "General Injury",
        "severity": "Moderate",
        "confidence": 0.40,
        "description": "Image analysis requires Google Gemini API key. Using basic assessment.",
        "source": "rule"
    }

def analyze_injury_type(injury_description):
    text = injury_description.lower()
    for keyword, injury_name in sorted(INJURY_TYPE_MAPPING.items(), key=lambda x: -len(x[0])):
        if keyword in text:
            return injury_name
    return "General Injury"

def generate_severity_score(image_analysis):
    return {"severity": image_analysis["severity"], "confidence": image_analysis["confidence"]}

def get_ai_first_aid(injury_type, severity, has_kit, kit_type):
    steps_dict = AI_FIRST_AID_STEPS.get(injury_type, AI_FIRST_AID_STEPS.get("Cut/Laceration"))
    severity_key = severity.lower()
    if severity_key not in steps_dict:
        severity_key = "moderate"
    steps = steps_dict[severity_key]

    if has_kit == "no":
        steps = [s for s in steps if "sterile" not in s.lower() and "bandage" not in s.lower()]
        if not steps:
            steps = ["Stay calm and do not panic", "Apply pressure if there is bleeding",
                     "Keep the injured area still", "Use clean cloth if available", "Go to hospital immediately"]
    elif kit_type == "basic":
        steps = [s for s in steps if "tourniquet" not in s.lower() and "advanced" not in s.lower()]

    return steps

def get_enhanced_first_aid(injury_type, injury_text="", has_kit="yes", kit_type="basic", ai_severity=None, ai_confidence=None):
    if injury_text:
        detected = analyze_injury_type(injury_text)
        if detected != "General Injury":
            injury_type = detected

    if ai_severity and ai_severity.lower() in ("mild", "moderate", "severe"):
        severity_data = {
            "severity": ai_severity.lower().capitalize(),
            "confidence": ai_confidence if ai_confidence else 0.85
        }
    else:
        severity_data = analyze_severity(injury_type, injury_text)
    severity = severity_data["severity"]
    confidence = severity_data["confidence"]

    steps = get_ai_first_aid(injury_type, severity, has_kit, kit_type)
    immediate = get_immediate_actions(severity, injury_type)

    if severity == "Severe":
        steps = immediate + ["---"] + steps

    return {
        "injury_type": injury_type,
        "severity": severity,
        "confidence": confidence,
        "severity_color": get_severity_color(severity),
        "severity_icon": get_severity_icon(severity),
        "immediate_actions": immediate,
        "steps": steps
    }
