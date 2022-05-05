def standardize_data(data):
    # standardize the data format and split using comma
    selected_data = data.replace(':',',').replace(" ", "")
    splitted_data = selected_data.split(',')

    return splitted_data

def get_reward_program(user_input):
    return user_input[0]

def get_date_sequence(user_input):
    return user_input[1:]

def is_weekend(user_input):
    




