import requests
import os
from PIL import Image
from io import BytesIO

# Parametrlər
NUMBER_OF_REQUESTS = 100
OUTPUT_DIR = "spanish_photos"

# Nəticələri saxlamaq üçün qovluq yaradılır
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

spanish_users = []
photo_paths = []

for i in range(NUMBER_OF_REQUESTS):
    try:
        # Servisə sorğu göndər
        response = requests.get("https://randomuser.me/api/", timeout=5)
        response.raise_for_status()
        user_data = response.json()
        result = user_data.get("results", [{}])[0]

        # İspan istifadəçini seç
        if result.get("nat") == "ES":
            full_name = f"{result['name']['first']} {result['name']['last']}"
            photo_url = result['picture']['large']
            spanish_users.append((full_name, photo_url))

            # Fotoşəkli yükləyib yadda saxla
            photo_response = requests.get(photo_url, timeout=5)
            photo_response.raise_for_status()
            photo = Image.open(BytesIO(photo_response.content))

            photo_path = os.path.join(OUTPUT_DIR, f"{full_name.replace(' ', '_')}.jpg")
            photo.save(photo_path)
            photo_paths.append(photo_path)

    except requests.exceptions.RequestException as e:
        print(f"Request {i + 1}: Error occurred: {e}")

# Fotoşəkillərin sayı ilə istifadəçilərin sayı müqayisə edilir
print(f"İspaniyadan olan istifadəçilərin sayı: {len(spanish_users)}")
print(f"Yadda saxlanılan fotoşəkillərin sayı: {len(photo_paths)}")

if len(spanish_users) == len(photo_paths):
    print("Fotoşəkillərin sayı istifadəçi sayı ilə uyğundur.")
else:
    print("Xəta: Fotoşəkillərin sayı istifadəçi sayı ilə uyğun deyil!")

print("Vizual yoxlama üçün şəkillər saxlanıldı.")
print(f"Şəkillər qovluğu: {OUTPUT_DIR}")
