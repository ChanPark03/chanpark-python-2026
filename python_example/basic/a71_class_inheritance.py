class Parent:
    def __init__(self, value):
        self.value = "테스트"
        self.value2 = value
        print("Parent 클래스의 __init__ 메소드가 호출 되었다.")
        
    def test(self):
        print("Parent 클래스의 test 메소드 입니다.")
        
    
    
def main():
    pObject = Parent("부모자료")
    pObject.test()


if __name__ == "__main__":
    main()