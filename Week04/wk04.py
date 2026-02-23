def count_characters(s):
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Iterate through each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_count[char] = 1
            
    return char_count  # Return the dictionary with character counts

def first_unique_character(s):
    char_count = count_characters(s)  # Get the character counts
    # Iterate through the string again to find the first unique character
    for i in range(len(s)):
        if char_count[s[i]] == 1:  # Check if the character count is 1
            return i  # Return the index of the first unique character
    return -1  # Return -1 if there is no unique character



def shuffle_array(nums, n):
    first_half = nums[:n]  # Get the first n elements (x1, x2, ..., xn)
    second_half = nums[n:]  # Get the next n elements (y1, y
    # Create an empty array to hold the shuffled result
    shuffled = [0] * (2 * n)
    
    # Fill the shuffled array with elements from the input array
    for i in range(n):
        shuffled.append(first_half[i])  # Add the first n elements (x1, x2, ..., xn)
        shuffled.append(second_half[i])  # Add the next n elements (y1, y2, ..., yn)
        
    return shuffled  # Return the shuffled array    





# Part A: Brute Force with a nested loop:
def two_sum_brute_force(nums, target):
    #Use a nested loop to check all pairs of numbers
    # Outer loop: i from 0 to len(numbers):
    for i in range(len(nums)):
        # Inner loop: j from i+1 to len(numbers):
        for j in range(i + 1, len(nums)):
            # Check if the sum of the pair equals the target
            if nums[i] + nums[j] == target:
                return [i, j]  # Return the indices of the two numbers
            

    return None  # Return None if no pair is found

# Optimized Solution: Using a Hash Map (Dictionary):
def two_sum_hash_map(nums, target):
    # Create a hash map to store the indices of the numbers
    seen = {}
    
    # Iterate through the list of numbers
    for i in range(len(nums)):
        # Calculate the complement (the number needed to reach the target)
        needed = target - nums
        
        # Check if the complement is already in the hash map
        if needed in seen:
            return [seen[needed], i]  # Return the indices of the two numbers
        
        # If not, add the current number and its index to the hash map
        seen[nums[i]] = i
    
    return None  # Return None if no pair is found        



