def main():
    print("hello world")
    print(__name__)

#import 를 당했을때 __main__이 아니라 hello가 출력된다.
if __name__ == "__main__":
    main()