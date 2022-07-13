import time
from datetime import datetime

def check_time(function):
    def inner(*args, **kwargs):
        start_time = datetime.now()
        l = function(*args, **kwargs)
        end_time = datetime.now()
        print("time taken===>", end_time - start_time)
        return l
    return inner

def timeit(func):
    def wrapper(*args, **kwargs):
        print("@@@@@@@@@@@@@@@@@@@")
        func(*args, **kwargs)
        print("%%%%%%%%%%%%%%%%%%%")

    return wrapper

@timeit
@check_time
def using_for_loop(n):
    """
    Function to insert even numbers between the range 0 to 10000 using for loop
    :return: l
    """
    print("=========using_for_loop=========")
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit
@check_time
def using_list_comp(n):
    """
    Function to insert even numbers between the range 0 to 10000 using list comp
    :return: l
    """
    print("=========using_list_comp=========")
    l = [i for i in range(n) if i % 2 == 0]
    return l

# print(using_for_loop())
# print(using_list_comp())
l1 = using_for_loop(1000000)
l2 = using_list_comp(1000000)

##########OUTPUT#####################

@@@@@@@@@@@@@@@@@@@
=========using_for_loop=========
time taken===> 0:00:00.041972
%%%%%%%%%%%%%%%%%%%
@@@@@@@@@@@@@@@@@@@
=========using_list_comp=========
time taken===> 0:00:00.032327
%%%%%%%%%%%%%%%%%%%

###############################
