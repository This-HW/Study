library(rpart)

#CART
help(rpart)
m <- rpart(Species~., data = iris)
m
plot(m, margin=.2, compress = T)
text(m, cex = 1.5)
summary(m)
print(m)


