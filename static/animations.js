// Exercise Animation System - Animated figures doing workouts

const exerciseAnimations = {
    // Jumping Jacks
    'Jumping Jacks': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes jumpingJack {
                    0%, 100% { transform: translateY(0); }
                    25% { transform: translateY(-15px); }
                    50% { transform: translateY(0); }
                }
                .figure { animation: jumpingJack 1s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="30" r="8" fill="#FF6B6B"/>
                <rect x="48" y="40" width="4" height="20" fill="#FF6B6B"/>
                <line x1="50" y1="40" x2="35" y2="55" stroke="#FF6B6B" stroke-width="2"/>
                <line x1="50" y1="40" x2="65" y2="55" stroke="#FF6B6B" stroke-width="2"/>
                <line x1="50" y1="60" x2="40" y2="90" stroke="#FF6B6B" stroke-width="2"/>
                <line x1="50" y1="60" x2="60" y2="90" stroke="#FF6B6B" stroke-width="2"/>
            </g>
        </svg>
    `,
    
    // Push-ups
    'Push-ups': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes pushup {
                    0%, 100% { transform: skewY(-5deg); }
                    50% { transform: skewY(15deg); }
                }
                .figure { animation: pushup 1s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="30" r="8" fill="#4ECDC4"/>
                <rect x="40" y="40" width="20" height="4" fill="#4ECDC4"/>
                <line x1="40" y1="42" x2="25" y2="55" stroke="#4ECDC4" stroke-width="2"/>
                <line x1="60" y1="42" x2="75" y2="55" stroke="#4ECDC4" stroke-width="2"/>
                <rect x="48" y="45" width="4" height="25" fill="#4ECDC4"/>
                <line x1="50" y1="70" x2="40" y2="100" stroke="#4ECDC4" stroke-width="2"/>
                <line x1="50" y1="70" x2="60" y2="100" stroke="#4ECDC4" stroke-width="2"/>
            </g>
        </svg>
    `,
    
    // Squats
    'Squats': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes squat {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(20px); }
                }
                .figure { animation: squat 1s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="30" r="8" fill="#95E1D3"/>
                <rect x="48" y="40" width="4" height="15" fill="#95E1D3"/>
                <line x1="50" y1="40" x2="35" y2="50" stroke="#95E1D3" stroke-width="2"/>
                <line x1="50" y1="40" x2="65" y2="50" stroke="#95E1D3" stroke-width="2"/>
                <line x1="35" y1="50" x2="30" y2="100" stroke="#95E1D3" stroke-width="2"/>
                <line x1="65" y1="50" x2="70" y2="100" stroke="#95E1D3" stroke-width="2"/>
            </g>
        </svg>
    `,
    
    // Lunges
    'Lunges': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes lunge {
                    0%, 100% { transform: scaleX(1); }
                    50% { transform: scaleX(-1); }
                }
                .figure { animation: lunge 2s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="30" r="8" fill="#F38181"/>
                <rect x="48" y="40" width="4" height="15" fill="#F38181"/>
                <line x1="50" y1="40" x2="35" y2="50" stroke="#F38181" stroke-width="2"/>
                <line x1="50" y1="40" x2="65" y2="50" stroke="#F38181" stroke-width="2"/>
                <line x1="50" y1="55" x2="35" y2="100" stroke="#F38181" stroke-width="2"/>
                <line x1="50" y1="55" x2="70" y2="85" stroke="#F38181" stroke-width="2"/>
            </g>
        </svg>
    `,
    
    // Plank
    'Plank': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes plank {
                    0%, 100% { transform: translateY(-5px); }
                    50% { transform: translateY(5px); }
                }
                .figure { animation: plank 1s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="80" r="8" fill="#AA96DA"/>
                <line x1="50" y1="88" x2="30" y2="100" stroke="#AA96DA" stroke-width="2"/>
                <line x1="50" y1="88" x2="70" y2="100" stroke="#AA96DA" stroke-width="2"/>
                <rect x="30" y="98" width="40" height="3" fill="#AA96DA"/>
                <line x1="30" y1="100" x2="20" y2="120" stroke="#AA96DA" stroke-width="2"/>
                <line x1="70" y1="100" x2="80" y2="120" stroke="#AA96DA" stroke-width="2"/>
            </g>
        </svg>
    `,
    
    // Yoga - Tree Pose
    'Tree Pose': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes balance {
                    0%, 100% { transform: rotate(-2deg); }
                    50% { transform: rotate(2deg); }
                }
                .figure { animation: balance 2s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="30" r="8" fill="#FCBAD3"/>
                <line x1="50" y1="38" x2="50" y2="60" stroke="#FCBAD3" stroke-width="2"/>
                <line x1="50" y1="40" x2="35" y2="50" stroke="#FCBAD3" stroke-width="2"/>
                <line x1="50" y1="40" x2="65" y2="50" stroke="#FCBAD3" stroke-width="2"/>
                <line x1="50" y1="60" x2="45" y2="100" stroke="#FCBAD3" stroke-width="2"/>
                <line x1="50" y1="60" x2="70" y2="85" stroke="#FCBAD3" stroke-width="2"/>
            </g>
        </svg>
    `,
    
    // Yoga - Downward Dog
    'Downward Dog': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes downdog {
                    0%, 100% { transform: translateY(-5px); }
                    50% { transform: translateY(5px); }
                }
                .figure { animation: downdog 1.5s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="70" r="8" fill="#FFD93D"/>
                <rect x="45" y="50" width="10" height="25" fill="#FFD93D"/>
                <line x1="45" y1="50" x2="35" y2="30" stroke="#FFD93D" stroke-width="2"/>
                <line x1="55" y1="50" x2="65" y2="30" stroke="#FFD93D" stroke-width="2"/>
                <line x1="50" y1="75" x2="40" y2="110" stroke="#FFD93D" stroke-width="2"/>
                <line x1="50" y1="75" x2="60" y2="110" stroke="#FFD93D" stroke-width="2"/>
            </g>
        </svg>
    `,
    
    // Meditation - Sitting
    'Meditation': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes breathe {
                    0%, 100% { opacity: 0.8; }
                    50% { opacity: 1; }
                }
                .figure { animation: breathe 3s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="40" r="12" fill="#A8DADC"/>
                <circle cx="45" cy="37" r="2" fill="white"/>
                <circle cx="55" cy="37" r="2" fill="white"/>
                <line x1="50" y1="50" x2="50" y2="70" stroke="#A8DADC" stroke-width="2"/>
                <line x1="50" y1="60" x2="35" y2="65" stroke="#A8DADC" stroke-width="2"/>
                <line x1="50" y1="60" x2="65" y2="65" stroke="#A8DADC" stroke-width="2"/>
                <path d="M 40 75 Q 50 85 60 75" stroke="#A8DADC" stroke-width="2" fill="none"/>
            </g>
        </svg>
    `,
    
    // Default exercise animation
    'default': `
        <svg viewBox="0 0 100 200" class="exercise-animation">
            <style>
                @keyframes wave {
                    0%, 100% { transform: rotate(0deg); }
                    25% { transform: rotate(-10deg); }
                    75% { transform: rotate(10deg); }
                }
                .figure { animation: wave 1s infinite; animation-play-state: paused; } 
                svg.playing .figure { animation-play-state: running; }
            </style>
            <g class="figure">
                <circle cx="50" cy="30" r="8" fill="#6C5CE7"/>
                <rect x="48" y="40" width="4" height="20" fill="#6C5CE7"/>
                <line x1="50" y1="40" x2="35" y2="55" stroke="#6C5CE7" stroke-width="2"/>
                <line x1="50" y1="40" x2="65" y2="55" stroke="#6C5CE7" stroke-width="2"/>
                <line x1="50" y1="60" x2="40" y2="90" stroke="#6C5CE7" stroke-width="2"/>
                <line x1="50" y1="60" x2="60" y2="90" stroke="#6C5CE7" stroke-width="2"/>
            </g>
        </svg>
    `
};

// Create SVG animation for an exercise
function getExerciseAnimation(exerciseName) {
    // Check if exact match exists
    if (exerciseAnimations[exerciseName]) {
        return exerciseAnimations[exerciseName];
    }
    
    // Check for partial matches
    for (let key in exerciseAnimations) {
        if (exerciseName.toLowerCase().includes(key.toLowerCase()) || 
            key.toLowerCase().includes(exerciseName.toLowerCase())) {
            return exerciseAnimations[key];
        }
    }
    
    // Return default if no match
    return exerciseAnimations['default'];
}

// Display animation for exercises
function displayExerciseAnimation(containerId, exerciseName) {
    const container = document.getElementById(containerId);
    if (container) {
        const animation = getExerciseAnimation(exerciseName);
        container.innerHTML = animation;
    }
}

// Initialize all animations on page load
document.addEventListener('DOMContentLoaded', function() {
    // Find all exercise animation containers and populate them
    const animationContainers = document.querySelectorAll('[data-exercise-animation]');
    animationContainers.forEach(container => {
        const exerciseName = container.getAttribute('data-exercise-animation');
        container.innerHTML = getExerciseAnimation(exerciseName);
    });
});
