from matplotlib.pyplot import scatter,show,xlabel,ylabel,title
from numpy import linspace

y = lambda l,x: l*x*(1-x)                                          #logistic function
x=0.5                                                              #x can be anything as it will converge anyways
 
class bounds:
    "boundary object"
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.n = 3000
        if self.left<0 or self.right>4:
            raise Exception("Incorrect bounds: lambda has to be in [0;4]")
            
b=bounds(0,4)                                                      #set the graph's bounds and accuracy
 
def attractors(l):
    "returns all the attractors for a given lambda"
    d={}
    res=[y(l,x)]
    for i in range(1,100):
        res.append(y(l,res[i-1]))                                  #iteration process
    rounded = [round(res[i],3) for i in range(len(res)) if i>75]
    for j in rounded:
        d.update({j:1})                                            #only draw each attractor once: massively improving performances
    return [i for i in d.keys()]



lvals=linspace(b.left,b.right,b.n)

attractorlist = [attractors(l) for l in lvals]                     #grab all the attractors

for x,y in zip(lvals,attractorlist):                               #plot the graph
    scatter(
            [x]*len(y),
            y,
            color=[0,0,0],
            marker=None,
            s=[0.01]*len(y)
            )
title("Bifurcation diagram")
xlabel(r"$\lambda$")
ylabel(r"$x$",rotation="horizontal")
show()

    
