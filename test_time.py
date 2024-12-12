import requests
import time

# Sorğu sayı
NUMBER_OF_REQUESTS = 100
SUCCESSFUL_REQUESTS = 0
FAILED_REQUESTS = 0

# Test funksiyası
def test_api_response_time():
    global SUCCESSFUL_REQUESTS, FAILED_REQUESTS
    
    with open("response_times_log.txt", "w") as log_file:
        log_file.write("Request #, Status Code, Response Time (s)\n")
        
        for i in range(NUMBER_OF_REQUESTS):
            start_time = time.time()
            
            try:
                response = requests.get("https://randomuser.me/api/")
                end_time = time.time()
                
                response_time = end_time - start_time
                status_code = response.status_code
                
                # Log məlumatını əlavə et
                log_file.write(f"{i + 1}, {status_code}, {response_time:.3f}\n")
                
                if status_code == 200 and response_time < 1:
                    print(f"Request {i + 1}: Success (Status: {status_code}, Time: {response_time:.3f}s)")
                    SUCCESSFUL_REQUESTS += 1
                else:
                    print(f"Request {i + 1}: Failed (Status: {status_code}, Time: {response_time:.3f}s)")
                    FAILED_REQUESTS += 1

            except Exception as e:
                end_time = time.time()
                response_time = end_time - start_time
                print(f"Request {i + 1}: Exception occurred - {e}")
                log_file.write(f"{i + 1}, ERROR, {response_time:.3f}\n")
                FAILED_REQUESTS += 1

# Testi işə sal
if __name__ == "__main__":
    print("Testing RandomUser API with 100 requests for response time...")
    test_api_response_time()
    
    print("\n--- Test Summary ---")
    print(f"Successful requests: {SUCCESSFUL_REQUESTS}")
    print(f"Failed requests: {FAILED_REQUESTS}")
    print("Detailed log written to 'response_times_log.txt'")
