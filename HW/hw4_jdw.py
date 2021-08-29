### This homework is meant to give you a feel for how different algorithms can affect runtime
### For this homework, you will be required to implement two different sorting algorithms. Choose
### your own (there's a lot online to choose from).

### The only constraint is that the two must be in different complexity classes. Most likely
### You will need to find something that is O(n^2) and O(n*logn) but feel free to make up your
### own or find something exotic. You must implement the sorting algorithms yourself.

### Once you've verified that the sorts are working properly (using tests), you will need to
### run a simulation and graph the results. Specifically, produce a graph with the following
### characteristics:
    # - The vertical axis is some measure of time
    # - The horizontal axis is N (size of set to sort)
    # - You have one line for each sort algorithm, showing how time goes up with n
    # - Everything is labelled appropriately
### Try to pick an N such that the effect is visually noticable. It should not take a very large
### increase to make this possible.

### Bonus: Also graph quicksort. Note whether you are graphing average, best or worse-case runtime.
### To test average run times try generating an array full of random numbers and sorting it. Do this
### a number of times and take the mean runtime.

import random

small_test = [i for i in range(10)]
large_test = [i for i in range(100)]
mega_test = [i for i in range(10000)]
small_odds = [1, 3, 5, 7, 9]

random.shuffle(small_test)
random.shuffle(large_test)
random.shuffle(mega_test)
random.shuffle(small_odds)

### Stole this idea from https://codoholicconfessions.wordpress.com/2017/05/21/strangest-sorting-algorithms/
### I think it's pretty funny, even if it's just a lazy copy of the selection_sort from lecture
### Pretty simple: it sleeps for one second per iteration of time squared between each step of the function.
import time

def sleepy_sort(numbers):
    start = time.time()
    n = 0
    numbers = numbers.copy()
    answer = []
    while len(numbers) > 0:
        answer.append(min(numbers))
        del numbers[numbers.index(answer[-1])]
        time.sleep(n*n)
        n += 1
        naps = n
        print(f"...snoozing...this is my {naps}th nap...zzz...")
    end = time.time()
    runtime = f"Sleepy sort took {end - start} seconds to run."
    return answer, runtime

sleepy_sort(numbers = small_test)
# sleepy_sort(numbers = large_test)             # Don't run this
sleepy_sort(numbers = small_odds)

### Taken primarily from https://www.geeksforgeeks.org/add-elements-in-start-to-sort-the-array-variation-of-stalin-sort/
### The program executes the Stalin sort, which eliminates incorrectly-ordered elements from the list.
### It moves the 'purged' element to the beginning of the list
### Rinse and repeat until there are no incorrectly-ordered elements

### I made this one mostly because there's a certain fraternity at my alma mater that's done some *horrendous* stuff
### recently, and I'd like to use a more extreme version of the Stalin sort to get rid of them

def stalin_sort(numbers):
    start = time.time()
    answer = numbers.copy()
    n = 0
    while True:
        moves = 0
        for i in range(len(answer) - 1 - n):                # We're searching over the list
            if answer[i] > answer[i + 1]:                   # If the ith element is greater than the next one, it replaces that number
                answer.insert(moves, answer.pop(i + 1))     # with the moves iteration, and 'purges' the next one (this is what .pop() does)
                moves = + 1                                 # Then it adds 1 to the counter
        n += 1                                              # And we store the iteration of the for loop, moving on to the next element of the list
        if moves == 0:                                      # Once we hit the end and there are no moves left, we break
            break
    end = time.time()
    runtime = f"☭☭☭ The purge took {end - start} seconds to execute. ☭☭☭"
    return answer, runtime

stalin_sort(numbers = small_test)
stalin_sort(numbers = large_test)
#stalin_sort(numbers = mega_test)

### Graphing the sorting algorithms
### Sleepy sort is O(n^2), while Stalin sort is O(n) (I think??)
import matplotlib.pyplot as plt


n = list(range(1, 11))
O1 = [i for i in n]
O2n = [2 ** i for i in n]

plt.plot(n, O1, 'r-', label = "Stalin Sort")
plt.plot(n, O2n, 'p-', label = "Sleepy Sort")
plt.xlim(1, 10)
plt.ylim(1, 100)
plt.xlabel('N')
plt.ylabel('Big O')
plt.legend()
plt.show()


