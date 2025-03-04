from datetime import datetime, timedelta

import pymysql
import pandas as pd
import yfinance as yf

mysql_conn = pymysql.connect(host='localhost', user='root', password='doitmysql',db='us_stock')

def getCompany():
    
    mysql_cur = mysql_conn.cursor()
    
    today = datetime.today() + timedelta(days=1)
    
    try:
        mysql_cur.execute("SELECT symbol, company_name, ipo_year, last_crawel_date_stock \
            FROM us_stock.nasdaq_company WHERE is_delete is NULL;")
        results = mysql_cur.fetchall()

        for row in results:
            _symbol = row[0]
            _company_name = row[1]

            if row[2] is None or row[2] ==0:
                _ipo_year = '1970'
            else:
                _ipo_year = row[2]
            
            if row[3] is None:
                _last_crawel_date_stock = str(_ipo_year) + '-01-01'
            else:
                _last_crawel_date_stock = row[3]
            
            if "." in _symbol:
                print(_symbol)
            else:
                if "/" in _symbol:
                    print(_symbol)
                else:
                    getStock(_symbol, _last_crawel_date_stock, today.strftime("%Y-%m-%d")) 
  
    except Exception as e:
        print("ERROR!!",e)
        mysql_conn.commit()
        mysql_conn.close()
        
        return {'error1': str(e)}
    
def getStock(_symbol, _start_date, _end_date):
    mysql_cur = mysql_conn.cursor()
    mysql_cur.execute("DELETE FROM us_stock.stock WHERE date >= %s and date <= %s and symbol = %s", (_start_date, _end_date, _symbol))
    mysql_conn.commit()
    
    try:
        stock_price = yf.download(_symbol, start=_start_date, end=_end_date)
        print("stockprice \n",stock_price)
        
        for index, row in stock_price.iterrows():
            _date = index.strftime("%Y-%m-%d")
            _open = str(row.loc["Open",_symbol])
            _high = str(row.loc["High",_symbol])
            _low = str(row.loc["Low",_symbol])
            _close = str(row.loc["Close",_symbol])
            #_adj_close = str(row.loc["Adj Close",_symbol]) 
            _volume = str(row.loc["Volume",_symbol])

            
            mysql_cur.execute("INSERT INTO us_stock.stock(date, symbol, open, high, low, close, adj_close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (_date, _symbol,_open,_high,_low, _close, "0", _volume))
            
        mysql_conn.commit()
        
        mysql_cur.execute("UPDATE us_stock.nasdaq_company SET open = %s, high = %s, low = %s, close = %s, adj_close = %s, volume = %s, last_crawel_date_stock = %s \
            WHERE symbol = %s", (_open, _high, _low, _close, "0", _volume, _date, _symbol))
        mysql_conn.commit()
            
    except Exception as e:
        print("ERROR-GETSTOCK", str(e))
        mysql_conn.commit()
        mysql_conn.close()
        
        return {'error2': str(e)}
                
if __name__ == '__main__':
    getCompany()