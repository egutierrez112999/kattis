message = input()
if 3 <= len(message) <=1000:
    s_count = message.count('e')
    new_e = ''
    for i in range(s_count*2):
        new_e += 'e'
    print('h' + new_e + 'y')
