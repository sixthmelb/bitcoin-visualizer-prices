#Import Librari
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

#Menyiapkan Data
crypto = input("Masukan Crypto Currency [contoh : BTC] : ")
currency = input("Masukkan Mata Uang Pembanding [contoh : USD] : ")


start = dt.datetime(2020,1,1)
end = dt.datetime.now()

#Memproses Data/Kalkulasi
btc = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
#eth = web.DataReader(f"ETH-{currency}", "yahoo", start, end)

#Kode Untuk Perbandingan Dua CryptoCurrency
#plt.yscale("log")
#plt.plot(btc['Close'], label="BTC")
#plt.plot(eth['Close'], label="ETH")
#plt.legend(loc="upper left")
#plt.show()


#Kode Untuk Graph Lilin
mpf.plot(btc, type="candle", volume=True, style="yahoo")
