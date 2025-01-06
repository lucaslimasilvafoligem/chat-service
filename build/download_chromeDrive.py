import os
import requests
import zipfile

# Esse é aénas para distribuições linux, se não for o seu caso procure um tutorial
def baixar_chromedriver():
    url = "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip"
    response = requests.get(url)
    with open("chromedriver.zip", "wb") as f:
        f.write(response.content)
    with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    os.remove("chromedriver.zip")
    print("ChromeDriver baixado e extraído com sucesso.")

if __name__ == "__main__":
    baixar_chromedriver()
