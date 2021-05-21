while 1:
    register = input('Welcome! Do you want to register? (Y/N): ').upper()
    if register == 'Y':
        username = input('Enter your username: ')
        fullname = input('Enter your full name: ')
        password = input('Enter your password: ')


        #password check
        while 1:
            uppercheck = False
            lowercheck = False
            numcheck = False
            passwordcheck = False

            if len(password) < 8:
                password = input('Enter a valid password: ')
            else:
                u = password.upper()
                l = password.lower()
                i = 0
                while i<len(password):
                    if password[i] == u[i] :
                        uppercheck = True
                    if password[i] == l[i]:
                        lowercheck = True
                    if password[i].isnumeric():
                        numcheck = True
                    if (uppercheck == True and lowercheck == True and numcheck == True):
                        passwordcheck = True
                        break
                    i = i+1
                if passwordcheck == True:
                    print('Thankyou for registration')
                    break
                else:
                    password = input('Enter a valid password: ')


        while 1:
            login = input('Do you want to login? (Y/N): ').upper()
            if login == 'Y':
                #login check
                while 1:
                    username_entered = input('Enter your username: ')
                    password_entered = input('Enter you password: ')

                    if username_entered == username and password_entered == password:
                        print('Welcome')
                        break
                    else:
                        print('Enter valid username and password')


                #Services
                while 1:
                    print('We provide three services: ')
                    print('1. Basic Calculator \n2. Table Generator \n3.Pattern Generator')
                    service_num = input('Choose one of the above services (1/2/3): ')

                    #Basic Calculator
                    if service_num == '1':
                        print('We are happy to provide Basic Calculator!')
                        #input check
                        while 1:
                            first_num = input('Enter the first number: ')
                            #first num check
                            if first_num.isnumeric():
                                first_num = int(first_num)
                                while 1:
                                    second_num = input('Enter the second number: ')
                                    #second num check
                                    if second_num.isnumeric():
                                        second_num = int(second_num)
                                        while 1:
                                            operator = input('Enter the operator(+ or - or * or /): ')
                                            #operator check
                                            if operator == '+' or operator == '-' or operator == '*' or operator == '/':
                                                break
                                            else:
                                                print('Not a valid operator!')
                                        break
                                    else:
                                        print('Not a valid number!')
                                break
                            else:
                                print('Not a valid number')

                        #Calculate
                        if operator == '+':
                            print('Your result is: {}'.format(first_num + second_num))
                        if operator == '-':
                            print('Your result is: {}'.format(first_num - second_num))
                        if operator == '*':
                            print('Your result is: {}'.format(first_num * second_num))
                        if operator == '/':
                            print('Your result is: {}'.format(first_num / second_num))
                        break


                    #Table Generator
                    elif service_num == '2':
                        print('We are happy to provide Table Generator!')
                        #input check
                        while 1:
                            num = input('Enter a number: ')
                            #num check
                            if num.isnumeric():
                                num = int(num)
                                print('Table is: ', end = '')
                                for i in range(1, 11):
                                    print(num*i, end = ' ')
                                break
                            else:
                                print('Invalid input!')
                        break

                    #Pattern Genrator
                    elif service_num == '3':
                        print('We are happy to provide Pattern Generator!')
                        #input check
                        character = input('Enter the character: ')
                        while 1:
                            num = input('Enter a number how many times the pattern is to be generated: ')
                            if num.isnumeric():
                                num = int(num)
                                print('Pattern is: ')
                                for i in range(1, num+1):
                                    print(character*i)
                                break
                            else:
                                print('Invalid input!')
                        break
                    else:
                        print('Invalid input')
        
                break
                        
            elif login == 'N':
                print('Exited successfully!')
                break
            else:
                print('Invalid input!')
       
        break

        
    if register == 'N':
        print('Exited successfully')
        break
    else:
        print('Invalid Input')
    
            
             
                
                
                
                
                                
                                  
            
                  
            
            
                    
                
            
    
