import re

FILE_PATH = 'Data/day_1_input.txt'

DIGIT_NUMBERS = [str(n) for n in range(0,10)]
SPELLED_NUMBERS = ["zero","one","two","three","four","five","six","seven","eight","nine"]
ALL_NUMBERS = DIGIT_NUMBERS+SPELLED_NUMBERS

def read_file(file):
    file = open(file, 'r')
    return file.readlines()

def find_first_digit(text):
    min_idx=len(text)
    min_val=''
    for num in ALL_NUMBERS:
        idx_found = text.find(num)
        if (idx_found != -1) and idx_found<=min_idx:
            min_idx=idx_found
            min_val=num
    return min_val

def find_last_digit(text):
    max_idx=-1
    max_val=''
    for num in ALL_NUMBERS:
        idx_found = text.rfind(num)
        if (idx_found != -1) and idx_found>=max_idx:
            max_idx=idx_found
            max_val=num
    return max_val

def text_to_int(text):
    if  text ==  '1' or text == 'one':
        return 1
    elif text ==  '2' or text == 'two':
        return 2
    elif text ==  '3' or text == 'three':
        return 3
    elif text ==  '4' or text == 'four':
        return 4
    elif text ==  '5' or text == 'five':
        return 5
    elif text ==  '6' or text == 'six':
        return 6
    elif text ==  '7' or text == 'seven':
        return 7
    elif text ==  '8' or text == 'eight':
        return 8
    elif text ==  '9' or text == 'nine':
        return 9
    elif text ==  '0' or text == 'zero':
        return 0

def get_sum(lines):
    sum=0
    for line in lines:
        sum +=(text_to_int(find_first_digit(line))*10 + text_to_int(find_last_digit(line)))
    return sum

if __name__ == "__main__":

    content = read_file(FILE_PATH)
    sum = get_sum(content)

    print(sum)
    #55093