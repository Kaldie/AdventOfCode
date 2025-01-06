# 
input = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0] # removed last 0 for sake of initialisation
input.reverse()

prev2=0
prev1=0
options = [[]]

for index, aim in enumerate(input):
    new_options = []
    for option in options:

        prev3= option[index-3] if len(option) >= 3 else 0
        prev2= option[index-2] if len(option) >= 2 else 0
        prev1= option[index-1] if len(option) >= 1 else 0

        # getal van 6 chars lang
        for i in range(8):
            a = (prev3 << 9 ) + (prev2 << 6 ) + (prev1 << 3 ) + i
            b = a % 8
            b = b ^ 7
            c = a >> b
            b = b ^ 7
            b = b ^ c
            b= b % 8

            # print(f"a: {a:b}, b: {b:b} c: {c:b}")
            if b == aim:
                new_options.append(option + [i])
    
    if len(new_options) == 0:
        raise ValueError(options, aim)
    
    options = new_options

print(options)

solves = []
for opt in options:
    opt_value = 0
    opt.reverse()
    for index, value in enumerate(opt):
        print(f"{(value  << (index * 3)):b}")
        opt_value += (value  << (index * 3))
    print(f'{opt_value:b}')
    solves.append(opt_value)

# Quick and dirty hack!
print(min(solves))
