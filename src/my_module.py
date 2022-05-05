from src.functions import standardize_input, read_json
from src.functions import get_reward_program_type, get_date_list, get_price_type
from src.functions import set_better_choice

def get_cheapest_hotel(user_input):   #DO NOT change the function's name
    #Handle user input
    handled_user_input = standardize_input(user_input)

    #Get info about Regular/Rewards user and the sequence of dates 
    reward_program_type = get_reward_program_type(handled_user_input)
    date_list = get_date_list(handled_user_input)

    #Read 'hotels.json' data
    hotels_data = read_json('src/hotels.json')

    better_choice = None
    #Iterate through registered hotels on 'hotels.json'
    for hotel in hotels_data['hotels'].keys():
        hotel_price = 0
        #Iterate through user input sequence of dates
        for day in date_list:
            price_type = get_price_type(day)
            hotel_price += hotels_data['hotels'][hotel][price_type][reward_program_type]

        #Check if is the first iteration
        if better_choice == None: 
            better_choice = set_better_choice(hotel, hotel_price, hotels_data['hotels'][hotel]['rating'])
        #Check if current hotel price is lower than the 'better_option' price
        elif hotel_price < better_choice['price']: 
            better_choice = set_better_choice(hotel, hotel_price, hotels_data['hotels'][hotel]['rating'])
        #Check if current hotel price is equal to 'better_option' price
        elif hotel_price == better_choice['price']: 
            #Check if current hotel rating is greater than 'better_option'
            if hotels_data['hotels'][hotel]['rating'] > better_choice['rating']:
                better_choice = set_better_choice(hotel, hotel_price, hotels_data['hotels'][hotel]['rating'])

    cheapest_hotel = better_choice['name']
    return cheapest_hotel