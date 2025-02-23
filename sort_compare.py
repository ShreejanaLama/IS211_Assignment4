import time
import random

# Function to do insertion sort
# This method sorts the array by shifting elements one by one
# It keeps picking an element and placing it in the right position

def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # The current element to be placed correctly
        j = i - 1  # Start comparing with the previous elements
        while j >= 0 and key < arr[j]:  # Shift elements if they are greater than key
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place key at the correct position
    return time.time() - start_time  # Return the time taken

# Function to do shell sort
# This method is an optimized version of insertion sort that uses gaps

def shell_sort(arr):
    start_time = time.time()
    n = len(arr)
    gap = n // 2  # Start with a big gap and reduce it
    while gap > 0:
        for i in range(gap, n):  # Go through elements after the gap
            temp = arr[i]  # Pick an element
            j = i
            while j >= gap and arr[j - gap] > temp:  # Shift elements
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp  # Place element in correct position
        gap //= 2  # Reduce the gap size
    return time.time() - start_time  # Return the time taken

# Function to use Python's built-in sorting algorithm
# This function just calls the default sort function

def python_sort(arr):
    start_time = time.time()
    arr.sort()  # Python’s optimized sorting function
    return time.time() - start_time  # Return time taken

# Function to test sorting speeds
# It runs each sorting method on random lists and records their time
def benchmark_sort():
    sizes = [500, 1000, 5000]  # Different list sizes to test
    for size in sizes:
        total_time_insert = total_time_shell = total_time_python = 0
        for _ in range(100):  # Run 100 times to get an average
            arr = [random.randint(1, 10000) for _ in range(size)]  # Create random list
            
            arr_copy = arr[:]  # Copy the list for insertion sort
            total_time_insert += insertion_sort(arr_copy)
            
            arr_copy = arr[:]  # Copy the list for shell sort
            total_time_shell += shell_sort(arr_copy)
            
            arr_copy = arr[:]  # Copy the list for python sort
            total_time_python += python_sort(arr_copy)
        
        # Print out the average time taken for each sorting method
        print(f"Size {size}:")
        print(f"Insertion Sort took {total_time_insert / 100:.7f} seconds to run, on average")
        print(f"Shell Sort took {total_time_shell / 100:.7f} seconds to run, on average")
        print(f"Python Sort took {total_time_python / 100:.7f} seconds to run, on average")

# Main function that starts the benchmarking
# This function runs when the script is executed

def main():
    benchmark_sort()

# Run the program only if it's executed directly (not imported)
if __name__ == "__main__":
    main()
