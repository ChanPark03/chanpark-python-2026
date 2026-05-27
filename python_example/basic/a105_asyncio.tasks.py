import asyncio
import time

async def hello():
    print("hello world!")
    await asyncio.sleep(5.0)
    
async def main():
    print("main 함수 ")
    # await hello()
    t1 = asyncio.create_task(hello())
    t2 = asyncio.create_task(hello())
    t3 = asyncio.create_task(hello())
    print("main 함수 종료")
    await t1  # t1 join 
    await t2  # t2 join 
    await t3  # t3 join 
    
if __name__ == "__main__":
    asyncio.run(main())