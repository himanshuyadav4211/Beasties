exec(open('venv/bin/activate_this.py').read(), {'_file_': 'venv/bin/activate_this.py'})

if _name_ == '_main_':
    print('\033c')
    print('\n\nBeasties')
    print('------------------------\n\n')
    Break = False
    pincode = -1
    state = ''
    city = ''
    animal = ''
    breed = ''
    service_type = -1

    while not Break:
        stateORpin = int(input('Find slots by:\n1. Pincode\n2. State\n   (enter 1 or 2)\n'))
        if stateORpin == 1:
            print('\033c')
            print('\n\nBeasties')
            print('------------------------\n\n')

            # ask for pincode
            pincode = int(input('Enter your pincode: '))
            Break = True
        elif stateORpin == 2:
            print('\033c')
            print('\n\nBeasties')
            print('------------------------\n\n')

            # ask for state + city
            state = input('Enter your state: ')
            city = input('Enter you city: ')
            Break = True
        else:
            print('\033c')
            print('\n\nBeasties')
            print('------------------------\n\n')
            print('Invalid ! Try again !\n')
    
    print('\033c')
    print('\n\nBeasties')
    print('------------------------\n\n')
    animal = input('What pet do you own ? (Dog/Cat/others)\n').lower()
    if animal == 'dog':
        print('\033c')
        print('\n\nBeasties')
        print('------------------------\n\n')

        breed = input('What is the breed of your dog ? (type \'na\' if you don\'t know)\n').lower()
    elif animal == 'cat':
        print('\033c')
        print('\n\nBeasties')
        print('------------------------\n\n')
        
        breed = input('Which cat do you have ? (type \'na\' if you don\'t know)\n').lower()
    else:
        print('\033c')
        print('\n\nBeasties')
        print('------------------------\n\n')

        breed = input('What is the breed/variety of your' + animal + '?\n').lower()

    Break = False
    while not Break:
        service_type = int(input('Enter your preferred service:\n1. Basic Wash\n2. Haircut\n3. Wash + massage\n4. Disease/injury treatment\n5. Pet training\n   (enter the number)\n   '))
        if service_type >= 1 and service_type <= 5:
            print('\033c')
            print('\n\nBeasties')
            print('------------------------\n\n')
            
            print('Thank you ! We shall soon provide the services...')
            Break = True
        else:
            print('\033c')
            print('\n\nBeasties')
            print('------------------------\n\n')
            print('Invalid ! Try again !\n')

    # pet clinic store address and schedules
    
    # petcare worker emails and phone number
