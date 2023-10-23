def safe_print_list(my_list=[], x=0):
    element_printed = 0
    try:
        for element in my_list:
            if element_printed < x:
                print(element, end=' ')
                element_printed += 1
                print()
    except:
    return (element_printed)
