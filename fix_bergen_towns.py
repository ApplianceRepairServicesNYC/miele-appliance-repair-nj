#!/usr/bin/env python3
import os
import re

# Correct Bergen County towns list HTML
correct_towns = '''                          <ul id="townsList">
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/allendale/"><h3>Allendale</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/alpine/"><h3>Alpine</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/bergenfield/"><h3>Bergenfield</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/bogota/"><h3>Bogota</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/carlstadt/"><h3>Carlstadt</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/cliffside-park/"><h3>Cliffside Park</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/closter/"><h3>Closter</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/cresskill/"><h3>Cresskill</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/demarest/"><h3>Demarest</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/dumont/"><h3>Dumont</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/east-rutherford/"><h3>East Rutherford</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/edgewater/"><h3>Edgewater</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/elmwood-park/"><h3>Elmwood Park</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/emerson/"><h3>Emerson</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/englewood/"><h3>Englewood</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/englewood-cliffs/"><h3>Englewood Cliffs</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/fair-lawn/"><h3>Fair Lawn</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/fairview/"><h3>Fairview</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/fort-lee/"><h3>Fort Lee</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/franklin-lakes/"><h3>Franklin Lakes</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/garfield/"><h3>Garfield</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/glen-rock/"><h3>Glen Rock</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/hackensack/"><h3>Hackensack</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/harrington-park/"><h3>Harrington Park</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/hasbrouck-heights/"><h3>Hasbrouck Heights</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/haworth/"><h3>Haworth</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/hillsdale/"><h3>Hillsdale</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/ho-ho-kus/"><h3>Ho-Ho-Kus</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/leonia/"><h3>Leonia</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/little-ferry/"><h3>Little Ferry</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/lodi/"><h3>Lodi</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/lyndhurst/"><h3>Lyndhurst</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/mahwah/"><h3>Mahwah</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/maywood/"><h3>Maywood</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/midland-park/"><h3>Midland Park</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/montvale/"><h3>Montvale</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/moonachie/"><h3>Moonachie</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/new-milford/"><h3>New Milford</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/north-arlington/"><h3>North Arlington</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/northvale/"><h3>Northvale</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/norwood/"><h3>Norwood</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/oakland/"><h3>Oakland</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/old-tappan/"><h3>Old Tappan</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/oradell/"><h3>Oradell</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/palisades-park/"><h3>Palisades Park</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/paramus/"><h3>Paramus</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/park-ridge/"><h3>Park Ridge</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/ramsey/"><h3>Ramsey</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/ridgefield/"><h3>Ridgefield</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/ridgefield-park/"><h3>Ridgefield Park</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/ridgewood/"><h3>Ridgewood</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/river-edge/"><h3>River Edge</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/river-vale/"><h3>River Vale</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/rochelle-park/"><h3>Rochelle Park</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/rockleigh/"><h3>Rockleigh</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/rutherford/"><h3>Rutherford</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/saddle-brook/"><h3>Saddle Brook</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/saddle-river/"><h3>Saddle River</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/south-hackensack/"><h3>South Hackensack</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/teaneck/"><h3>Teaneck</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/tenafly/"><h3>Tenafly</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/teterboro/"><h3>Teterboro</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/upper-saddle-river/"><h3>Upper Saddle River</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/waldwick/"><h3>Waldwick</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/wallington/"><h3>Wallington</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/washington-township/"><h3>Washington Township</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/westwood/"><h3>Westwood</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/wood-ridge/"><h3>Wood-Ridge</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/woodcliff-lake/"><h3>Woodcliff Lake</h3></a></li>
                                <li><a href="https://mieleappliancerepairnj.com/bergen-county/wyckoff/"><h3>Wyckoff</h3></a></li>
                            </ul>'''

# Pattern to match the old towns list
pattern = r'<ul id="townsList">.*?</ul>'

# Fix ALL pages in bergen-county (including service pages)
import glob

fixed_count = 0

for index_file in glob.glob('bergen-county/**/index.html', recursive=True):
    with open(index_file, 'r') as f:
        content = f.read()

    # Replace the towns list
    new_content = re.sub(pattern, correct_towns, content, flags=re.DOTALL)

    if new_content != content:
        with open(index_file, 'w') as f:
            f.write(new_content)
        fixed_count += 1
        print(f"Fixed: {index_file}")

print(f"\nTotal files fixed: {fixed_count}")
