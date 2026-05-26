import sys
from pathlib import Path

def main():
    path = Path(r"C:\Users\cjs\Desktop\chanpark-python-2026\python_example\basic\data")
    with open(path / "text.txt", "r") as f:
        # data = f.readlines()
        #print(data)
        #for str in data:
        #print(str.strip()
        #   print(str)
        # data = f.read()
        # print(data)
        
        #파일이 굉장히 클때 사용.
        while data := f.readline():
            print(data)
        
    print(sys.stdin.fileno())
    print(sys.stdout.fileno())
    print(sys.stderr.fileno())
    print("error message", file=sys.stderr)
    with open(path / "text.txt", "a", encoding="utf-8")as f:
        print("이것은 프린트로 파일을 쓴 데이터이다.", file=f)

if __name__ == "__main__":
    main()