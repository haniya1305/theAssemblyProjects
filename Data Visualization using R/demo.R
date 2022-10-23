# R can be used as a calculator
# It can be directly implemented on the console or on a R script for complex operations
# Demo for mathematical functions such as +,-,*,/,^, prompt symbol (>)
# : is used to specify a range, both limits included
# There are built-in constants such as pi => (1:5)+pi
# We can extract integer and remainder of modular arithmetic- %% for remainder and %/% for integer part
# The workspace is known as the global environment that can be used to store the results of calculations,
# and other objects (variables).

# interest <- 10.45^2 (we can also use =, but <- is preferred as we are requesting an action rather than 
# stating a relation)
# Keep in mind that R is case sensitive.
x <- 1:10 # is different from X
# R provides us with built-in functions such as mean()
MEAN <- mean
MEAN(x) 
# We have created a user-defined function which calls the built-in function

# List all the objects in the workspace using objects() or ls() function
ls()
objects()

# Remember that if we quit our R session without saving the workspace, then these objects will disappear. 
# If we save the workspace, then the workspace will be restored at our next R session.

# Random number generator => runif() function
a <- runif(4,min=1, max=4)
# If min/max isn't specified, by default it will always be 0-1

# Vectors in R => numeric vectors is a list of numbers
# c() function is used to join values into a vector
y <- c(10,2,4,7,4,1)
xy <- c(x,y)  #vectors can be internally joined too
# Extracting elements from vectors
xy[1]
xy[c(2,15,11,9)]
xy[2:3]
xy[-c(2:8)]
# Patterned vectors - 
seq(1,9, by = 2) #if by is not specified, by default 1 will be used
rep(3,5)
rep(seq(2,10,by=2),2)
rep(c(1,3), each = 4)
rep(c(1,2),c(4,9))
rep(1:5, rep(2,5))
# Random Patterned vectors - 
dice <- sample(1:6, 5, replace = FALSE)
# die is rolled 10 times to give random values
coin <- sample(1:2, 10, replace = TRUE)
# coin is tossed 10 times to give random values
# Character vectors - (ensure that all elements of a vector must be of the same type)
colors <- c("red","blue","green")
substr(colors,1,2)  # to take substring, use substr(x, start, stop)
paste(colors, "flowers")  # to concatenate
paste("I like", colors, collapse = ", ") # used to make all into one string

# Factors -
grp <- c("control", "treatment", "control", "treatment")
grp <- factor(grp)
as.integer(grp)
levels(grp)
levels(grp)[as.integer(grp)]
levels(grp)[1] <- "placebo"

# Matrices and arrays
m <- matrix(1:6, nrow=2, ncol=3)
m[1,2]  #access element of a matrix using indices
m[4]    #access element of a array using indices 
m[1,]   #access row of a matrix using indices 
m[,2]   #access column of a matrix using indices
arr <- array(1:24)

# Use ?q or help(q) to access the help facility for a function q

values <- NULL #keeps the variable empty
values[seq(2,10,2)] <- seq(2,10,2)
is.na(values) #detects if there are null values

# Elementary built-in Functions
var(x)
summary(x)
length(x)
min(x)
max(x)
range(x)
IQR(x)
m <- 1:5 
n <- 7:3 
m
n
pmin(m,n)   #pairwise minima
pmax(m,n)   #pairwise maxima

# Logical Operations -
val1 <- c(TRUE,FALSE,FALSE,TRUE)
val2 <- c(13,7,9,3)
val2[val1]
sum(val1) #number of true statements
!val1     #negation of val1
# && and || are similar to & and |; they are not vectorized: only one calculation is done

# Relational Operators - 
vectors_elements <- c(2,4,8,6,14,3,85,9)
vectors_elements > 5

# Data Frames and Lists - 
# data sets are stored in R as data frames, and we get some with R, such as women. 
summary(women)
nrow(women)
ncol(women)
dim(women)
str(women)
# extract from data frames similar to matrices
#columns can be accessed using $ operator
women$height[women$weight>150]
#with() function allows us to access columns of data frame without using $
with(women, weight/height)
#constructing data frames: 
mn <- data.frame(m,n)

# Plots
# Users of statistical computing need to produce graphs of their data and the results of their computations
summary(WorldPhones)
WorldPhones51 = WorldPhones[1,]
barplot(WorldPhones51)
barplot(WorldPhones51, cex.names = 0.75, cex.axis = 0.75,main = "Numbers of Telephones in 1951")
dotchart(WorldPhones51, xlab = "Numbers of Phones (’000s)")
groupsizes <- c(18, 30, 32, 10, 10)
labels <- c("A", "B", "C", "D", "F")
pie(groupsizes, labels,col = c("grey40", "white", "grey", "black", "grey90"))
summary(iris)
boxplot(Sepal.Length~Species, data = iris, ylab = "Sepal length (cm)", main = "Iris measurements", boxwex = 0.5)

# Flow of Control
# for loop - Factorial Function
n <- 10
result <- 1
for (i in 1:n)
  result <- result * i
result
# while loop - Fibonacci Function
Fib1 <- 1
Fib2 <- 1
Fibonacci <- c(Fib1, Fib2)
while (Fib2 < 300) {
  Fibonacci <- c(Fibonacci, Fib2)
  oldFib2 <- Fib2
  Fib2 <- Fib1 + Fib2
  Fib1 <- oldFib2
}
# if statement
x <- 3 
if (x > 2) y <- 2 * x else y <- 3 * x

# replicate() function - evaluate the statements n times
replicate(5, 1:3)

# Packages
# In R, a package is a module containing functions, data, and documentation. 
# Base packages include base, stats, graphics; these contain things that everyone will use
# to load a package,
library(knitr)
# to see which packages sare loaded,
search()

# Question - Read from a csv file, create a new data frame object with only the Year, Province, and Population, create a lattice dotplot
setwd("/Users/HANIYA/R")
CanPop = read.csv("population.csv",stringsAsFactors = TRUE)
summary(CanPop)
head(CanPop)
CanPop = CanPop[,c(1,2,13)] #Columns that have the year, province and population is 1,2 and 13
head(CanPop)
names(CanPop) = c("Year", "Province","Pop") #Renaming the columns
head(CanPop)
library(lattice)
dotplot(Province~Pop|as.character(Year),data=CanPop)
