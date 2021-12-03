#Script to get data from github https://github.com/pcm-dpc/COVID-19/blob/master/
import pandas as pd
from datetime import datetime

def getProvince_dataset(time):
    time = datetime.strftime(time, '%Y%m%d')
    #Province dataset
    date_fileProvince = 'dpc-covid19-ita-province-'+str(time)+'.csv'
    urlProvince = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/'+date_fileProvince

    dataProvince = pd.read_csv(urlProvince)
    df_province = pd.DataFrame(dataProvince)
    return df_province

def getRegioni_dataset(time):
    time = datetime.strftime(time, '%Y%m%d')
    #Region dataset
    date_fileRegion = 'dpc-covid19-ita-regioni-'+time+'.csv'
    urlRegioni = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/'+date_fileRegion
    dataRegioni = pd.read_csv(urlRegioni)
    df_regioni = pd.DataFrame(dataRegioni)
    return df_regioni