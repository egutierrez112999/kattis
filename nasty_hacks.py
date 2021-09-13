cases = int(input())
case_list = []
for i in range(cases):
    case_list.append(input().split())
def ad(case):
    revenue = int(case[0])
    ad_profit = int(case[1])
    ad_price = int(case[2])
    if ad_profit > (revenue + ad_price):
        return('advertise')
    elif ad_profit == (revenue + ad_price):
        return('does not matter')
    else:
        return('do not advertise')
for i in case_list:
    print(ad(i))
