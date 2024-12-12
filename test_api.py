import requests

# Sorğu sayı
NUMBER_OF_REQUESTS = 100
SUCCESSFUL_RESPONSES = 0
FAILED_RESPONSES = 0

# Sorğu göndərmə funksiyası
def test_randomuser_api():
    global SUCCESSFUL_RESPONSES, FAILED_RESPONSES
    for i in range(NUMBER_OF_REQUESTS):
        try:
            response = requests.get("https://randomuser.me/api/")
            if response.status_code == 200:
                data = response.json()
                # Strukturun doğruluğunu yoxla
                if "results" in data and isinstance(data["results"], list):
                    print(f"Request {i+1}: Success")
                    SUCCESSFUL_RESPONSES += 1
                else:
                    print(f"Request {i+1}: Invalid structure")
                    FAILED_RESPONSES += 1
            else:
                print(f"Request {i+1}: Failed with status code {response.status_code}")
                FAILED_RESPONSES += 1
        except Exception as e:
            print(f"Request {i+1}: Exception occurred - {e}")
            FAILED_RESPONSES += 1

# Testi işə sal
if __name__ == "__main__":
    print("Testing RandomUser API with 100 requests...")
    test_randomuser_api()
    print("\n--- Test Summary ---")
    print(f"Successful responses: {SUCCESSFUL_RESPONSES}")
    print(f"Failed responses: {FAILED_RESPONSES}")
