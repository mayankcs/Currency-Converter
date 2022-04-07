import exchange_rate

class history:

    def prevMonthDate(self,date):
        '''This function returns previous month date
            for the date provided'''
        month=int(date[5:7])
        year=date[:4]
        month-=1
        if month%10==month:
            month='0%s'%(month)
        if month=='00':
            month=12
            year=str(int(date[:4])-1)
        month=str(month)
        daate=date[8:]
        if daate=='30' or daate=='31':
            daate='28' 
        if month=='02' and int(daate)>28:
            daate='28'
        return '%s-%s-%s'%(year,month,daate)
        
    def prevYearDate(self,date):
        '''This function returns previous year date
            for the date provided'''
        year=str(int(date[:4])-1)
        return '%s-%s'%(year,date[5:])


    def get_history(self,source,target,date):
        '''This function returns exchange rate of currency
            for previous month and previous year'''
        prevMonth=self.prevMonthDate(date)
        prevYear=self.prevYearDate(date)
        rate1=exchange_rate.get_exchange_rate(source,target,prevMonth)
        rate2=exchange_rate.get_exchange_rate(source,target,prevYear)
        return [rate1,rate2]


