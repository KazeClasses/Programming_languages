import random
import time

N = 100
random.seed(int(time.time()))


def insertion_sort(unsorted_list: list[int]) -> list[int]:
    # Implement your function here ...
    raise NotImplementedError


# Do not change the following lines
if __name__ == "__main__":
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = insertion_sort(input_list)
    if output_list == sorted(output_list):
        print("List sorted")
    else:
        raise ValueError("Input list is not sorted")