#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def replace_emojis():
    file_path = r'c:\Users\rendo\OneDrive\proyectos\arcade\index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # All replacements - find by href and replace the emoji span after it
    replacements_dict = {
        'doom.html': 'doom.jpg',
        'supermarioworld.html': 'super mario world.jpg',
        'donkeykongcountry.html': 'DonkeyKongCountry.jpg',
        'fzero.html': 'fzero.jpg',
        'ultimatemortalkombat3.html': 'ultimate mortal kombat.webp',
        'casper.html': 'casper.jpg',
        'frogger_snes.html': 'frogger.jpg',
        'SuperMarioKart.html': 'super mario kart.jpg',
        'ZeldaLinkPast.html': 'zelda a link to the past.jpg',
        'contra.html': 'contra.png',
        'galaga_nes.html': 'galaga.jpg',
        'excitebike_nes.html': 'excitebike.jpg',
        'donkeykong_nes.html': 'donkey kong classics.webp',
        'pacman_nes.html': 'pac man.webp',
        'trackfield_nes.html': 'track & field.jpg',
        'marioparty.html': 'mario party.webp',
        'roadfighter_nes.html': 'roadfighter.jpg',
        'IceClimber.html': 'ice climber.webp',
        'f1race_nes.html': 'f1 race.png',
        'sonic.html': 'sonic the hedgehog.webp',
        'outrun.html': 'outrun.jpg',
        'tazmania.html': 'tazmania.jpg',
        'streetsofrage3.html': 'streets of rage 3.jpg',
        'comixzone.html': 'comix zone.jpg',
        'aladdin.html': 'aladdin.webp',
        'tmnt.html': 'teenage mutant ninja turtles.webp',
        'quackshot.html': 'quackshot.webp',
        'pokemonemerald.html': 'pokemon esmeralda.webp',
        'mariopinball_gba.html': 'mario pinball land.png',
        'mariogolf_gba.html': 'mario golf advance tour.webp',
        'paperboy_gbc.html': 'paperboy.jpg',
    }
    
    count = 0
    for html_file, img_file in replacements_dict.items():
        # Pattern to find the emoji span after this href
        # Match href="file.html">....<span class="card-emoji">ANYTHING</span>
        pattern = f'href="{re.escape(html_file)}">.*?<span class="card-emoji">[^<]*</span>'
        
        # Find matches
        matches = list(re.finditer(pattern, content, re.DOTALL))
        if matches:
            for match in matches:
                old = match.group()
                # Extract the title from the game info
                title = html_file.replace('.html', '').replace('_', ' ').upper()
                new = re.sub(
                    r'<span class="card-emoji">[^<]*</span>',
                    f'<img src="{img_file}" alt="{title}" class="card-emoji" style="width: 80px; height: 80px; object-fit: contain;">',
                    old
                )
                content = content.replace(old, new, 1)
                count += 1
                print(f"✓ {html_file} -> {img_file}")
        else:
            print(f"⚠ No match found for {html_file}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n¡Completados {count} reemplazos!")

if __name__ == '__main__':
    replace_emojis()

