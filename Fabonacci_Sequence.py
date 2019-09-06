class Solution:
    def getFib(self, position):
        if position == 0:
            return 0
        elif position == 1:
            return 1
        first = 0
        second = 1
        num = first + second
        for i in range(2, position + 1):
            first = second
            second = num
            num = first + second
        return num


Sol = Solution()
test_cases = [0, 1, 2, 3, 4, 5]
for test_case in test_cases:
    print(Sol.getFib(test_case))


# Sol = Solution()
# print(Sol.getFib(0))


"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position-1) + get_fib(position-2)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
