import requests
import urllib3
from bs4 import BeautifulSoup
def check_product_Availability():
    url = input("Please provide URL:")
    urllib3.disable_warnings()
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    availability_element = soup.find('span', {'class': 'a-size-medium a-color-success'})
    if availability_element:
        availability = availability_element.text.strip()
        print(f"Product Availability is: {availability}")
    else:
        print('Not available')
check_product_Availability()











