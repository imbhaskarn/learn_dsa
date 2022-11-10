
def containsDuplicate(nums) -> bool:
    arr_map = {}
    for elem in nums:
        if arr_map.get(elem) != None:
            return True
        else:
            arr_map[elem] = elem
    return False