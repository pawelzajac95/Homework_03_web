import time
from multiprocessing import Pool, cpu_count


def factorize(*numbers):
    factors_list = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        factors_list.append(factors)
    return factors_list


def factorize_s(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        factors_list = pool.map(factorize_s, numbers)
    return factors_list


if __name__ == '__main__':

    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    print("Czas wykonania:", end_time - start_time, "sekundy")

    start_time_async = time.time()
    a_async, b_async, c_async, d_async = factorize_parallel(
        128, 255, 99999, 10651060)
    end_time_async = time.time()
    print("Czas wykonania:", end_time_async - start_time_async, "sekundy")
