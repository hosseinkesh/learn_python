weight = int(input('Weight? '))
weight_type = input("(K)g or (L)bs? ")
if weight_type.lower() == 'k':
    print(str(weight) + "Kg")
elif weight_type.lower() == 'l' :
    print(str(weight) + "Lbs")
else :
    print('Invalid weight type')