#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime is Linearithmic = O(n log n)
This is because the input is a cube of itself and the variable is the square, which means it will need to run a number of  a*n times more per size of input increase. As the input size increases the time to complete will grow at a slightly faster rate. 


b) This is Polynomial = O(n^c) because there are nested loops.
    The inner loop is Logeratimic but because it is nested in a for loop it has to complete a number of n times. As n increases the space will grow at a faster rate.


c) This solution is Exponential. = O(c^n)
    As the input increases the recursive function has to call itself at a exponential rate to the size of the input.

## Exercise II

The building is n stories high
and a egg is broken at >= f
find the value of f
break as and drop as few eggs as possible

def findf(n)

# if it breaks at a low floor
# then its fast to find and the amount of drops is minimal
# but if it only breaks at the top floor the amount of drops is high
# imagine you run to different floors and drop the egg
# always drop on the first floor then middle=
# first run to the middle floor and drop the egg
# if it doesn't break then go up floors halfway between middle and top
# if it doesn't go down halfway 
# set f
# binary search makes the most sense
# which is O(log n) runtime complexity
# base case would be to always check the first floor
def findfloortodropeggs(stories):
    egg = "safe"
    # this is the floor dropped
    f = 1
    # split the number in half
    # drop at different floors until you find f
    broken = 0
    

    # if the amount of drops is greater than or equal to the amount broken or when broken gets to one
     
    return f
    

findfloortodropeggs(10)
