from functions import standardize_data, get_reward_program, get_date_sequence

def get_cheapest_hotel(number):   #DO NOT change the function's name

    data = standardize_data(number)
    select_rewards_program = get_reward_program(data)
    select_date_sequence = get_date_sequence(data)

    


    cheapest_hotel = "cheapest_hotel_name"
    return cheapest_hotel

get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)")
