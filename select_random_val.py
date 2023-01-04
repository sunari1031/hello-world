#-*- coding: utf-8 -*-

# select_random_val.py
# 랜덤하게 데이터 뽑기
# author: noma@neople.co.kr

# last modified date: 2019.06.12

# history
# 2019.06.12
# create this file

import random
import os
import sys

# 뽑히는 값 중복 가능
# 예를 들어, [1, 2, 3]에서 2개 뽑을 때 [2, 2] 가 뽑힐 수 있음
def duplicated_random(data_list, random_count):
    #val = random.choice(data_list)
    return [random.choice(data_list) for i in range(random_count)]

# 뽑히는 값 중복 불가
def unique_random(data_list, random_count):
    return random.sample(data_list, random_count)

# input 파일에서 리스트 획득
def get_data_list(file_input):
    data_list = []
    f = open(file_input)
    data_list = list(map(lambda s: s.strip(), f.readlines()))
    f.close()
    return data_list

if __name__ == "__main__":
    # python select_random_val.py input.txt 2
    # data_list = [1, 2, 3, 3, 5, 3, 7, 3, 9]
    # random_count = 2
    if len(sys.argv) != 3:
        print("Usage>> python select_random_val.py <input.txt> <val_count>")
        print("input.txt e.g. >>>>>>")
        print("1")
        print("2")
        print("3")
        print(">>>>>>>>>>>>>>>>>>>>>")
        sys.exit()

    file_input = sys.argv[1]
    if not os.path.exists(file_input):
        print("Dose not exist input file: %s" % file_input)
        sys.exit()

    try:
        random_count = int(sys.argv[2])
    except ValueError as e:
        print("<val_count> is not int")
        print("Usage>> python select_random_val.py <input.txt> <val_count>")
        sys.exit()
    
    data_list = get_data_list(file_input)
    #result_list = duplicated_random(data_list, random_count)
    result_list = unique_random(data_list, random_count)

    print(result_list)