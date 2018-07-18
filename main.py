import inbreast

fold = 2
valfold = 4



# the data, shuffled and split between train and test sets
trX, y_train, teX, y_test, teteX, y_test_test = inbreast.loaddataenhance(fold, 5, valfold=valfold)
