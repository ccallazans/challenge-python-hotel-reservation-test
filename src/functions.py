import json

def standardize_input(data):
    # standardize the data format and split using comma
    selected_data = data.replace(':',',').replace(" ", "")
    splitted_data = selected_data.split(',')

    return splitted_data

def read_json(path):
    file = open(path)
    return json.load(file)

def set_better_choice(hotel_name, price, rating):
    value = {
        'name': hotel_name,
        'price': price,
        'rating': rating
    }
    return value

def get_day_price(user_input):
    select_index_range = user_input.find('(') + 1
    day = user_input[select_index_range:-1]

    dictionary = {
        "mon": 'weekday_price',
        "tues": 'weekday_price',
        "wed": 'weekday_price',
        "thur": 'weekday_price',
        "fri": 'weekday_price',
        
        "sat": 'weekend_price',
        "sun": 'weekend_price',
    }

    return dictionary[day]

def get_reward_program(user_input):
    return user_input[0]

def get_date_list(user_input):
    return user_input[1:]