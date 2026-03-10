#!/usr/bin/env python3
"""
Fix services-grid alignment to match homepage - items should be left-aligned.
"""

import re
from pathlib import Path

BASE_DIR = Path('/Users/globalaffiliate/miele-appliance-repair-nj')

def fix_grid(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False

    # Skip if already has justify-items in services-grid
    if 'services-grid' in content and 'justify-items: start' in content:
        return False

    # Skip if no services-grid
    if '.services-grid {' not in content:
        return False

    # Add justify-items: start to services-grid CSS
    old_css = '''.services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }'''

    new_css = '''.services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            justify-items: start;
        }'''

    if old_css in content:
        content = content.replace(old_css, new_css)
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
        if fix_grid(f):
            count += 1

    print(f"Fixed grid alignment on {count} pages")


if __name__ == "__main__":
    main()
