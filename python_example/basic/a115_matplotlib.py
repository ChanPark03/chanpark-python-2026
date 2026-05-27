import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path 

def main():
    csv_path = Path(r"/home/chan/chanpark-python-2026/python_example/basic/data")
    df = pd.read_csv(csv_path /"ta_20260527093833.csv", skipinitialspace=True)
    df.info()
    # plt.figure(figsize=(12,6))
    plt.plot(df['timestamp'], df['average'])
    plt.show()

if __name__ == "__main__":
    main()
