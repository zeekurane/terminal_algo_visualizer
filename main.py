import time
CLEAR_LINE="\033[0J"
MOVE_UP="\033[1A"
MOVE_TO_LAST_SAVED="\033[u"
CLEAR_WINDOW="\033[2J"
SAVE_CURSOR_POSITION="\033[s"
algorithms=["linear_search", "binary_search_decreasing_order", "binary_search_increasing_order"]


def main():
    algo_choice=input(f"Type name of the algorithm to visualize it.\nAlgorithms are as follows: {algo()}\nName: ")
    match algo_choice:
        case "linear_search":
            linear_search()
        case "binary_search_increasing_order":
            binary_search(1)
        case "binary_search_decreasing_order":
            binary_search(-1)
        case _ :
            print("Error!")
        

def algo():
    output_str=""
    for name in algorithms:
        output_str+=name+" "
    return output_str


def binary_search(order):
    ip=tuple(map(int,input("Input the elements of list using space as separation between adjacent values: ").split()))
    target=int(input("Enter the target value: "))
    print(f"{CLEAR_WINDOW}Target: {"\033[32m"}{target}{"\033[0m"}")
    print(f"{SAVE_CURSOR_POSITION}")
    low=0
    high=len(ip)-1
    while low<=high:
        mid=(low+high)//2
        
        for i in range(len(ip)):
            if i==mid:
                print(f"{"\033[31m"}{ip[i]}{"\033[0m"} ", end="")
            elif i==low or i==high:
                print(f"{"\033[34m"}{ip[i]}{"\033[0m"} ", end="")
            else:
                print(f"{ip[i]} ", end="")
        print()
        time.sleep(5)
        
        if ip[mid]==target:
            break

        elif ip[mid]<target:
            if order==-1:
                high=mid-1
            else:
                low=mid+1
        elif ip[mid]>target:
            if order==-1:
                low=mid+1
            else:
                high=mid-1
        print(f"{MOVE_TO_LAST_SAVED}")
    if ip[mid]==target:
        print(f"{MOVE_TO_LAST_SAVED}")
        for i in range(len(ip)):
            if i==mid:
                print(f"{"\033[32m"}{ip[i]}{"\033[0m"} ", end="")
            else:
                print(f"{ip[i]} ", end="")
        print()
        time.sleep(1)
    


def linear_search():
    pointer=0
    ip=tuple(map(int,input("Input the elements of list using space as separation between adjacent values: ").split()))
    target=int(input("Enter the target value: "))
    print(f"{CLEAR_WINDOW}Target: {"\033[32m"}{target}{"\033[0m"}")
    print(f"{SAVE_CURSOR_POSITION}")
    for _ in range(len(ip)):
        for j in range(len(ip)):
            if j!=pointer:
                print(f"{ip[j]} ", end="")
            else:
                print(f"{"\033[31m"}{ip[j]}{"\033[0m"} ", end="")
        print()
        time.sleep(0.5)
        print(f"{MOVE_TO_LAST_SAVED}")
        if ip[pointer]==target:
            for k in range(len(ip)):
                if k!=pointer:
                    print(f"{ip[k]} ", end="")
                else:
                    print(f"{"\033[32m"}{ip[k]}{"\033[0m"} ", end="")
            print()
            time.sleep(1)
            break
        pointer+=1

if __name__=="__main__":
    main()