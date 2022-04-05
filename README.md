

# Currency-Converter 💰
This is the command line app for Real time Currency Converter, that let you convert your currency into other 

*Q. Why i called it real time ?*

*--> Because, currency exchange rate's are always changing and that is why this is real time problem*

Let's first have look towards it

## How to run Currency-Converter

 1. **Clone** this Github repository 
 2. **Install** all dependencies specified in requirements. txt
 3. Run **main.py**

main.py will demand 3 arguments from user
1. Source currency code
2. Target currency code
3. Amount to convert

command line app will not only provide converted amount but also will let user know what would have been conversion value if exchange rate of previous/last month or year was applied  

See the demo below:-
Say i want to convert USD 5 to INR

run main.py

    code>main.py
    ******************************
    Welcome to Currency convertor
    ******************************
    
    Please type 3 letter country code
    Convert from USD
    Convert to INR
    Amount to convert USD 5
    ******************************
    USD 5 equals to INR 376.990445
    
    last month USD 5 was equals to INR 381.867520
    last year USD 5 was equals to INR 366.398745

![github](https://user-images.githubusercontent.com/65117236/161731609-3eb6ab62-222e-466d-9cba-5b38952d33aa.JPG)

last 2 lines tells the conversion using historical data of previous month and previous year
