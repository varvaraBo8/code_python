''' determines the number of factors the argument has
    args:
    number: an interger needed to dteremine the number of its factors

    returns
    an integer which is the toal amount of factors the argument has
    '''
def factor_count(number):

    counter = 0  
    for divider in range(1, number+1):
        if number % divider ==0:
            counter += 1

        return counter

upper_limit = int(input("Enter N: "))

for num in range(1, upper_limit+1):
    factor_size = factor_count(num)

    print(f"{num} has {factor_size} factors")
