import json
import os

# Leer el archivo games.json
with open('src/data/games.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

games = data['games']
categories = {cat['id']: cat for cat in data['categories']}

# Crear carpeta de salida
os.makedirs('prompts', exist_ok=True)

prompts_data = []

for game in games:
    category = categories.get(game['category'], {})
    category_name = category.get('name', 'Desconocido')

    # Crear prompt basado en título, descripción y categoría
    prompt = f"""Game illustration for a church camp activity.

Title: {game['title']}
Description: {game['description']}
Category: {category_name}

Create a colorful, friendly cartoon-style illustration showing people playing this game.
The scene should be:
- Set outdoors in a grassy field or camp setting
- Show diverse group of happy people (teens and young adults)
- Everyone wearing casual modest summer clothing
- Bright, cheerful colors
- Clear visual of the main activity/materials mentioned
- Family-friendly, church-appropriate style
- No text or words in the image
- Wide angle shot showing the full activity

Style: Vibrant cartoon illustration, similar to community event flyers,
cheerful and energetic, good for church youth group"""

    prompts_data.append({
        'game_id': game['id'],
        'title': game['title'],
        'prompt': prompt.strip()
    })

    # Guardar prompt individual
    filename = f"prompts/{game['id']}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {game['title']}\n\n")
        f.write(f"Category: {category_name}\n\n")
        f.write(f"Description: {game['description']}\n\n")
        f.write(f"Prompt:\n{prompt.strip()}")

    print(f"✓ Prompt generado: {game['title']} ({game['id']})")

# Guardar resumen
with open('prompts/resumen.json', 'w', encoding='utf-8') as f:
    json.dump(prompts_data, f, indent=2, ensure_ascii=False)

print(f"\n✅ {len(games)} prompts generados en carpeta 'prompts/'")
print(f"📁 Resumen guardado en 'prompts/resumen.json'")
