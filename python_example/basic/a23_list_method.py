import datetime

def main():
    list_a = [1,2,3]
    list_b = [4,5,6]
    print(list_a + list_b) # list_a와 list_b를 합쳐서 새로운 리스트를 만듦. list_a와 list_b는 변하지 않음.
    list_a.__add__(list_b) # list_a와 list_b를 합쳐서 새로운 리스트를 만듦. list_a와 list_b는 변하지 않음.
    print(list_a := list_a + list_b) # list_a와 list_b를 합쳐서 새로운 리스트를 만듦. list_a는 변함. list_b는 변하지 않음.
    
    list_a.extend(list_b) # list_a에 list_b를 추가함. list_a는 변함. list_b는 변하지 않음.
    print(list_a)
    
    print(list_a * 4) # list_a를 4번 반복해서 새로운 리스트를 만듦. list_a는 변하지 않음.
    print(list_a.__mul__(4)) # list_a를 4번 반복해서 새로운 리스트를 만듦. list_a는 변하지 않음.
    
    list_b.append("추가 원소")
    print(list_b) # list_b에 "추가 원소"가 추가됨. list_a는 변하지 않음.
    
    list_b.insert(3, 7) # list_b의 3번째 인덱스에 7을 추가함. list_b는 변함. list_a는 변하지 않음.
    print(list_b)
    
    print(list_b.pop()) 
    print(list_b) # list_b의 마지막 원소가 제거됨. list_a는 변하지 않음.
    print(list_b.pop(0))
    print(list_b) # list_b의 0번째 인덱스의 원소가 제거됨. list_a는 변하지 않음.
    list_b.remove(5) # list_b에서 5를 제거함. list_b는 변함. 
    print(list_b) # list_b에서 5가 제거됨. list_a는 변하지 않음.
    print(list_b.index(7)) # list_b에서 7의 인덱스를 반환함. list_b는 변하지 않음. list_a는 변하지 않음.
    
    list_b = ['a', 'b', 'c', 'd', 'e']
    list_e = [*str("dsadhadsajdhsajdhasjdhasjd")] # list_e에 문자열을 리스트로 변환해서 저장함.
    print(list_b.index('e')) # list_b에서 'e'의 인덱스를 반환함. 
    print(list_e)
    print(list_e.__len__()) # list_e의 길이를 반환함.
    print(len(list_e)) # list_e의 길이를 반환함. 이렇게 사용하는게 일반적. 위랑 같은 결과 반환 .
    
    print("k" in list_e)
    print("d" in list_e)
    
    #del 메모리삭제
    del list_e[4]
    
    # del 사용자 정의 객체 삭제
    print(list_e)  
    ptime = datetime.datetime.now()
    list_e.append(ptime)
    print(list_e[16])
    del list_e[16]
    print (list_e)
    print(ptime) 
if __name__ == "__main__":
    main()