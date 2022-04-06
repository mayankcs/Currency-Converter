import exchange_rate
import history

print("******************************")
print("Welcome to Currency convertor")
print("******************************\n")
print("Please type 3 letter country code")
source=input("Convert from ").upper().rstrip()
target=input("Convert to ").upper().rstrip()
amount=float(input("Amount to convert %s "%(source)))
print("******************************")
date=0

try:
    ex_rate,date=exchange_rate.get_exchange_rate(source,target)
    history=history.get_history(source,target,date)


    result=amount*ex_rate
    print('\n')
    print('%s %d equals to %s %f'%(source,amount,target,result))

    prevMonthRate=history[0][0]
    prevYearRate=history[1][0]

    prevMonthAmount=amount*prevMonthRate
    prevYearAmount=amount*prevYearRate
    print('\n')
    st1='last month %s %d was equals to %s %f'%(source,amount,target,prevMonthAmount)
    st2='last year %s %d was equals to %s %f'%(source,amount,target,prevYearAmount)
    print(st1)
    print(st2)

except:
    print("please type the country code correctly")

