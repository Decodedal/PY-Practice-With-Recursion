# Write code for algorithm 4 below

# Write a function that calculates the value of 'a' to the power of 'b'.

def a_to_power_b(a,b):
    if b == 1:
        return a 
    else:
        return a * a_to_power_b(a, b-1)    

print(a_to_power_b(2,4))