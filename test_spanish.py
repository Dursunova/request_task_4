import requests

# İspaniyadan olan istifadəçiləri saymaq üçün dəyişən
spanish_users = []

# 100 sorğu göndərin
for i in range(100):
    response = requests.get("https://randomuser.me/api/", timeout=5)
    
    if response.status_code == 200:  # Əgər sorğu uğurlu alınırsa
        data = response.json()
        user = data.get("results")[0]  # İlk nəticəni götür
        country = user.get("location", {}).get("country", "")
        name = user.get("name", {})
        
        # İspaniyadan olanları tapın
        if country.lower() == "spain":
            full_name = f"{name.get('first', '')} {name.get('last', '')}"
            spanish_users.append(full_name)

# Nəticələri göstər
print(f"İspaniyadan olan istifadəçilərin sayı: {len(spanish_users)}")
if spanish_users:
    print("Adlar:")
    for user in spanish_users:
        print(user)

# Log faylına yazmaq
with open("spanish_users_log.txt", "w", encoding="utf-8") as log_file:
    log_file.write(f"İspaniyadan olan istifadəçilərin sayı: {len(spanish_users)}\n")
    log_file.write("Adlar:\n")
    for user in spanish_users:
        log_file.write(user + "\n")
