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

    // Initialize Theme & Health Reminders
    initTheme();
    ensureThemeToggle();
    ensureReminderTrigger();
    initHealthReminders();
});

/* ============================================
   THEME MANAGER (DARK / LIGHT MODE TOGGLE)
   ============================================ */

function initTheme() {
    const savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    setTheme(savedTheme);
}

function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    document.body.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);

    const toggleBtns = document.querySelectorAll('.theme-toggle-btn');
    toggleBtns.forEach(btn => {
        if (theme === 'dark') {
            btn.innerHTML = btn.classList.contains('is-floating')
                ? '<i class="fas fa-sun"></i>'
                : '<i class="fas fa-sun text-amber-400"></i> <span>Light Mode</span>';
            btn.classList.add('is-dark');
            btn.setAttribute('title', 'Switch to Light Mode');
        } else {
            btn.innerHTML = btn.classList.contains('is-floating')
                ? '<i class="fas fa-moon"></i>'
                : '<i class="fas fa-moon text-indigo-400"></i> <span>Dark Mode</span>';
            btn.classList.remove('is-dark');
            btn.setAttribute('title', 'Switch to Dark Mode');
        }
    });
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
}

// Auto-create a theme toggle button if the page does not ship one
function ensureThemeToggle() {
    if (document.querySelector('.theme-toggle-btn')) return;

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'theme-toggle-btn is-floating';
    btn.onclick = toggleTheme;
    document.body.appendChild(btn);
    setTheme(document.documentElement.getAttribute('data-theme') || 'light');
}

/* ============================================
   HEALTH REMINDERS & NOTIFICATION SYSTEM
   ============================================ */

const HEALTH_TIPS = [
    {
        icon: 'fa-droplet',
        color: '#06B6D4',
        title: '💧 Hydration Break',
        body: 'Time to take a sip of water! Staying hydrated maintains energy, focus, and healthy joint function.'
    },
    {
        icon: 'fa-user-nurse',
        color: '#10B981',
        title: '🧘 Posture Check',
        body: 'Sit up straight, roll your shoulders back, and un-hunch your neck. Your back will thank you!'
    },
    {
        icon: 'fa-wind',
        color: '#8B5CF6',
        title: '🫁 Deep Breathing Break',
        body: 'Take 3 slow, deep breaths right now. Inhale deeply through your nose, hold 3 seconds, exhale slowly.'
    },
    {
        icon: 'fa-eye',
        color: '#F59E0B',
        title: '👀 20-20-20 Eye Care',
        body: 'Give your eyes a break! Look away from your screen at an object 20 feet away for 20 seconds.'
    },
    {
        icon: 'fa-child',
        color: '#EC4899',
        title: '🦵 Quick Stretch',
        body: 'Unclench your jaw, relax your facial muscles, stretch out your hands, and flex your fingers.'
    },
    {
        icon: 'fa-heart',
        color: '#EF4444',
        title: '❤️ Mindful Health Check',
        body: 'Remember to take periodic health breaks throughout your day. Your health is your greatest wealth!'
    }
];

let lastTipIndex = -1;
let reminderInterval = null;
let idleWatchInterval = null;
let lastActivity = Date.now();

const REMINDER_INTERVAL_MS = 10 * 60 * 1000;
const IDLE_THRESHOLD_MS = 5 * 60 * 1000;

function initHealthReminders() {
    // Ensure toast container exists
    if (!document.getElementById('health-reminder-container')) {
        const container = document.createElement('div');
        container.id = 'health-reminder-container';
        document.body.appendChild(container);
    }

    // Request desktop notification permissions on interaction
    if ("Notification" in window && Notification.permission === "default") {
        document.addEventListener('click', function requestOnce() {
            Notification.requestPermission();
            document.removeEventListener('click', requestOnce);
        }, { once: true });
    }

    // Schedule a periodic health tip (every 10 minutes)
    if (!reminderInterval) {
        reminderInterval = setInterval(triggerHealthReminder, REMINDER_INTERVAL_MS);
    }

    // Gentle reminder when the user is idle (no mouse/keyboard activity for 5 min)
    function markActivity() { lastActivity = Date.now(); }
    ['mousemove', 'keydown', 'click', 'scroll', 'touchstart'].forEach(function (evt) {
        document.addEventListener(evt, markActivity, { passive: true });
    });

    if (!idleWatchInterval) {
        idleWatchInterval = setInterval(function () {
            if (document.visibilityState === 'hidden') return;
            if (Date.now() - lastActivity >= IDLE_THRESHOLD_MS) {
                lastActivity = Date.now();
                triggerHealthReminder('We noticed it has been quiet for a while — stand up, stretch, and take a few deep breaths. Your body will thank you!');
            }
        }, 60 * 1000);
    }

    // Trigger notification when tab visibility changes (user leaves or comes back)
    document.addEventListener('visibilitychange', function() {
        if (document.visibilityState === 'hidden') {
            sendBackgroundNotification();
        } else {
            // Show welcome back toast when user returns
            setTimeout(() => {
                triggerHealthReminder('Welcome back! Take a moment to check your posture & hydrate.');
            }, 1000);
        }
    });
}

// Auto-create a floating "Health Tip" trigger button if the page does not ship one
function ensureReminderTrigger() {
    if (document.querySelector('.reminder-trigger-btn')) return;

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'reminder-trigger-btn';
    btn.innerHTML = '<i class="fas fa-heartbeat"></i> <span>Health Tip</span>';
    btn.title = 'Get a quick health tip';
    btn.onclick = function () {
        triggerHealthReminder();
    };
    document.body.appendChild(btn);
}

function getRandomTip() {
    let index;
    do {
        index = Math.floor(Math.random() * HEALTH_TIPS.length);
    } while (index === lastTipIndex && HEALTH_TIPS.length > 1);
    lastTipIndex = index;
    return HEALTH_TIPS[index];
}

function triggerHealthReminder(customMessage) {
    const tip = getRandomTip();
    const messageBody = customMessage || tip.body;

    // 1. Send desktop notification if tab is hidden / browser supports it
    if ("Notification" in window && Notification.permission === "granted" && document.visibilityState === 'hidden') {
        try {
            new Notification(tip.title, {
                body: messageBody,
                icon: 'https://cdn-icons-png.flaticon.com/512/2966/2966327.png',
                tag: 'health-hub-reminder'
            });
        } catch (e) {
            console.log('Desktop notification error:', e);
        }
    }

    // 2. Always show stylish in-app toast notification
    showHealthToast(tip.title, messageBody, tip.icon, tip.color);
}

function sendBackgroundNotification() {
    const tip = getRandomTip();
    if ("Notification" in window && Notification.permission === "granted") {
        try {
            new Notification("❤️ HealthHub Pro Care Reminder", {
                body: tip.title + ": " + tip.body,
                tag: 'health-hub-background'
            });
        } catch (e) {}
    }
}

function showHealthToast(title, body, iconClass, iconColor) {
    const container = document.getElementById('health-reminder-container');
    if (!container) return;

    // Limit active toasts to 2
    if (container.children.length >= 2) {
        container.removeChild(container.firstChild);
    }

    const toast = document.createElement('div');
    toast.className = 'health-toast';
    toast.innerHTML = `
        <div class="toast-icon-badge" style="background:${iconColor || 'var(--primary-color)'};">
            <i class="fas ${iconClass || 'fa-heart'}"></i>
        </div>
        <div class="toast-content">
            <div class="toast-title">${title}</div>
            <div class="toast-body">${body}</div>
        </div>
        <button class="toast-close" onclick="dismissToast(this)" title="Dismiss">&times;</button>
    `;

    container.appendChild(toast);

    // Auto dismiss toast after 8 seconds
    setTimeout(() => {
        dismissToast(toast.querySelector('.toast-close'));
    }, 8000);
}

function dismissToast(btn) {
    if (!btn) return;
    const toast = btn.closest('.health-toast');
    if (toast && !toast.classList.contains('toast-hiding')) {
        toast.classList.add('toast-hiding');
        setTimeout(() => {
            if (toast.parentNode) {
                toast.parentNode.removeChild(toast);
            }
        }, 300);
    }
}

