import requests
import re
from bs4 import BeautifulSoup
import random

def scrape_restaurants(url):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f'failed to get the webpage: {response.status_code}')
            return []
        
        soup = BeautifulSoup(response.text,'html.parser')
       
        title_tags = soup.find_all("h3", class_= re.compile("^_h3_cuogz")) #use regex to find h3 tag with class name beginning with _h3_cuogz
        restaurants = []
        for title_tag in title_tags: 
            # ignore titles without span tag since they could be ads
            if title_tag.span:
                title = title_tag.text.strip()
                article_tag = title_tag.find_parent("article") 
                tag_items = article_tag.find_all("li", class_="tag_item")
                tags =  [tag.text.strip() for tag in tag_items]
                link = title_tag.find_parent('a')
                url = link.get('href')      
                rating_tag = article_tag.find("div", class_=re.compile("^_rating_")) #use regex to find rating tag with class name beginning with _rating_
                rating = 'None'
                if rating_tag: 
                    rating = rating_tag.text
                restaurants.append((title, tags, url, rating))

        return restaurants
        
    except Exception as e:
        print(f'An error has occured: {e}')
        return []

def display_restaurant(title, tags, url, rating):
    
    print (title)
    for tag in tags:
        print (f'\t{tag}')
    print (f'\tRating: {rating}')
    print (f'\tURL: https://www.timeout.com{url}')


def main():
    url = "https://www.timeout.com/newyork/restaurants/100-best-new-york-restaurants"

    restaurants = scrape_restaurants(url)

    if restaurants:
        print("Top 50 Restaurants in New York City")
        for (title, tags, url, rating) in restaurants:
            display_restaurant(title, tags, url, rating)
            
        choice = ""

        while choice != "n":
            choice = input("Would you like a random restaurant recommendations?(y/n)")
            if choice == 'y':
                random_number = random.randint(0, 50)
                (title, tags, url, rating) = restaurants[random_number]
                display_restaurant(title, tags, url, rating)
            elif choice == 'n':
                print('Hope you found a restaurant you like!')
    else:
        print("an error occured: no restaurants found")

if __name__ == "__main__":
    main()