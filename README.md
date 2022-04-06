


# Currency-Converter 💰
This is the command line programme for the Real Time Currency Converter, which allows you to convert currency to other currencies.

Jump directly to
[How to run this command line app](https://github.com/mayankcs/Currency-Converter/blob/main/README.md#how-to-run-currency-converter)

*Q. Why i called it real time ?*

*--> Because, currency exchange rate's are dynamic and get constatntly fluctuate due to the fact that a currency's value is determined by a variety of factors in the country

> Hey !! You want Web app for this converter ?
> 
> Not to worry, we've already **deployed this app on Heroku**.
> 
> **[click here](https://currency-cvt.herokuapp.com/)** to check it live!

Now let's have deep dive into command line app 

## How to run Currency-Converter

 1. **Clone** this Github repository 
 2. **Install** all dependencies specified in requirements. txt
 3. Run **main.py**

main.py will demand 3 arguments from user
1. Source currency code
2. Target currency code
3. Amount to convert

The command line program will not only Display the converted amount, but will also inform the user of what the conversion value would have been if the previous/last month's or year's exchange rate had been used.

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


![Currency](https://user-images.githubusercontent.com/65117236/161817311-301ce9c3-e1d7-467f-a67b-768677f8f4de.JPG)

The last two lines describe the conversion using historical data from the prior month and year.

Currency code can be found from [here](https://www.iban.com/currency-codes)

## How it works?

we have three files 

 1. exchange_rate.py
 2. history.py
 3. main.py

 **main. py** :-
 
This is the script that calls the necessary functions from other files in the same directory and displays Conversion to the user.

**exchange_rate.py** :-

This file has a function named get exchange rate, which returns the exchange rate. The function is called by the main script, and the exchange rate obtained is multiplied by the amount given by the user, and the result is presented to the user.

The get_exchange_rate method uses the API to retrieve the current exchange rate.

**history. py**:-

This file provides functions for retrieving the prior month and year dates, which are then passed to the get_exchange_rate function in exchange rate.py to obtain the exchange rate at that time.

Once we have an exchange rate, the converted value is shown to the user in the last two lines.

## 💻 Web Application for Currency-Converter

Check out that Github repository by clicking [here](https://github.com/mayankcs/Currency-Converter-web-app).
Alternatively, you can simply click [here](https://currency-cvt.herokuapp.com/) to view that Website in real time.
