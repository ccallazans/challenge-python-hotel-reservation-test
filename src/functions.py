import json

def standardize_input(data):
    """
    Standardize user input(data), leaving it in list format
    Parameter data: user input string
    Returns the list [<reward_program_type>,<day1>,<day2>,<day3>]
    """
    selected_data = data.replace(':',',').replace(" ", "")
    splitted_data = selected_data.split(',')

    return splitted_data

def read_json(path):
    """
    Read json file
    Parameter path: the json file path
    Returns a python dictionary
    """
    # Read json file
    file = open(path)

    return json.load(file)

def set_better_choice(hotel_name, price, rating):
    """
    Create a dictionary containing hotel information
    Parameter hotel_name: name of the hotel
              price: price of the hotel
              rating: rating of the hotel
    Returns a python dictionary
    """
    # Set best hotel option data
    value = {
        'name': hotel_name,
        'price': price,
        'rating': rating
    }

    return value

def get_price_type(user_input):
    """
    Shows whether the date is a weekday or weekend day
    Parameter user_input: reservation date string
    Returns string
    """
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
    """
    Shows whether the user is a regular or rewards user
    Parameter user_input: List -> [<reward_program_type>,<day1>,<day2>,<day3>]
    Returns string
    """
    return user_input[0]

def get_date_type_count(user_input):
    """
    Counts how many days are weekdays or weekend days
    Parameter user_input: List -> [<reward_program_type>,<day1>,<day2>,<day3>]
    Returns dict
    """
    date_list = user_input[1:]

    price_type = []
    for day in date_list:
        price_type.append(get_price_type(day))

    days_count = {
        'weekday_price': price_type.count('weekday_price'),
        'weekend_price': price_type.count('weekend_price'),
    }

    return days_count