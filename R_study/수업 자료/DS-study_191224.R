getwd()
set1 <- read.csv("data/실습용데이터모음/실습용데이터모음/set1.csv", header = T, stringsAsFactors = F)
str(set1)
set1$status <- as.factor(set1$status)

plot(set1) # 데이터가 선형적 관계가 없다느 것을 알 수 있다.

library(MASS)
density <- kde2d(set1$food, set1$book, n = 400)
image(density, xlab = "food", ylab = "book")

library(e1071)
m1 <- svm(status ~ food + book + cul + cloth + travel, type = "C-classification", data=set1)
m1

predict(m1, set1)
sum(set1$status != predict(m1, set1)) # 12이므로 아래꺼보다 정확도가 더 높다.


library(kernlab)
m2 <- ksvm(status ~ ., kernel = "rbfdot", data = set1)
m2

sum(set1$status != predict(m2, set1)) # 100 이므로 위에꺼가 정확도가 더 낮다.


