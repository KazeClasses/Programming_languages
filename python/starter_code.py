import random
import time

N = 100
random.seed(int(time.time()))

def insertion_sort(unsorted_list: list[int]) -> list[int]:
    # Implement your function here ...
    raise NotImplementedError

if __name__ == "__main__":
    input_list = list(range(N))
    random.shuffle(input_list)
    if input_list == sorted(input_list):
        print("Input list is already sorted")
    else:
        raise ValueError("Input list is not sorted")
