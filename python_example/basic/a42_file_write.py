from pathlib import Path


def main():
    path = Path(r"C:\Users\cjs\Desktop\chanpark-python-2026\python_example\basic\data")
    # f = open(path + "\\text.txt", "w")
    # f.write("Hello Python Programming...!")
    # f.close()
    with open(path / "text.txt", "a") as f:
        f.write("hello!!!")

if __name__ == "__main__":
    main()