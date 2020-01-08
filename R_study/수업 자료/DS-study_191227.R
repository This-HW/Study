library(ggplot2)

data(diamonds)
head(diamonds)
str(diamonds)

t<-sample(1:nrow(diamonds),1000)
test<-diamonds[t,]
dim(test)
str(test)
test


mydia<-test[c("price","carat","depth","table")]

result<-hclust(dist(mydia),method="ave") #거리값을 이용한 계층적 군집화

plot(result,hang=-1)

iris2 <- iris[,1:4] 
km.out.withness<-c()
km.out.between<-c()
for (i in 2:7){ #군집수를 k=2~7까지 변화시켜가며 클러스터링 시행
  set.seed(1)
  km.out<-kmeans(iris2, centers=i)
  km.out.withness[i-1]<-km.out$tot.withinss #군집 내 제곱합의 합
  km.out.between[i-1]<-km.out$betweenss #군집 간 제곱합의 합
  }
data.frame(km.out.withness, km.out.between)
plot(km.out.withness)
plot(km.out.between)
km.out$cluster
plot(iris2[,1:2], col=km.out$cluster, pch=ifelse(km.out$cluster==1, 16, ifelse(km.out$cluster==2, 17, 18)), cex=2);
points(km.out$centers, col=1:3, pch=16:18, cex=5)


library(arules)
library(arulesViz)
data(Groceries)
str(Groceries)
inspect(Groceries[1:10])
summary(Groceries)

sort(itemFrequency(Groceries,type="absolute"),decreasing = T)
itemFrequencyPlot(Groceries,topN=10,type="absolute")
itemFrequencyPlot(Groceries,topN=10,type="relative")

apriori(Groceries) #support=0.1, confidence=0.8
result_rules<-apriori(Groceries,
                      parameter=list(support=0.005,confidence=0.5,minlen=2))
result_rules
summary(result_rules) # {lhs} --> {rhs}
inspect(result_rules[1:10])
plot(result_rules, method="graph", control=list(type="items"))

plot(result_rules, method="grouped")





dsamp <- diamonds[sample(nrow(diamonds), 1000), ]
(d <- qplot(carat, price, data=dsamp, colour=clarity))

# Change scale label
d + scale_colour_brewer()
d + scale_colour_brewer("clarity")
d + scale_colour_brewer(expression(clarity[beta]))

# Select brewer palette to use, see ?scales::brewer_pal for more details
d + scale_colour_brewer(type="seq")
d + scale_colour_brewer(type="seq", palette=3)

d + scale_colour_brewer(palette="Blues")
d + scale_colour_brewer(palette="Set1")

# scale_fill_brewer works just the same as
# scale_colour_brewer but for fill colours
ggplot(diamonds, aes(x=price, fill=cut)) +
  geom_histogram(position="dodge", binwidth=1000) +
  scale_fill_brewer(palette = )

fake_data2 = data.frame(
  x = rnorm(140), 
  y = rnorm(140), 
  Label = rep(LETTERS[1:20], each = 7))






library(ggplot2)
theme_set(theme_bw())
fake_data = data.frame(
  x = rnorm(42), 
  y = rnorm(42), 
  Label = rep(LETTERS[1:7], each = 6))

p_too_light <- ggplot()+ geom_line(data=fake_data, aes(x, y, color=Label))+ 
  scale_colour_brewer(palette="Oranges")
p_too_light


library(RColorBrewer)
my_orange = brewer.pal(n = 9, "Oranges")[3:9] #there are 9, I exluded the two lighter hues

p_better <- ggplot()+ geom_line(data=fake_data, aes(x, y, color=Label))+ scale_colour_manual(values=my_orange)
p_better

orange_palette = colorRampPalette(c(my_orange[1], my_orange[4], my_orange[6]), space = "Lab")
my_orange2 = orange_palette(20)

p_20cat <- ggplot()+ geom_line(data=fake_data, aes(x, y, color=Label))+
  scale_colour_manual(values=my_orange2)
p_20cat


library(RColorBrewer)
my_palette = c(brewer.pal(5, "Set1")[c(1,3,4,5)], brewer.pal(5, "Pastel1")[c(2,5,1,3)])
#grid::grid.raster(my_palette, int=F)

scale_colour_discrete = function(...) scale_colour_manual(..., values = palette())

dsamp <- diamonds[sample(nrow(diamonds), 1000), ]
(p <- qplot(carat, price, data = dsamp, colour = clarity)) # default palette

palette(my_palette)
p # custom colors
