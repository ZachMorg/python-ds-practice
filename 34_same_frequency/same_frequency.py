def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_dict1 = {}
    num_dict2 = {}
    num_list1 = list(str(num1))
    num_list2 = list(str(num2))
    for num in num_list1:
        num_dict1[num] = num_dict1.get(num, 0)+1
    for num in num_list2:
        num_dict2[num] = num_dict2.get(num, 0)+1
    return num_dict1 == num_dict2