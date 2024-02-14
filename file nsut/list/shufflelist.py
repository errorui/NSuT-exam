import random

def shuffle_and_print(input_list):
    shuffled_list = input_list[:]  # Create a copy of the input list to avoid modifying the original
    random.shuffle(shuffled_list)
    print("Shuffled list:", shuffled_list)

# Example usage:
my_list = [1, 2, 3, 4, 5]
shuffle_and_print(my_list)
my_string = "hello"
char_to_remove = 'l'
new_string = my_string.replace(char_to_remove, '')
print(new_string)