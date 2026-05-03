import re

file_path = r'c:\Users\rendo\OneDrive\proyectos\arcade\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Simple replacements - just replace any card-emoji span with an img tag
replacements = {
    'doom.html': ('doom.jpg', 'DOOM'),
    'supermarioworld.html': ('super mario world.jpg', 'SUPER MARIO WORLD'),
    'donkeykongcountry.html': ('DonkeyKongCountry.jpg', 'DONKEY KONG COUNTRY'),
    'fzero.html': ('fzero.jpg', 'F-ZERO'),
    'ultimatemortalkombat3.html': ('ultimate mortal kombat.webp', 'ULTIMATE MORTAL KOMBAT 3'),
    'casper.html': ('casper.jpg', 'CASPER'),
    'frogger_snes.html': ('frogger.jpg', 'FROGGER'),
    'SuperMarioKart.html': ('super mario kart.jpg', 'SUPER MARIO KART'),
    'ZeldaLinkPast.html': ('zelda a link to the past.jpg', 'ZELDA: A LINK TO THE PAST'),
    'contra.html': ('contra.png', 'CONTRA'),
    'galaga_nes.html': ('galaga.jpg', 'GALAGA'),
    'excitebike_nes.html': ('excitebike.jpg', 'EXCITEBIKE'),
    'donkeykong_nes.html': ('donkey kong classics.webp', 'DONKEY KONG CLASSICS'),
    'pacman_nes.html': ('pac man.webp', 'PAC-MAN'),
    'trackfield_nes.html': ('track & field.jpg', 'TRACK & FIELD'),
    'marioparty.html': ('mario party.webp', 'MARIO PARTY'),
    'roadfighter_nes.html': ('roadfighter.jpg', 'ROAD FIGHTER'),
    'IceClimber.html': ('ice climber.webp', 'ICE CLIMBER'),
    'f1race_nes.html': ('f1 race.png', 'F-1 RACE'),
    'sonic.html': ('sonic the hedgehog.webp', 'SONIC THE HEDGEHOG'),
    'outrun.html': ('outrun.jpg', 'OUTRUN'),
    'tazmania.html': ('tazmania.jpg', 'TAZ-MANIA'),
    'streetsofrage3.html': ('streets of rage 3.jpg', 'STREETS OF RAGE 3'),
    'comixzone.html': ('comix zone.jpg', 'COMIX ZONE'),
    'aladdin.html': ('aladdin.webp', 'ALADDIN'),
    'tmnt.html': ('teenage mutant ninja turtles.webp', 'TEENAGE MUTANT NINJA TURTLES'),
    'quackshot.html': ('quackshot.webp', 'QUACKSHOT'),
    'pokemonemerald.html': ('pokemon esmeralda.webp', 'POKÉMON EMERALD'),
    'mariopinball_gba.html': ('mario pinball land.png', 'MARIO PINBALL LAND'),
    'mariogolf_gba.html': ('mario golf advance tour.webp', 'MARIO GOLF: ADVANCE TOUR'),
    'paperboy_gbc.html': ('paperboy.jpg', 'PAPERBOY'),
}

for html_file, (image_file, title) in replacements.items():
    # Replace <span class="card-emoji">anything</span> after this html file reference
    content = re.sub(
        f'(href="{re.escape(html_file)}">.*?<div class="card-art">)<span class="card-emoji">[^<]*</span>',
        f'\\1<img src="{image_file}" alt="{title}" class="card-emoji" style="width: 80px; height: 80px; object-fit: contain;">',
        content,
        flags=re.DOTALL
    )

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Todos los reemplazos completados exitosamente!')
