# if it breaks at a low floor
# then its fast to find and the amount of drops is minimal
# imagine you run to different floors and drop the egg
# always drop on the first floor then middle=
# first run to the middle floor and drop the egg
# if it doesn't break then go up floors halfway between middle and top
# binary search makes the most sense
# which is O(log n) runtime complexity
# base 
def findfloortodropeggs(stories):
    egg = "safe"
    # this is the floor dropped
    f = 1
    # split the number in half
    broken = 0
    if broken == 1:
        return f

    # if the amount of drops is greater than or equal to the amount broken or when broken gets to one
     
    return f
    

findfloortodropeggs(10)