'''
Created on Oct 3, 2012

@author: Joseph Lee
'''
from bayes_theor import BayesTheorem

def main():
    bayes = BayesTheorem()
    choice = option()
    print("---------------------------------------------")
    print()
    
    x = input("Please enter the number of categories: ")
    y = input("Please enter the number of subcategories: ")
    a = obtain_input(choice, int(x), int(y))
    
    if(choice == "2"):
        bayes.calc_by_prob(a)
    else:
        display(a)
        bayes.calc_by_value(a)
    
def obtain_input(choice, x, y):
    
    a = []
    b = []
    for i in range(x):
        category = input("Please enter category name: ")
        prob = 0
        if(choice == "2"):
            prob = input("Please enter the probability: ")
        a.append((category, float(prob), []))     
    for i in range(y):
        name = input("please enter the subcategory name: ")
        b.append(name)
    for i in range(x):
        for j in range(y):
            value = input(str.format("Enter the value of {0} in {1}: ", b[j], a[i][0]))
            a[i][2].append((b[j], float(value)))
    return a

def display(a):
    print()
    print("-----------------Value Tree------------------")
    for x in a:
        print(str.format("Category: {0}", x[0]))
        for y in x[2]:
            print(str.format("    subcategory: {0}, value: {1}", y[0], y[1]))
            
def option():
    print("---------------------------------------------")
    print("---------------Bayes Theorem-----------------")
    print("---------------------------------------------")
    print()
    print("1) Enter by values (Population problem)")
    print("2) Enter by percentage (Economic Growth Problem)")
    return input("Please choose an option: ")
    
if __name__ == '__main__':
    main()
