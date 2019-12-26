library(caret)

idx <- createDataPartition(iris$Species, p=0.7, list =F)
iris_train <- iris[idx,]
irirs_test <- iris[-idx,]
table(iris_train$Species)

