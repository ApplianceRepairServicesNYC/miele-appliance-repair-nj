#!/usr/bin/env python3
"""
Sync .service CSS to match homepage exactly.
"""

import re
from pathlib import Path

BASE_DIR = Path('/Users/globalaffiliate/miele-appliance-repair-nj')

def fix_service_css(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False

    original = content

    # Fix .service box-shadow to match homepage (none)
    content = re.sub(
        r'(\.service \{[^}]*?)box-shadow: 0 5px 20px rgba\(0, 0, 0, 0\.08\);',
        r'\1box-shadow: none;',
        content
    )

    # Fix .service:hover box-shadow to match homepage (none)
    content = re.sub(
        r'(\.service:hover \{[^}]*?)box-shadow: 0 20px 40px rgba\(0, 0, 0, 0\.15\);',
        r'\1box-shadow: none;',
        content
    )

    # Fix .alt background to match homepage (#fff)
    content = re.sub(
        r'(\.alt \{[^}]*?)background: var\(--gray\);',
        r'\1background: #fff;',
        content
    )

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False


def main():
    html_files = list(BASE_DIR.rglob('index.html'))
    print(f"Found {len(html_files)} pages")

    count = 0
    for f in html_files:
        if 'assets' in str(f) or 'sitemap' in str(f):
            continue
        # Skip homepage
        if f == BASE_DIR / 'index.html':
            continue
        if fix_service_css(f):
            count += 1

    print(f"Synced service CSS on {count} pages")


if __name__ == "__main__":
    main()
