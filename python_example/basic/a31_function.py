def print_3_time():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
    
def print_n_time(value: str, n: int) -> str:  #타입힌트를 적어도 됨.
    """_summary_

    Args:
        value (str): _description_
        n (int): _description_

    Returns:
        str: _description_
    """
    
    for i in range(n):
        print(value)
    return "ok"

def main():
    print("첫번째 함수 호출")
    print_3_time()
    print("두번째 함수 호출")
    print_3_time()
    print("세번째 함수 호출")
    print_3_time()
    
    print_n_time("안녕하세요", 5)
    
if __name__ == "__main__":
    main()