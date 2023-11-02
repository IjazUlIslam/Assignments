def Multiple(integer1, integer2):
    if integer1 % integer2 == 0:
        print(f'{integer1} is the multiple of {integer2}')
    else:
        print(f'{integer1} is not multiple of {integer2}')
Multiple(int(input("Enter integer1 : ")), int(input("Enter integer2 : ")))

