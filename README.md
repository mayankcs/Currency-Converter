

# Currency-Converter 💰
This is the command line app for Real time Currency Converter, that let you convert your currency into other 

*Q. Why i called it real time ?*

*--> Because, currency exchange rate's are always changing and that is why this is real time problem*

> Hey !! You want Web app for this converter ?
> 
> No worries, we have **deployed this app to Heroku** 
> 
> **[click here](https://currency-cvt.herokuapp.com/)** to see 

Now let's have deep dive into command line app 

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

Currency code can be found from [here](https://www.iban.com/currency-codes)

## How it works?

we have three files 

 1. exchange_rate.py
 2. history.py
 3. main.py

 **main. py** :-
 
it is the driving script that calls required function from other files in the same directory 

**exchange_rate.py** :-

This file has function named get_exchange_rate that return exchange rate ,and this function is called by main script and exchange rate returned is multiplied with amount supplied by user and result is displayed to user

get_exchange_rate function uses API to fetch exchange rate in real time

**history. py**:-

This file contains function to get previous month date and previous year date, which are then supplied to get_exchange_rate function in exchange_rate.py to have exchange rate of that time.
Once we have exchange rate then converted value as per that rate is displayed to user in last two lines
