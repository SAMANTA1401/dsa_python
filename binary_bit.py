##1. generate All binary tree

# print(bin(4)) #100

def append_bits(x,L):
    print([x + element for element in L])
    return [x + element for element in L]

def generate_bit(n):

    if n==0: return []
    if n==1: return ['0','1']
    else:

    # if n==2: return ['00','01','10','11']
    # if n==3: return ['000','001','010','011', '100','101','110','111'] 

        return (append_bits('0',generate_bit(n-1)) + append_bits('1',generate_bit(n-1)))


print(generate_bit(3))
# The time complexity of the append_bits function is O(k), where k is the length of the input list.
# Since the generate_bit function makes two recursive calls, the time complexity is roughly doubled in each call.
# The recursion depth is n, and the time complexity at each level is O(2^k), where k is the current level.

# The function stores the results of each recursive call in memory.
# The space complexity at each level is O(2^k), where k is the current level.