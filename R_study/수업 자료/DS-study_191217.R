# getwd()
drink <- read.csv("./data/실습용데이터모음/실습용데이터모음/drink.csv", header=T)
drink

str(drink)
library(class)
# glm은 로지스틱 회귀 함수이다.
m <- glm(지각여부 ~ 나이 + 결혼여부 + 자녀여부 + 체력 + 주량 + 직급 + 성별, family = binomial(link = logit), data = drink)
# m <- glm(지각여부 ~  . , family = binomial(link = logit), data = drink)  전체 변수를 다 넣을 때에는 . 을 찍어도 똑같다.
m # 이 결과값들은 결과 값이 될 확률분에 안 될 확률을 나타낸 것이다. (1에 가까울수록 의미가 없다.)
predict(m, drink, type = "response")
predict(m, drink, type = "response") >= 0.5
table(drink$지각여부, predict(m, drink, type = "response") >= 0.5)


library(aod) library(ggplot2) 
# view the first few rows of the data 
mydata <- read.csv("https://stats.idre.ucla.edu/stat/data/binary.csv") 
head(mydata) # 데 이 터 의 대 략 적 인 분 포 확 인 
summary(mydata) # 데 이 터 구 조 확 인 
str(mydata) # 변 수 별 표 준 편 차 확 인 
sapply(mydata, sd) # contingency table : xtabs(~ x + y, data) 
xtabs(~admit+rank, data =mydata)

mydata$rank <-factor(mydata$rank) 
mylogit <- glm(admit ~ gre + gpa + rank, data = mydata, family = "binomial") 
summary(mylogit)

