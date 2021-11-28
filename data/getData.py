#Script to get data from github https://github.com/pcm-dpc/COVID-19/blob/master/
import pandas as pd

def getProvince_dataset():
    #Province dataset
    date_fileProvince = 'dpc-covid19-ita-province-20200224.csv'
    urlProvince = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/'+date_fileProvince

    dataProvince = pd.read_csv(urlProvince)
    df_province = pd.DataFrame(dataProvince)
    return df_province

def getRegioni_dataset():
    #Region dataset
    date_fileRegion = 'dpc-covid19-ita-regioni-20200224.csv'
    urlRegioni = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/'+date_fileRegion

    dataRegioni = pd.read_csv(urlRegioni)
    df_regioni = pd.DataFrame(dataRegioni)
    return df_regioni