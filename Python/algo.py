
# y = mx + b
def get_slope_intersection():
    y = int(input("Please enter a y coordinate: "))
    m = int(input("Please enter a slope: "))
    x = int(input("Please enter a x coordinate: "))
    
    res = (m * x) - y
    print()
    return "Slope Intersection Result: " + str(res)


def main():
    # TODO Create Binary search, Breadth first search, Depth First Search, Merge Sort, Quicksort
    algo = {
    "Slope Intersection": get_slope_intersection
    
    }
    
    # Display Algo list for user input
    for value in algo:
        print("List of Algorithms: ", value, end="\n")
    
    # Call func, display results to user
    user_algo = input("Type name of Algorithm to run: ")
    solution = algo[user_algo]()
    print(solution)
    
    

if __name__ == '__main__':
    main()