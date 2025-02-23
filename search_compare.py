import time
import random

# Function to perform sequential search
def sequential_search(arr, target):
    start_time = time.time()  # Start timer
    for i in range(len(arr)):
        if arr[i] == target:  # If target is found
            return True, time.time() - start_time  # Return True and time taken
    return False, time.time() - start_time  # Return False if not found

# Function to perform ordered sequential search (list is sorted first)
def ordered_sequential_search(arr, target):
    start_time = time.time()  # Start timer
    arr.sort()  # Sorting the list first
    for i in range(len(arr)):
        if arr[i] == target:  # If target is found
            return True, time.time() - start_time  # Return True and time taken
        elif arr[i] > target:  # Stop searching if current element is greater than target
            return False, time.time() - start_time
    return False, time.time() - start_time  # Return False if not found

# Function to perform iterative binary search
def binary_search_iterative(arr, target):
    start_time = time.time()  # Start timer
    arr.sort()  # Sorting the list first (needed for binary search)
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2  # Find middle index
        if arr[mid] == target:
            return True, time.time() - start_time  # Return True if target found
        elif arr[mid] < target:
            low = mid + 1  # Move right if target is greater
        else:
            high = mid - 1  # Move left if target is smaller
    return False, time.time() - start_time  # Return False if not found

# Function to perform recursive binary search
def binary_search_recursive(arr, target, low=0, high=None, start_time=None):
    if start_time is None:
        start_time = time.time()  # Start timer only on first call
        arr.sort()  # Sorting the list first (needed for binary search)
    if high is None:
        high = len(arr) - 1  # Set high to last index on first call
    if low > high:
        return False, time.time() - start_time  # Return False if not found
    mid = (low + high) // 2  # Find middle index
    if arr[mid] == target:
        return True, time.time() - start_time  # Return True if target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, start_time)  # Search right half
    else:
        return binary_search_recursive(arr, target, low, mid - 1, start_time)  # Search left half

# Function to benchmark the search algorithms
def benchmark_search():
    sizes = [500, 1000, 5000]  # Different list sizes
    target = 99999999  # Target number that does not exist in the list
    for size in sizes:
        total_time_seq = total_time_ord_seq = total_time_bin_iter = total_time_bin_rec = 0
        for _ in range(100):  # Run 100 times to get average time
            arr = [random.randint(1, 10000) for _ in range(size)]  # Generate random list
            _, t = sequential_search(arr, target)  # Run sequential search
            total_time_seq += t
            _, t = ordered_sequential_search(arr, target)  # Run ordered sequential search
            total_time_ord_seq += t
            _, t = binary_search_iterative(arr, target)  # Run iterative binary search
            total_time_bin_iter += t
            _, t = binary_search_recursive(arr, target)  # Run recursive binary search
            total_time_bin_rec += t
        
        # Print average run time for each search method
        print(f"Size {size}:")
        print(f"Sequential Search took {total_time_seq / 100:.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {total_time_ord_seq / 100:.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {total_time_bin_iter / 100:.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {total_time_bin_rec / 100:.7f} seconds to run, on average")

# Main function to start benchmarking
def main():
    benchmark_search()

# Run the program if executed directly
if __name__ == "__main__":
    main()
