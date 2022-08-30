# IMPORTs #
from time import sleep


# DEFs #
def maior(*nums):
    print("-=" * 25)
    print("Contando números...")
    for n in nums:
        print(f"{n}...", end="", flush=True)
        sleep(0.3)
    print("FIM")
    print(f"O maior número foi {max(nums)}")
maior(1, 2, 3, 4, 5)
maior(2, 5, 6, 7, 4, 6, 3)
maior(0, 55, 98, 100, 3, 7, 34, 545)
