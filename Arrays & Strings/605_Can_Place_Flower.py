def canPlaceFlower(self, flowerbed: list[int], n:int) -> bool:
    """
    Determines if `n` flowers can be planted in the `flowerbed` such that there is at least one empty space (0) between each flower.

    This function modifies the input `flowerbed` by adding a 0 to the beginning and end of the list. It then iterates over the
    `flowerbed`, checking if there are no flowers (sum of elements is 0) in the current position and the two adjacent positions.
    If there are no flowers, a flower is added to the current position and `n` is decremented. If `n` becomes less than or equal
    to 0 after planting a flower, the function returns True, indicating that it's possible to plant all `n` flowers.
    If the function iterates over the entire `flowerbed` without planting `n` flowers, it returns False.

    Args:
        flowerbed (List[int]): A list representing a flower bed, where 0 means an empty space and 1 means a flower.
        n (int): The number of flowers that need to be planted.

    Returns:
        bool: True if `n` flowers can be planted in the `flowerbed` with at least one empty space (0) between each flower,
              False otherwise.
              
    Time Complexity = O(n), where n is the length of the array
    Space Complexity = O(1)

    """
    
    flowerbed = [0] +  flowerbed + [0] 
    for i in range(1, len(flowerbed)- 1):
        if sum(flowerbed[i-1 : i+2] == 0):
            flowerbed[i] == 1
            n -=1
    return n<=0
    
    
    