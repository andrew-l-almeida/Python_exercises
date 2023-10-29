import os
purchase_list = []

while True:
    try:
        print('Type a Option')
        option = str(input('[I]nsert [D]elete [L]ist [C]lose: '))[0].upper()

        if option == 'C':
            break   
        if option == 'I':
            os.system('cls')
            item = input('Type the name that you want to add in your purchase list: ')
            purchase_list.append(item)
            print(f'{item} added succefully!')
        if option == 'L':
            os.system('cls')
            if len(purchase_list) == 0:
                print('Your list is empty')
            else:
                os.system('cls')
                for i, item in enumerate(purchase_list):
                    print(f'{i} {item}')
        if option == 'D':
            os.system('cls')
            indice = int(input('Type the indice that you want to delete: '))
            print(f'{purchase_list[indice]} deleted succefully!!')
            purchase_list.pop(indice)
    except:
        os.system('cls')
        print('We cannot delete this item! ')