def main():
    result = []
    valid = False
    while valid == False:
        start = input('Enter the starting letter: ')
        end = input('Enter the ending letter: ')
        if start>end:
            print ('error message')
            valid = False
        else: 
            if start.isalpha() == False or end.isalpha() == False:
                valid = False
            else: 
                valid = True
                print (valid)
                break
    
    begin = ord(start)
    last = ord(end)
    for num in range(begin, last +1 , 1):     
        result.append(chr(num))
    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result,valid


if __name__ == '__main__':
    main()
