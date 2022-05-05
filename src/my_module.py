from src.functions import standardize_input, read_json
from src.functions import get_reward_program, get_date_list, get_day_price
from src.functions import set_better_choice

def get_cheapest_hotel(number):   #DO NOT change the function's name

    user_input = standardize_input(number)
    rewards_program = get_reward_program(user_input)
    date_list = get_date_list(user_input)

    hotels_data = read_json('src/hotels.json')

    better_choice = None
    for hotel in hotels_data['hotels'].keys():
        hotel_price = 0

        for day in date_list:
            date_price = get_day_price(day)
            hotel_price += hotels_data['hotels'][hotel][date_price][rewards_program]

        if better_choice == None:
            better_choice = set_better_choice(hotel, hotel_price, hotels_data['hotels'][hotel]['rating'])
        elif hotel_price < better_choice['price']:
            better_choice = set_better_choice(hotel, hotel_price, hotels_data['hotels'][hotel]['rating'])
        elif hotel_price == better_choice['price']:
            if hotels_data['hotels'][hotel]['rating'] > better_choice['rating']:
                better_choice = set_better_choice(hotel, hotel_price, hotels_data['hotels'][hotel]['rating'])

    cheapest_hotel = better_choice['name']
    return cheapest_hotel