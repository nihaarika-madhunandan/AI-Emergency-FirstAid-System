import re
t = open('static/hub.css', encoding='utf-8').read()
print('--- [data-theme=dark] .logo / navbar-brand rules ---')
for m in re.finditer(r'\[data-theme="dark"\][^{]*?(?:\.logo|\.navbar-brand)[^{]*\{[^}]*\}', t):
    s = ' '.join(m.group(0).split())
    if 'logo' in s or 'brand' in s:
        print(' ', s[:240])
print()
print('--- hub.css navbar backgrounds (dark) ---')
for m in re.finditer(r'\[data-theme="dark"\][^{]*?navbar[^{]*\{[^}]*\}', t):
    s = ' '.join(m.group(0).split())
    if 'background' in s or 'background:' in s:
        print(' ', s[:260])
