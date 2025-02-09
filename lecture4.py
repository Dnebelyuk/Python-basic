original_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

new_dict = {key: value for key, value in original_dict.items() if value >= 3}

print(new_dict)
