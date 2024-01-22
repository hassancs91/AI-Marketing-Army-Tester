from selenium import webdriver
from selenium_stealth import stealth
from urllib.parse import urlparse
from selenium.webdriver.chrome.options import Options
import time
import requests

client_id = "10086"

def upload_to_imgur(image_path):
    
    headers = {"Authorization": f"Client-ID {client_id}"}

    with open(image_path, "rb") as image:
        data = {"image": image.read()}
        response = requests.post("https://api.imgur.com/3/upload", headers=headers, files=data)
        
        if response.status_code == 200:
            # Extracting the public URL from the response
            return response.json()['data']['link']
        else:
            print(f"Error: {response.status_code}")
            print(response.json())
            return None




def capture_web_page_image(url, file_path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=chrome_options)

    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    
    driver.get(url)
    time.sleep(4)  # Wait for the page to load

    driver.save_screenshot(file_path)
    driver.quit()
    return file_path