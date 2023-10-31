import requests
from bs4 import BeautifulSoup

# Function to scrape a web page and extract clean text
def scrape_web_page(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the text content
            text = soup.get_text()

            # Print the clean text to the console
            print(text)
        else:
            print("Failed to retrieve the web page. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

# Provide the URL of the web page you want to scrape
url = "https://www.waheediqbal.info/"  # Replace with the URL of the web page you want to scrape

# Call the function to scrape the web page and output clean text
scrape_web_page(url)

#umair's comment:

