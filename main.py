from typing import Tuple, List

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    counter = 0
    for i in range(1, len(val_losses)):
        diff = val_losses[i-1] - val_losses[i]
        if diff < min_delta - 1e-10:
            counter += 1
            if counter == patience:
                return (i, i - patience)
        else:
            counter = 0
    return (len(val_losses) - 1, len(val_losses) - 1)

# print(early_stopping([0.9, 0.8, 0.79, 0.78, 0.77], 2, 0.1))

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        counter = 0
        for i in range(len(flowerbed)-2):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                counter += 1
                flowerbed[i] = 1
            elif i == len(flowerbed) - 2 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                counter += 1
                flowerbed[i+1] = 1
            elif flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                counter += 1
                flowerbed[i+1] = 1
        return counter == n
    
nums = [1,0,0,0,1,0,0]

print(canPlaceFlowers(nums, 2))