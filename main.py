import requests
import re
from bs4 import BeautifulSoup


def scrape_restaurants(url):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f'failed to get the webpage: {response.status_code}')
            return []
        
        soup = BeautifulSoup(response.text,'html.parser')
       
        restaurants = soup.find_all("div", class_= re.compile("^articleContent _articleContent"))

        for item in restaurants:
            title = item.find("h3", class_= re.compile("^_h3_cuogz"))
            print(title)
           # tags = item.find("ul", class_= re.compile("^_tagsList"))
           # cuisine = tags.find("li", class_=re.compile("^_tag_"))
        
    except Exception as e:
        print(f'An error has occured: {e}')
        return []

def main():
    url = "https://www.timeout.com/newyork/restaurants/100-best-new-york-restaurants"

    scrape_restaurants(url)

if __name__ == "__main__":
    main()