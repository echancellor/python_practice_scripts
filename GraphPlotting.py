# importing the required module 
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [1,2,3] 
y1 = [2,4,1] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "line 1") 
  
# line 2 points 
x2 = [1,2,3] 
y2 = [4,1,3] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "line 2") 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Two lines on same graph!') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 

# x axis values 
x = [1,2,3,4,5,6] 
# corresponding y axis values 
y = [2,5,1,5,2,6] 
  
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 
  
# setting x and y axis range 
plt.ylim(1,8) 
plt.xlim(1,8) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('Some cool customizations!') 
  
# function to show the plot 
plt.show() 
