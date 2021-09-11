def kaanBey():
    for kaan in range(1, 11):
        print('*'*(0+kaan) + "    "*(10-kaan) + '*'*(0+kaan))
    for reis in range(1,11):
        print('*'*(10-reis) + "    "*(0+reis) + '*'*(10-reis))
kaanBey()
