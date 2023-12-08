import re

FILE_PATH = 'Data/input1.txt'

def read_file(file):
    file = open(file, 'r')
    return file.readlines()

def get_sum(lines):
    sum=0
    for line in lines:
        nums_lst = re.findall(r'\d', line.strip())
        if len(nums_lst) > 0:
            sum +=(int(nums_lst[0])*10 + int(nums_lst[-1]))
    return sum

if __name__ == "__main__":

    content = read_file(FILE_PATH)
    sum = get_sum(content)

    print(sum)
    #55002