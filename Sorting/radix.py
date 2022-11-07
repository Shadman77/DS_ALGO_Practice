def radix_sort(arr, digit_pos_from_right):
    output_arr = []
    
    # Store nth digit wise variable
    count = []
    for _ in range(10):
        count.append([])
    
    non_zero_found = False
    for elem in arr:
        # taking the nth digit from the right from the number
        # the formula is floor(number / 10 to the power of digit from right) % 10 
        nth_digit = (elem // (10**digit_pos_from_right)) % 10
        count[nth_digit].append(elem)
        if nth_digit > 0:
            non_zero_found = True
    
    for digit in count:
        for elem in digit:
            output_arr.append(elem)

    if non_zero_found:
        return radix_sort(output_arr, digit_pos_from_right=digit_pos_from_right + 1)
    else:
        return output_arr
    

if __name__ == "__main__":
    arr = [100, 80, 25, 46, 554, 351, 52, 3, 37, 439, 80, 25, 46, 554, 351, 52]
    print(arr)
    print(radix_sort(arr, 1))