import datetime

def main():
    list_a = []
    list_b = list()
    list_c = [1, 2, 3, 4, 5, 6]
    
    print(list_a, list_b, list_c)
    print(type(list_a), type(list_b), type(list_c))
    ptime = datetime.datetime.now()
    list_d = [1, 2, 3.141592, "Park", ptime]
    print(list_d) # print(list_d[3]) -> Park 
    print(type(list_d))
    
    
    list_e = [[1,2,3], [4,5,6,], [7,8,9]]
if __name__ == "__main__":
    main()