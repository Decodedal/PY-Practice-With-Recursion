# Write code for algorithm 2 below
# Write a function that prints the natural numbers from 1 to n.

def natural_nums(target, num = 1):
    if target == num:
        return target
    else:
        print(num)
        return natural_nums(target, num + 1)

print(natural_nums(10))