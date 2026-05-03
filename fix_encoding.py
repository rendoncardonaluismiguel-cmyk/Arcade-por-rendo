from pathlib import Path
path = Path('index.html')
text = path.read_text(encoding='utf-8')
replacements = {
    'â€”': '—',
    'â˜…': '★',
    'â–º': '▶',
    'â—„': '◄',
    'ðŸŽ®': '🎮',
    'ðŸ“º': '🕹️',
    'ðŸ‘¾': '👥',
    'ðŸ•¹ï¸': '🕹️',
    'âš¡': '⚡',
    'Â·': '·',
    'Â©': '©',
    'COLECCIÃ“N': 'COLECCIÓN',
    'CLÃSICA': 'CLÁSICA',
    'ACCIÃ“N': 'ACCIÓN',
    'POKÃ‰MON': 'POKÉMON',
    'diseÃ±o': 'diseño',
    'secciÃ³n': 'sección',
    'â–¶ JUGAR': '▶ JUGAR',
    'â–¶': '▶',
}
for bad, good in replacements.items():
    if bad in text:
        print(f"Replacing {bad!r} -> {good!r}, count={text.count(bad)}")
        text = text.replace(bad, good)
path.write_text(text, encoding='utf-8')
print('Done')
