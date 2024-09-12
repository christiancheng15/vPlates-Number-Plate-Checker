import cloudscraper
from datetime import datetime
import concurrent.futures
import random
import threading

class ProxyHandler:
    def __init__(self, filename: str = "proxies.txt"):
        self.proxies = self.load_proxies(filename)

    def load_proxies(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            proxies = [line.strip() for line in file]
        print(f"[INFO] Loaded {len(proxies)} proxies from {filename}.")
        return proxies
        
    def get_random_proxy(self) -> str:
        proxy = random.choice(self.proxies).split(":")
        return self.reformat_proxy(proxy)

    def reformat_proxy(self, proxy: list) -> str:
        return f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"
    
    def test_proxy(self, proxy: str) -> bool:
        proxies = {
            "http": proxy,
            "https": proxy
        }

        return scraper.get("https://vplates.com.au/", proxies=proxies).status_code == 200
    
    def get_working_proxy(self) -> str:
        while True:
            proxy = self.get_random_proxy()
            if self.test_proxy(proxy):
                return {
                    "http": proxy,
                    "https": proxy
                }
            
class Combinations:
    def __init__(self, filename: str = "combinations.txt"):
        self.combinations = self.load_combinations(filename)

    def load_combinations(self, filename: str) -> list:
        with open(filename, "r") as file:
            combinations = file.readlines()
        print(f"[INFO] Loaded {len(combinations)} combinations from {filename}.")
        return combinations

class SystemUtils:
    @staticmethod
    def get_epoch_now():
        return round(datetime.timestamp(datetime.now()))

def main(combination):
    try:
        proxies = proxyhandler.get_working_proxy()

        params = {
            'vehicleType': 'car',
            'combination': combination,
            '_': SystemUtils.get_epoch_now(),
        }

        response = scraper.get(f"https://vplates.com.au/vplatesapi/checkcombo", params=params, proxies=proxies, timeout=10).json()
        if response["success"] == True:
            with file_lock:
                with open("success.txt", "a") as file:
                    file.write(f"{combination}\n")
                print(f"[SUCCESS] {combination}")
    except Exception as e:
        print(f"[ERROR] {combination}: {e}")

if __name__ == "__main__":
    proxyhandler = ProxyHandler("proxies.txt")
    combinations = Combinations("combinations.txt")

    scraper = cloudscraper.create_scraper(delay=10)
    file_lock = threading.Lock()

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(main, combinations.combinations)
