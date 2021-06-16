import time


def measure_performance(func):
    def wrapper():
        start_time = time.time()
        func()
        print("--- %s seconds ---" % (time.time() - start_time))
    return wrapper

@measure_performance
def for_loop_func():
    x = []
    for i in range(1,10):
        x.append(i)
    print(x)

@measure_performance
def list_comp_func():
    x = [i for i in range(1,10)]
    print(x)

for_loop_func()
list_comp_func()
