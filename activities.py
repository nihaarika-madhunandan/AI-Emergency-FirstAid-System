from age_categories import get_age_group, get_intensity, get_intensity_level, get_duration_recommendation

EXERCISES_BY_AGE = {
    "kids": {
        "morning": {
            "title": "Morning Fun Workout",
            "description": "Playful movement designed for short energy bursts.",
            "exercise_duration": "2-3 mins",
            "exercises": [
                {"name": "Jumping Jacks", "focus": "Cardio and coordination", "youtube_id": "H1qPzxQDj2w"},
                {"name": "Running in Place", "focus": "Light endurance", "youtube_id": "8gfScw0f_0E"},
                {"name": "Dancing", "focus": "Rhythm and balance", "youtube_id": "xRYjSRIPOL0"},
                {"name": "Basic Stretching", "focus": "Muscle warm-up", "youtube_id": "y3i3cXyl6x0"}
            ],
            "intensity": "Low"
        },
        "evening": {
            "title": "Evening Active Play",
            "description": "Gentle activities that help the body wind down.",
            "exercise_duration": "2-3 mins",
            "exercises": [
                {"name": "Hopscotch", "focus": "Balance and coordination", "youtube_id": "326GR2A7q-s"},
                {"name": "Skipping", "focus": "Cardio", "youtube_id": "H1qPzxQDj2w"},
                {"name": "Animal Walks", "focus": "Mobility", "youtube_id": "8gfScw0f_0E"}
            ],
            "intensity": "Low"
        },
        "quick": {
            "title": "Quick Energy Boost",
            "description": "Tiny bursts of movement for a pick-me-up.",
            "exercise_duration": "2 mins",
            "exercises": [
                {"name": "Star Jumps", "focus": "Whole-body movement", "youtube_id": "326GR2A7q-s"},
                {"name": "Arm Circles", "focus": "Shoulder mobility", "youtube_id": "y3i3cXyl6x0"},
                {"name": "Toe Touches", "focus": "Flexibility", "youtube_id": "xRYjSRIPOL0"}
            ],
            "intensity": "Low"
        }
    },
    "teens": {
        "morning": {
            "title": "Morning Flow",
            "description": "A focused yet manageable start to the day.",
            "exercise_duration": "2-3 mins",
            "exercises": [
                {"name": "Burpees", "focus": "Cardio and strength", "youtube_id": "6OTUrjItnf0"},
                {"name": "Mountain Climbers", "focus": "Core stability", "youtube_id": "btEjeYDRz3E"},
                {"name": "Push-ups", "focus": "Upper body strength", "youtube_id": "M0ECBD6egbI"}
            ],
            "intensity": "Low-Medium"
        },
        "evening": {
            "title": "Evening Strength",
            "description": "Build endurance without overloading the body.",
            "exercise_duration": "2-3 mins",
            "exercises": [
                {"name": "Lunges", "focus": "Lower body strength", "youtube_id": "ixjdNUtWN-Y"},
                {"name": "Squats", "focus": "Leg power", "youtube_id": "6k6cWxrBpK8"},
                {"name": "Plank", "focus": "Core control", "youtube_id": "btEjeYDRz3E"}
            ],
            "intensity": "Low-Medium"
        },
        "quick": {
            "title": "Quick Power Session",
            "description": "Short rounds that keep energy levels up.",
            "exercise_duration": "2 mins",
            "exercises": [
                {"name": "Jump Squats", "focus": "Explosive movement", "youtube_id": "6k6cWxrBpK8"},
                {"name": "Crunches", "focus": "Core strength", "youtube_id": "ixjdNUtWN-Y"},
                {"name": "Leg Raises", "focus": "Hip flexibility", "youtube_id": "M0ECBD6egbI"}
            ],
            "intensity": "Low-Medium"
        }
    },
    "adults": {
        "morning": {
            "title": "Moderate Cardio",
            "description": "Balanced movement for steadier energy and stamina.",
            "exercise_duration": "2-3 mins",
            "exercises": [
                {"name": "Brisk Walking", "focus": "Steady cardio", "youtube_id": "pNOrQoqybW8"},
                {"name": "Cycling", "focus": "Leg endurance", "youtube_id": "ILodiqpiUsc"},
                {"name": "Stretching", "focus": "Mobility", "youtube_id": "hpv-fcZt9t0"}
            ],
            "intensity": "Medium"
        },
        "evening": {
            "title": "Core & Flexibility",
            "description": "A calm routine to support posture and recovery.",
            "exercise_duration": "2-3 mins",
            "exercises": [
                {"name": "Yoga Flow", "focus": "Stretch and balance", "youtube_id": "v7AYKMP6rOE"},
                {"name": "Pilates", "focus": "Core strength", "youtube_id": "DBm1bUAR_sQ"},
                {"name": "Balance Training", "focus": "Stability", "youtube_id": "SUDFpYeiLl4"}
            ],
            "intensity": "Medium"
        },
        "quick": {
            "title": "Quick Fitness Boost",
            "description": "Simple routines that fit into a packed schedule.",
            "exercise_duration": "2 mins",
            "exercises": [
                {"name": "Bodyweight Squats", "focus": "Lower body strength", "youtube_id": "otzWCWpuW-A"},
                {"name": "Push-ups", "focus": "Upper body strength", "youtube_id": "IODxDxX7oi4"},
                {"name": "Planks", "focus": "Core endurance", "youtube_id": "ASdvN_XEl_c"}
            ],
            "intensity": "Medium"
        }
    },
    "seniors": {
        "morning": {
            "title": "Gentle Morning Routine",
            "description": "Safe, low-impact movement for the day ahead.",
            "exercise_duration": "2 mins",
            "exercises": [
                {"name": "Walking", "focus": "Gentle cardio", "youtube_id": "UeU_jdHo_e8"},
                {"name": "Arm Raises", "focus": "Mobility", "youtube_id": "HwES4OSc9H8"},
                {"name": "Deep Breathing", "focus": "Relaxation", "youtube_id": "GskHIA3iE5Q"}
            ],
            "intensity": "Low"
        },
        "evening": {
            "title": "Balance & Stability",
            "description": "Support coordination and steadiness with easy movement.",
            "exercise_duration": "2-3 mins",
            "exercises": [
                {"name": "Heel-to-Toe Walk", "focus": "Balance", "youtube_id": "2wNoTsxlmDI"},
                {"name": "Chair Stands", "focus": "Lower body strength", "youtube_id": "UiGotC1cn6M"},
                {"name": "Gentle Stretching", "focus": "Flexibility", "youtube_id": "UeU_jdHo_e8"}
            ],
            "intensity": "Low"
        },
        "quick": {
            "title": "Quick Mobility Boost",
            "description": "Small movement breaks to reduce stiffness.",
            "exercise_duration": "2 mins",
            "exercises": [
                {"name": "Shoulder Rolls", "focus": "Neck and shoulder relief", "youtube_id": "HwES4OSc9H8"},
                {"name": "Seated Marching", "focus": "Gentle movement", "youtube_id": "UiGotC1cn6M"},
                {"name": "Toe Taps", "focus": "Foot mobility", "youtube_id": "GskHIA3iE5Q"}
            ],
            "intensity": "Low"
        }
    }
}

YOGA_BY_AGE = {
    "kids": {
        "yoga": {
            "title": "Fun Yoga for Kids",
            "duration": "15 mins",
            "description": "Playful yoga poses to build flexibility and focus",
            "intensity": "Low",
            "poses": ["Tree Pose", "Downward Dog", "Cat-Cow", "Butterfly Pose", "Happy Baby"],
            "youtube_ids": ["vMMRb10LtGM", "8oGR5xucItI", "4ZpkRAcgws4", "CBko9JPMtHs", "vMMRb10LtGM"],
            "benefits": ["Flexibility", "Focus", "Body Awareness", "Fun Exercise"]
        }
    },
    "teens": {
        "yoga": {
            "title": "Teen Yoga Flow",
            "duration": "20-25 mins",
            "description": "Build strength and flexibility with dynamic poses",
            "intensity": "Low-Medium",
            "poses": ["Sun Salutation", "Warrior Series", "Triangle Pose", "Bridge Pose", "Cobra Pose"],
            "youtube_ids": ["L4Z7lix6Qao", "7kgZnJqzNaU", "6kJgTouHHeE", "UPszTB6UzaA", "7kgZnJqzNaU"],
            "benefits": ["Strength", "Flexibility", "Stress Relief", "Confidence"]
        }
    },
    "adults": {
        "yoga": {
            "title": "Therapeutic Yoga",
            "duration": "20-25 mins",
            "description": "Healing poses for stress relief and body rejuvenation",
            "intensity": "Medium",
            "poses": ["Gentle Flow", "Child's Pose", "Legs-Up-The-Wall", "Seated Twist", "Corpse Pose"],
            "youtube_ids": ["aKsu112bzHE", "rJZw__B-RmY", "4mUyca7LKAw", "pWobp3phsEU", "CYC3apoMRDw"],
            "benefits": ["Stress Relief", "Pain Management", "Relaxation", "Better Sleep"]
        }
    },
    "seniors": {
        "yoga": {
            "title": "Gentle Chair Yoga",
            "duration": "15-20 mins",
            "description": "Safe, supported yoga for mobility and relaxation",
            "intensity": "Low",
            "poses": ["Seated Mountain", "Chair Cat-Cow", "Seated Forward Fold", "Ankle Stretch", "Shoulder Rolls"],
            "youtube_ids": ["1DYH5ud3zHo", "Znm51BKoBfs", "U_jdXFfegKE", "WkYz1g47Hj0", "7yjPnhRbcV0"],
            "benefits": ["Mobility", "Joint Health", "Balance", "Calmness"]
        }
    }
}

MEDITATION_BY_AGE = {
    "kids": {
        "breathwork": {
            "title": "Fun Breathing Games",
            "duration": "5 mins",
            "description": "Playful breathing exercises for young minds",
            "intensity": "Low",
            "benefits": ["Calmness", "Focus", "Emotional Regulation"]
        },
        "mindfulness": {
            "title": "Mindful Moments",
            "duration": "5 mins",
            "description": "Simple awareness exercises for children",
            "intensity": "Low",
            "benefits": ["Awareness", "Patience", "Kindness"]
        },
        "sleep": {
            "title": "Bedtime Stories Meditation",
            "duration": "10 mins",
            "description": "Guided imagery for peaceful sleep",
            "intensity": "Low",
            "benefits": ["Better Sleep", "Relaxation", "Imagination"]
        }
    },
    "teens": {
        "breathwork": {
            "title": "Focus Breathing",
            "duration": "10 mins",
            "description": "Breathing techniques to improve concentration",
            "intensity": "Low-Medium",
            "benefits": ["Better Focus", "Exam Prep", "Stress Management"]
        },
        "mindfulness": {
            "title": "Teen Mindfulness",
            "duration": "10 mins",
            "description": "Stay present and manage teenage stress",
            "intensity": "Low-Medium",
            "benefits": ["Emotional Balance", "Self-awareness", "Confidence"]
        },
        "sleep": {
            "title": "Teen Sleep Meditation",
            "duration": "15 mins",
            "description": "Release daily stress and drift into deep sleep",
            "intensity": "Low",
            "benefits": ["Deep Sleep", "Anxiety Relief", "Mental Clarity"]
        }
    },
    "adults": {
        "breathwork": {
            "title": "Calm Breathing",
            "duration": "15-20 mins",
            "description": "Reduce daily stress with deep breathing",
            "intensity": "Low",
            "benefits": ["Stress Relief", "Better Focus", "Improved Sleep"]
        },
        "mindfulness": {
            "title": "Adult Mindfulness",
            "duration": "15-20 mins",
            "description": "Find balance in a busy life",
            "intensity": "Low-Medium",
            "benefits": ["Work-Life Balance", "Emotional Stability", "Peace of Mind"]
        },
        "sleep": {
            "title": "Sleep Therapy",
            "duration": "20 mins",
            "description": "Guided sleep meditation for adults",
            "intensity": "Low",
            "benefits": ["Better Sleep Quality", "Relaxation", "Rest"]
        }
    },
    "seniors": {
        "breathwork": {
            "title": "Gentle Breathing",
            "duration": "10-15 mins",
            "description": "Calming breathing exercises for seniors",
            "intensity": "Low",
            "benefits": ["Calmness", "Better Circulation", "Relaxation"]
        },
        "mindfulness": {
            "title": "Peaceful Mindfulness",
            "duration": "10-15 mins",
            "description": "Gentle awareness practice for inner peace",
            "intensity": "Low",
            "benefits": ["Inner Peace", "Acceptance", "Contentment"]
        },
        "sleep": {
            "title": "Restful Sleep Meditation",
            "duration": "10-15 mins",
            "description": "Gentle guidance to peaceful sleep",
            "intensity": "Low",
            "benefits": ["Better Sleep", "Relaxation", "Rest"]
        }
    }
}


def get_exercises_by_age(age):
    group = get_age_group(age)
    exercises = EXERCISES_BY_AGE.get(group, EXERCISES_BY_AGE["adults"])
    return {
        "exercises": exercises,
        "age_group": group,
        "intensity": get_intensity(age),
        "duration": get_duration_recommendation(age)
    }


def get_yoga_by_age(age):
    group = get_age_group(age)
    yoga = YOGA_BY_AGE.get(group, YOGA_BY_AGE["adults"])
    return {
        "yoga": yoga["yoga"],
        "age_group": group,
        "intensity": get_intensity(age)
    }


def get_meditation_by_age(age):
    group = get_age_group(age)
    meditation = MEDITATION_BY_AGE.get(group, MEDITATION_BY_AGE["adults"])
    return {
        "meditations": meditation,
        "age_group": group,
        "intensity": get_intensity(age)
    }

AGE_SAFETY_WARNINGS = {
    "kids": "⚠️ Adult supervision recommended. Keep exercises fun and non-competitive.",
    "teens": "⚠️ Focus on proper form over intensity. Listen to your body.",
    "adults": "⚠️ Consult your doctor before starting new routines. Stay hydrated.",
    "seniors": "⚠️ Consult your doctor first. Use support when needed. Stop if you feel pain."
}


def get_safety_warning(age):
    return AGE_SAFETY_WARNINGS.get(get_age_group(age), "")
