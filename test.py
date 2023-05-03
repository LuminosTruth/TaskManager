import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция '{func.__name__}' затратила {end_time - start_time:.2f} секунд на запуск")
        return result

    return wrapper


@time_it
def asd():
    a = 5
    b = 3
    sum = a + b
    print(sum)

asd()
