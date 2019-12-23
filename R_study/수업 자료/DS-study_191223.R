install.packages("caret")
library(caret)

idx <- createDataPartition (iris$Species, p=0.7, list=F)

iris_train <- iris[idx,]
iris_test <- iris[-idx,]
table(iris_train$Species)
table(iris_test$Species)

library(nnet)
model <- multinom(Species~., data=iris)
summary(model)
result <- predict(model, iris_test)
result

confusionMatrix(result, iris_test$Species)

idx <- createDataPartition(iris$Species, p=0.7, list = F)
iris_train[idx,]
iris_test[-idx,]

library(rpart)
model <- rpart(Species ~ . , data=iris_train)
result <- predict(model, iris_test, type="class")
result
head(result)
confusionMatrix(result, iris_test$Species)

install.packages("ramdomForest")
library(randomForest)
rdf <- randomForest(Species ~ . , data=iris_train, importance=T)

