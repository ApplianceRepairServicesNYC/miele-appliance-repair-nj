#!/usr/bin/env python3
"""
Sync services section content from homepage to all subpages.
This ensures all pages have the same detailed expandable content.
"""

import re
from pathlib import Path

BASE_DIR = Path('/Users/globalaffiliate/miele-appliance-repair-nj')

# Read the services template from homepage
with open(BASE_DIR / 'services_template.html', 'r', encoding='utf-8') as f:
    SERVICES_TEMPLATE = f.read()

def get_location_from_h2(content):
    """Extract location name from the services h2 heading."""
    match = re.search(r'Authorized Miele Service Technicians Serving ([^<]+)</h2>', content)
    if match:
        return match.group(1).strip()
    return None

def sync_services(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False

    # Skip if no services-grid
    if 'class="services-grid"' not in content:
        return False

    # Get the location name from the current page
    location = get_location_from_h2(content)
    if not location or location == "New Jersey":
        return False  # Skip homepage

    # Create location-specific services section
    services_section = SERVICES_TEMPLATE.replace(
        'Authorized Miele Service Technicians Serving New Jersey',
        f'Authorized Miele Service Technicians Serving {location}'
    )

    # Find and replace the services section
    # Pattern: from <section class="alt"> to </section> before <section class="alt" id="contact">
    pattern = r'(<section class="alt">)\s*<div class="container">\s*<h2[^>]*>Authorized Miele Service Technicians[^<]*</h2>\s*<div class="services-grid">.*?</div>\s*</div>\s*</section>(\s*<section class="alt" id="contact">)'

    replacement = services_section + r'\2'

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
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
        if sync_services(f):
            count += 1
            if count % 500 == 0:
                print(f"  Processed {count} pages...")

    print(f"Synced services content on {count} pages")


if __name__ == "__main__":
    main()
