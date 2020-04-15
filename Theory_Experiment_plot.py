#Created on July 7, 2016  15:10:33
#@author: Evan and Rob 
############################################################
#
# comments are typcially used to explain the following line of code
#
############################################################

# import the  library numpy  and rename it  np
import numpy as np
# import the library matplotlib   and rename it plot
import matplotlib.pyplot as plt
#name  the input file  with the data
import sys

fname = sys.argv[1]

# read in data - the file is assumed to be in csv format (comma separated variables). 
#Files need to be specified with a full path OR they have to be saved in the same folder 
#as the script
data = np.loadtxt(fname, delimiter=',',comments='#',usecols =(0,1,2), skiprows = 1)
# access the data columns and assign variables x and y
#generate  an array  x  which is the first  column  of  data.  Note the first column is 
#indexed as  zero.
x = data[:,0]
#generate  an array  y  which is the second  column  of  data  (index  1)
y = data[:,1]
#note the data is not copied during this process - x,y are 'pointing' to the same 
#memory as data
#define the uncertainty in y. 
sigmay= data[:,2]

#Define theory function parameters
Area = 1.7E-4
Atm = 100000
ngas = 0.000082
R = 8.314462618
T = 295.5
#define theory function for plotting
def function(Vrec, Area,Atm,ngas,R,T):
    return Area*Atm - Area*ngas*R*T*Vrec
#define the domain of f(x)  from  xmin to xmax  with npoints  
    
xmin= 1/1E-5
xmax= 1/2.8E-6
npoints=1000   
# define x as an array  of points  from 0, 10
xtheory= np.linspace(xmin,xmax,npoints)
#define y   as  f(x)
ytheory= function(xtheory,Area,Atm,ngas,R,T)




# plot the data
plt.errorbar(x, y,yerr=sigmay,marker='o',linestyle='', label = 'Experimental data')
plt.plot()
## marker='o' : use markers to indicate each data point (x_1,y_1),(x_2,y_2)
## linestyle= '' : no line is drawn to connect the data points
## linestyle= '-' : a line is drawn to connect the data points

# plot the theory function
plt.plot(xtheory,ytheory,linestyle="-",linewidth=2,color="orange",label = "Theoretical prediction")


# add axis labels
plt.tick_params(axis='both', which='major', labelsize=12)
plt.xlabel('Reciprocal Volume [1/m^3]', fontsize=14)
plt.ylabel('Average applied force [N]',fontsize = 14)
plt.title('Plot of experimental volume and force data \n with theoretical prediction', fontsize = 16)
plt.legend(fontsize = 12)
# this next command makes  sure the plot is shown. 
plt.show()
# ----- you can save a figure by right-clicking on the graph in the console
# ----- alternatively use: plt.savefig("NAMEOFFIGURE")