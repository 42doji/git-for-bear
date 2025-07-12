
def input_handler():
    try:
        inputs = input()
        splitted = inputs.split()
        casted = list(map(float, splitted))
    except ValueError:
        print("Error: Invalid arguments.")
    return casted 
    
    
def find_min(nums):
    _min = nums[0]
    for num in nums:
        if _min > num:
            _min = num;
    return _min

def find_max(nums):
    _max = nums[0]
    for num in nums:
        if _max < num:
            _max = num
    return _max

def main():
    inputs = input_handler()
    print(f"min: {find_min(inputs)}, max: {find_max(inputs)}")

if __name__ == "__main__":
    main()
