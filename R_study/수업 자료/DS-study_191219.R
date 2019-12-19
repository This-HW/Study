library(party)
str(airquality)
summary(airquality)

air_ctree <- ctree(Temp~Solar.R+Wind+Ozone, data=airquality)
air_ctree
plot(air_ctree)


# install.packages("randomForest") 
library(randomForest) 
rf<-randomForest(Species ~ . , data=iris)
rf

rf2<-randomForest(iris[,1:4],iris[,5])
rf2

rf3<-randomForest(Species~.,data=iris, importance=TRUE) 
importance(rf3)
