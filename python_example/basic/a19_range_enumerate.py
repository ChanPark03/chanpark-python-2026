def main():
    list1 = ["a", "b", "c", 1, 2, 3]
    list2 = ["에이", "비", "씨", "one", "two", "three"]

    for ele in list1:
        print(ele)  # list1의 원소를 하나씩 ele에 대입하면서 반복 파이썬 다운코드 

    for i in range(len(list1)): # 0부터 list1의 길이까지 1씩 증가하면서 반복 #len(list1) -> list1의 길이 반환  c스러운 코드 
        print(list1[i])
        print(list1[i], list2[i]) # list1과 list2의 원소를 하나씩 불러와서 출력)
        
    for i, ele in enumerate(list1): # list1의 원소를 하나씩 ele에 대입하면서 반복하면서 i에는 인덱스가 대입된다. 
        print(i, ele) # i는 인덱스 ele는 원소 
    for ele1, ele2 in zip(list1, list2): # list1과 list2의 원소를 하나씩 불러와서 ele1과 ele2에 대입하면서 반복 
        print(ele1, ele2) # ele1은 list1의 원소 ele2는 list2의 원소
        
if __name__ == "__main__":
    main()