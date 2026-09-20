MENSTRUAL_PROBLEMS = [
    {"id": "cramps", "label": "Menstrual cramps"},
    {"id": "back_pain", "label": "Back pain during periods"},
    {"id": "headache", "label": "Headache"},
    {"id": "bloating", "label": "Bloating"},
    {"id": "fatigue", "label": "Fatigue"},
    {"id": "nausea", "label": "Mild nausea"},
    {"id": "irregular", "label": "Irregular periods"},
    {"id": "heavy_bleeding", "label": "Heavy menstrual bleeding"},
    {"id": "other", "label": "Other menstrual-related concerns"},
]

DISCLAIMER = (
    "This section provides general health information only. It is not a diagnosis, "
    "prescription, or a substitute for professional medical advice, examination, or treatment. "
    "If you are worried about your symptoms, contact a qualified healthcare professional."
)

_GUIDANCE = {
    "cramps": {
        "title": "Menstrual cramps",
        "serious": False,
        "self_care": [
            "Use a heating pad or warm compress on the lower abdomen.",
            "Try gentle movement such as walking or stretching, if it feels comfortable.",
            "Rest in a comfortable position and use slow, steady breathing.",
            "Stay hydrated and choose lighter meals if you feel unwell.",
            "If a clinician has previously said an over-the-counter pain reliever is suitable for you, follow the label directions. Do not start a new medicine without checking with a pharmacist or doctor, especially if you are pregnant, have other conditions, or take other medicines.",
        ],
        "immediate": [
            "Sit or lie down in a quiet place.",
            "Apply warmth to the lower abdomen or lower back.",
            "Sip water slowly.",
            "Avoid intense exercise until the pain eases.",
        ],
        "seek_care": [
            "Pain is sudden, severe, or much worse than your usual period pain.",
            "Pain is accompanied by fever, fainting, vomiting you cannot keep down, or very heavy bleeding.",
            "Cramps stop you from daily activities despite usual self-care.",
            "You could be pregnant and have pelvic pain or bleeding.",
        ],
    },
    "back_pain": {
        "title": "Back pain during periods",
        "serious": False,
        "self_care": [
            "Apply a warm compress to the lower back.",
            "Try gentle stretches for the lower back and hips if they do not increase pain.",
            "Use a supportive chair or lie on your side with a pillow between your knees.",
            "Avoid heavy lifting until the discomfort settles.",
        ],
        "immediate": [
            "Change position: stand, walk slowly, or lie on your side.",
            "Use warmth on the lower back.",
            "Rest if the pain is sharp with movement.",
        ],
        "seek_care": [
            "Back pain is sudden and severe, or follows a fall or injury.",
            "You have numbness, weakness in the legs, or loss of bladder or bowel control — seek emergency care.",
            "Pain is accompanied by fever, unexplained weight loss, or bleeding that is much heavier than usual.",
            "Pain continues after your period ends or keeps getting worse.",
        ],
    },
    "headache": {
        "title": "Headache around the menstrual cycle",
        "serious": False,
        "self_care": [
            "Rest in a dim, quiet room.",
            "Drink water; dehydration can worsen headaches.",
            "A cool cloth on the forehead may help some people.",
            "Keep a simple symptom diary (timing around your cycle) to share with a clinician if headaches are frequent.",
        ],
        "immediate": [
            "Sit or lie down and reduce bright light and noise.",
            "Sip water.",
            "Do not drive if the headache is severe or you feel dizzy.",
        ],
        "seek_care": [
            "This is the worst headache of your life, or it started suddenly like a thunderclap — seek emergency care.",
            "Headache with confusion, fainting, weakness, trouble speaking, stiff neck, fever, or vision loss — seek emergency care.",
            "Headaches are new for you, much more frequent, or not responding to your usual self-care.",
            "You are pregnant and have a new or severe headache.",
        ],
    },
    "bloating": {
        "title": "Bloating",
        "serious": False,
        "self_care": [
            "Eat smaller meals and limit very salty foods if they worsen swelling.",
            "Sip water through the day.",
            "Gentle walking may ease abdominal tightness.",
            "Wear comfortable clothing around the waist.",
        ],
        "immediate": [
            "Loosen tight clothing.",
            "Sit upright rather than lying flat after a large meal.",
            "Avoid carbonated drinks if they increase gas.",
        ],
        "seek_care": [
            "Bloating is severe, sudden, or one-sided and does not ease.",
            "You have persistent vomiting, inability to pass stool or gas, or severe abdominal pain — seek urgent care.",
            "Bloating is ongoing (not just around periods) or is paired with unexplained weight loss or feeling full quickly.",
        ],
    },
    "fatigue": {
        "title": "Fatigue",
        "serious": False,
        "self_care": [
            "Allow extra rest around your period if you can.",
            "Keep a regular sleep schedule and limit late caffeine.",
            "Eat regular meals with iron-containing foods if your clinician has not advised otherwise.",
            "Use short breaks and light movement rather than pushing through exhaustion.",
        ],
        "immediate": [
            "Sit or lie down if you feel lightheaded.",
            "Drink water and have a small snack if you have not eaten.",
            "Avoid driving or operating machinery if you feel faint.",
        ],
        "seek_care": [
            "Fatigue is extreme, sudden, or paired with fainting, chest pain, shortness of breath, or very heavy bleeding.",
            "You have ongoing tiredness, paleness, or dizziness across several cycles — a clinician can check for causes such as low iron; this app cannot diagnose that.",
            "Fatigue stops you from daily activities for more than a few days after your period.",
        ],
    },
    "nausea": {
        "title": "Mild nausea",
        "serious": False,
        "self_care": [
            "Sip water, oral rehydration fluid, or weak tea in small amounts.",
            "Eat small, bland snacks if you can keep them down (for example dry crackers).",
            "Rest sitting upright or slightly reclined.",
            "Avoid strong smells and greasy foods until it settles.",
        ],
        "immediate": [
            "Sit still and breathe slowly.",
            "Sip fluids; do not force a large meal.",
            "Use a cool cloth on the neck if it helps.",
        ],
        "seek_care": [
            "Vomiting is persistent, you cannot keep fluids down, or you become dehydrated (very dry mouth, little urine, dizziness).",
            "Nausea comes with severe abdominal pain, fainting, chest pain, or a severe headache.",
            "You could be pregnant, or nausea is new and severe.",
            "There is blood in vomit — seek urgent care.",
        ],
    },
    "irregular": {
        "title": "Irregular periods",
        "serious": True,
        "self_care": [
            "Track cycle dates, flow, and associated symptoms in a calendar or app.",
            "Note recent changes such as stress, travel, illness, weight change, or new medicines to share with a clinician.",
            "Use usual period self-care for cramps or tiredness if they occur.",
            "Do not try to ‘correct’ a cycle with unprescribed hormones or supplements.",
        ],
        "immediate": [
            "Write down the date, how heavy the flow is, and any pain, dizziness, or other symptoms.",
            "Use period products as needed and rest if you feel unwell.",
            "If bleeding is soaking products very quickly, treat this as heavy bleeding (see that topic) and get medical help.",
        ],
        "seek_care": [
            "This information cannot tell you why your cycle changed and is not a diagnosis.",
            "See a clinician if periods suddenly become much more frequent, much less frequent, stop for several months (and you are not pregnant and not in menopause), or change a lot from your usual pattern.",
            "Seek care promptly if irregular bleeding happens after menopause, after sex, or with pelvic pain, fever, or dizziness.",
            "If you might be pregnant and have bleeding or pain, get medical advice without delay.",
        ],
    },
    "heavy_bleeding": {
        "title": "Heavy menstrual bleeding",
        "serious": True,
        "self_care": [
            "Rest and avoid strenuous activity until you can be assessed if bleeding is much heavier than usual.",
            "Drink fluids.",
            "Lie down if you feel faint; elevate your legs if you are dizzy.",
            "Keep used products to help describe soaking (for example how often you change a pad or tampon) when you speak to a clinician.",
        ],
        "immediate": [
            "If you feel faint, dizzy, confused, or short of breath, seek emergency care.",
            "Sit or lie down; do not drive yourself if you feel unwell.",
            "Use additional period products and note how quickly they soak.",
        ],
        "seek_care": [
            "This app cannot diagnose the cause of heavy bleeding.",
            "Seek urgent or emergency care if you soak a pad or tampon every hour for several hours, pass large clots, feel faint, or bleed heavily with pregnancy possible.",
            "See a clinician if heavy periods are new for you, last longer than usual, or leave you exhausted or lightheaded.",
            "Bleeding after menopause, or bleeding with severe pain or fever, needs prompt medical assessment.",
        ],
    },
    "other": {
        "title": "Other menstrual-related concerns",
        "serious": True,
        "self_care": [
            "Note what you feel, when it started, and how it relates to your cycle.",
            "Use comfort measures (rest, warmth, hydration) for mild, familiar symptoms only.",
            "Avoid unused medicines, unprescribed treatments, or delaying care in order to ‘wait it out’ if symptoms are new or severe.",
        ],
        "immediate": [
            "If symptoms feel sudden, severe, or frightening, seek emergency or urgent care rather than waiting on this page.",
            "If you have mild, familiar period discomfort, rest and hydrate while you decide whether you need a clinician.",
        ],
        "seek_care": [
            "This feature cannot identify a specific condition.",
            "Contact a healthcare professional for symptoms that are new, worsening, or different from your usual cycle.",
            "Seek emergency care for fainting, severe pain, very heavy bleeding, chest pain, trouble breathing, one-sided weakness, or thoughts of self-harm.",
            "If you might be pregnant, have a fever with pelvic pain, or have bleeding after menopause, get medical care promptly.",
        ],
    },
}


def get_menstrual_guidance(problem_id):
    if not problem_id or problem_id not in _GUIDANCE:
        return None
    data = dict(_GUIDANCE[problem_id])
    data["id"] = problem_id
    data["disclaimer"] = DISCLAIMER
    return data


def list_menstrual_problems():
    return MENSTRUAL_PROBLEMS
