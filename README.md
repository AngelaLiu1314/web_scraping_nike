# Restaurant Recommendation Program

## Website Used
The website used was Timeout Market's article: ["The 50 best restaurants in NYC right now"](https://www.timeout.com/newyork/restaurants/100-best-new-york-restaurants). This website was chosen because it provides comprehensive information about each restaurant, which we felt could be summarized into a shorter list. Additionally, when looking for a place to eat, users often don't know what type of restaurant they want, so having an option for a random recommendation helps users make a decision faster.

## Purpose
The purpose of this program is to:
- Summarize information about the top 50 restaurants in NYC.
- Provide an option to give a random recommendation to the user.

## Features
1. Summarizes the top 50 restaurants.
2. Provides information about:
   - Restaurant name
   - Type of cuisine
   - General location
   - Rating
   - A URL to Timeout's review of the location (provided all the information is available for that restaurant).
3. Allows users to ask for a random recommendation from the list until they find a restaurant they want to go to.

## Prerequisites
1. Install all libraries listed in the `requirements.txt` file using pip.

## Usage
- Run the program to receive the entire list of 50 restaurants.
- When asked if you want a random recommendation:
  - Type `y` to receive a random restaurant.
  - Type `n` to end the program.
