X = c(1, 2, 3)
y = c(1, 2.5, 3.5)

#slope of the best fit model
thetas =c(0.5, 1.0, 1.5)

cost <- function(X,y,theta){
    #inner <- 
    return((sum((theta-y)^2))/6)
}
for(i in X){
    print(cost(X,y,X[i]*thetas))
}
