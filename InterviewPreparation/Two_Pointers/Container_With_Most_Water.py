'''
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
'''

def mostWater(height):
    water=0
    l,r=0,len(heights)-1
    
    while l<r:
        w=r-l
        h=min(height[l],height[r])
        area=w*h
        if area>water: water=area
        
        if height[l]>height[r]:
            r-=1
        else:
            l+=1
    
    return water


heights=[0,1,0,2,1,0,1,3,2,1,2,1]
print(mostWater(heights))