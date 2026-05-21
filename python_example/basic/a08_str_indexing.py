def main():
    print("안녕하세요")
    str_var = "안녕하세요"
    print(str_var[0])
    print(str_var[1])
    print(str_var[2])
    print(str_var[3])
    print(str_var[4])

    for c in str_var:
        print("for로 불러온 원소", c)
    
    str_var *= 3
    print(str_var[5:10]) # 5부터 9까지
    print(str_var[-3:]) # 뒤에서 3개
    print(str_var[5:10:2]) # 5부터 9까지 2칸씩 건너뛰면서
    print(str_var[-1::-1]) # 뒤에서부터 1칸씩 건너뛰면서 역순으로 출력z``
    print("str_var 길이", len(str_var))
    print("str_var 길이", str_var.__len__())
    
if __name__ == "__main__":
    main()