from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configure Chrome to ignore SSL errors
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-gpu')  # optional, avoids rendering bugs
options.add_argument('--log-level=3')  # reduce logging noise

# Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the fighter page
url = "https://www.tapology.com/fightcenter/fighters/76553-deiveson-alcantra-daico"
driver.get(url)

# Wait for the table to load
time.sleep(10)

# Try finding the table again
tables = driver.find_elements(By.CLASS_NAME, "fighterRecord")
print(f"Found {len(tables)} table(s).")

#driver.quit()

