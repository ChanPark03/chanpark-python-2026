var_a = 10


def make_20(var_a_b):
    # global var_a
    var_a_b[0] = 20
    print(var_a_b)
    

def main():
    var_a = 10
    
    
    # global var_a
    wrapper_list = [var_a]
    make_20(wrapper_list) 
    var_a = wrapper_list[0]
    
    print(var_a) # 20이 출력됨. var_a는 make_20 함수에서 지역변수로 사용됨.

    #list 이름은 값이 아니라 메모리로 참조하는 것이다. 그래서 list는 mutable한 자료형이다.
    
    list_a = [1,2,3]
    list_b = [4,5,6, list_a]
    print(list_b)
    list_a[2] = 30
    print(list_b) # list_a의 값이 바뀌었기 때문에 list_b의 값도 바뀜. list는 mutable한 자료형이기 때문.
if __name__ == "__main__":
    main()