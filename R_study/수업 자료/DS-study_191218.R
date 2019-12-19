library(rpart)
# library(rpart.plot)

#CART
help(rpart)
m <- rpart(Species~., data = iris)
m
plot(m, margin=.2, compress = T)
text(m, cex = 1.5)
summary(m)
# library(rpart.plot)
# prp(m,type=4,extra=2,digits=3)

# install.packages("party")
library(party)

m2<-ctree(Species~.,data=iris)
m2
plot(m2)
levels(iris$Species)
