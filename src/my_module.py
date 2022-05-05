from src.functions import standardize_input, read_json
from src.functions import get_reward_program_type, get_date_type_count
from src.functions import set_better_choice

def get_cheapest_hotel(user_input):   #DO NOT change the function's name

    handled_user_input = standardize_input(user_input)
    reward_program_type = get_reward_program_type(handled_user_input)
    date_type_count = get_date_type_count(handled_user_input)

    hotels_data = read_json('src/hotels.json')
    hotels_data = hotels_data['hotels']

    better_choice = None
    #Iterate through registered hotels on 'hotels.json'
    for hotel in hotels_data.keys():
        weekday_price = hotels_data[hotel]['weekday_price'][reward_program_type] * date_type_count['weekday_price']
        weekend_price = hotels_data[hotel]['weekend_price'][reward_program_type] * date_type_count['weekend_price']
        hotel_price = weekday_price + weekend_price

        #Check if is the first iteration
        if better_choice == None: 
            better_choice = set_better_choice(hotel, hotel_price, hotels_data[hotel]['rating'])
        #Check if current hotel price is lower than the 'better_option' price
        elif hotel_price < better_choice['price']: 
            better_choice = set_better_choice(hotel, hotel_price, hotels_data[hotel]['rating'])
        #Check if current hotel price is equal to 'better_option' price
        elif hotel_price == better_choice['price']: 
            #Check if current hotel rating is greater than 'better_option'
            if hotels_data[hotel]['rating'] > better_choice['rating']:
                better_choice = set_better_choice(hotel, hotel_price, hotels_data[hotel]['rating'])

    cheapest_hotel = better_choice['name']
    return cheapest_hotel