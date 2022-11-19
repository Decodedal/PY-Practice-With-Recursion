# Write code for algorithm 1 below

# https://github.com/Decodedal/PY-Practice-With-Recursion.git

def count_down(num):
    if num == 0:
        return 0 
    else:
        print(num)
        return(count_down(num-1))    

print(count_down(5))