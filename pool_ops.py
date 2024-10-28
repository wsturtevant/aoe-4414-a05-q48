# pool_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in h_pool w_pool s p
#
# Arguments:
#   c_in: input channel count
#   h_in: input height count
#   w_in: input width count
#   h_pool: filter height count
#   w_pool: filter width count
#   s: stride of convolution filters
#   p: amount of padding on each of the four input map sides
#   
# Written by Wheat Sturtevant
# Other contributers: None

# import Python modules
import math # math module
import sys  # argv

# "constants"
w = 7.292115*10**-5

# initialize script arguments
c_in = float('nan')  
h_in = float('nan')  
w_in = float('nan')  
h_pool = float('nan')
w_pool = float('nan')
s = float('nan')
p = float('nan')

# parse script arguments 
if len(sys.argv) == 8:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    h_pool = float(sys.argv[4])
    w_pool = float(sys.argv[5])
    s = float(sys.argv[6])
    p = float(sys.argv[7])
else:
    print(\
        'python3 conv_ops.py c_in h_in w_in h_pool w_pool s p'\
            )
    exit()

# write script below this line
c_out = c_in
h_out = (h_in+2*p-h_pool)/s+1
w_out = (w_in+2*p-w_pool)/s+1 
adds = c_in*h_out*w_out*(h_pool*w_pool-1)
mults = 0
divs = c_in*h_out*w_out

print(int(c_out))   # channel count
print(int(h_out))   # height count
print(int(w_out))   # width count
print(int(adds))    # additions performed
print(int(mults))   # multiplications performed
print(int(divs))    # divisions performed

# Test Usage:
# python3 conv_ops.py c_in h_in w_in h_pool w_pool s p