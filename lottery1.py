import operator
import random

def get_lottery_num(temp_total_num, temp_lottery_num):
    pool = list()
    lottery_pool = list()
    
    for i in range(int(temp_total_num)):
        pool.append(i)
    
    random.shuffle(pool)
    
    for j in range(int(temp_lottery_num)):
        print("#{}:\t{}".format(j+1, pool[j]+1))
        lottery_pool.append(pool[j]+1)

    return lottery_pool







if __name__ == '__main__':
    
    while True:
        total_num = int(input("請輸入樂透母池最大數: "))
        lottery_num = int(input("請輸入樂透抽取數: "))
    
        print(get_lottery_num( total_num, lottery_num))

