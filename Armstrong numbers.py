while True:
    print("Bitte Zahl eingeben:")
    number = str(input())
    sum = 0

    for i in number:
        sum = sum + int(i)**len(number)

    if sum == int(number):
        print("%s ist eine Armstrong Nummer" % (number))
    else:
        print("%s ist leider KEINE Armstrong Nummer" % (number))