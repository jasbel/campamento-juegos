import os
import json
import time

# Leer prompts generados
with open('prompts/resumen.json', 'r', encoding='utf-8') as f:
    prompts_data = json.load(f)

# Verificar si hay API key
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("⚠️  No se encontró OPENAI_API_KEY en el entorno")
    print("📝 Para generar imágenes, necesitas:")
    print("   1. Instalar: pip install openai")
    print("   2. Configurar: export OPENAI_API_KEY='tu-key-aqui'")
    print("   3. Ejecutar de nuevo")
    exit(1)

print(f"✅ API Key encontrada, generando {len(prompts_data)} imágenes...")

from openai import OpenAI
client = OpenAI(api_key=api_key)

os.makedirs('public/images/juegos', exist_ok=True)

generated_count = 0
for item in prompts_data:
    game_id = item['game_id']
    title = item['title']
    prompt = item['prompt']

    try:
        print(f"🎨 Generando: {title}...")

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            response_format="url"
        )

        image_url = response.data[0].url
        print(f"   ✅ Imagen generada: {image_url}")

        # Descargar imagen
        import requests
        img_response = requests.get(image_url)
        filename = f"public/images/juegos/{game_id}.png"

        with open(filename, 'wb') as f:
            f.write(img_response.content)

        print(f"   💾 Guardada: {filename}")
        generated_count += 1

        # Pequeña pausa para no exceder rate limits
        time.sleep(1)

    except Exception as e:
        print(f"   ❌ Error generando {title}: {e}")

print(f"\n✅ {generated_count} imágenes generadas exitosamente!")
