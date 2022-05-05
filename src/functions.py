import json

def standardize_input(data):
    # standardize user input to create a list with comma separated values
    selected_data = data.replace(':',',').replace(" ", "")
    splitted_data = selected_data.split(',')

    return splitted_data

def read_json(path):
    # Read json file
    file = open(path)

    return json.load(file)

def set_better_choice(hotel_name, price, rating):
    # Set best hotel option data
    value = {
        'name': hotel_name,
        'price': price,
        'rating': rating
    }

    return value

def get_price_type(user_input):
    # Check if the day is a weekday or if it is the weekend
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

def get_reward_program_type(user_input):
    return user_input[0]

def get_date_list(user_input):
    return user_input[1:]