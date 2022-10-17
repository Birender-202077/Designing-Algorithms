#taking input for maximu bag(sack) weight
bag_weight = int(input("\nEnter the weight of bag: "))

#taking weights of different objects from user
w = input("\nEnter the weight of objects: ")
w = w.split()
w = [int(x) for x in w]                                    # type conversion -- string to integer 
print("\nWeight List: ",w)

#taking user input values  of profit
p = input("\nEnter the value of profits: ")
p = p.split()
p = [int(y) for y in p]                                     # type conversion -- string to integer 
print("\nProfit List: ",p)

#combining the list of weights and profit to make a list containing pairs in tuple
list = [(w[i],p[i]) for i in range(len(w))]
print("\nWeight - Profit Pair: ",list)

#defining knapSack function
def knapSack(bag_weight,list):
    #sorting the list of tuples in reverse order w.r.t profit
    list=sorted(list, key = lambda i : i[1], reverse=True)
    print("\nSorted list: ",list)

    total_profit = 0

    for item in list:
        if item[0] <= bag_weight:
            total_profit=total_profit + item[1]
            bag_weight= bag_weight-item[0]
    return total_profit

# Test Case
if __name__ == '__main__':
    A=knapSack(bag_weight,list)                                 # function call
    print("\nMaximum Profit : ",A)
    print("\n")