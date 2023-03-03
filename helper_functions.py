import numpy as np
import pandas as pd

def wkpentopounds(amt_paid:float) -> float:

    if not np.isnan(amt_paid):
        amt_pound = amt_paid/100
        amt_week = amt_pound/2

    elif np.isnan(amt_paid):
        raise ValueError('amt_paid is a NaN value')
    
    return amt_week


def shop_ex(shop: pd.Series) -> pd.Series:
    
    shop_list = ['70','140','2390','340','680','1300','1420','1550','2150','1590','1980','2190',
                    '1090','275','770','480','2370','1002','2960']
    header = shop.name
    shop = shop.to_frame()
    
    return shop[header].isin(shop_list)


def internet_ex(shop: pd.DataFrame) -> pd.DataFrame:
    shop_list = ['1130','1131','1132','1133','1134','1135','1136','1140','1141','1142',
                    '1143','1144','1145','1146']
    header = shop.name
    shop = shop.to_frame()
    
    return shop[header].isin(shop_list)

def clothing_chains(shop: pd.DataFrame) -> pd.DataFrame:
    '''function to identify c codes with x suffix (selected clothing chains)'''
    shop_list = ['350','670','760','1510','2250','2260','2380','330','570','130','190','220',                                         
                   '390','580','830','980','1060','1870','170','270','460','900','1000',
                   '1190','1710','2290','2300','1420','1450','1600','1610','740','880',
                   '1400','1540','1630','1700','1830','1910','2240','2400','2950','3060',
                   '3150','3180']
    header = shop.name
    shop = shop.to_frame()
    
    return shop[header].isin(shop_list)
    
    
def large_supermarkets(shop: pd.DataFrame) -> pd.DataFrame:
    '''function to identify c codes with suffix y (large supermarkets)''' 
    
    shop_list = ['70','140','2390','340','680','1300','1550','2150','1590',
                    '1980','2190','1090','275','770','480','2370','1002','2960']  
    header = shop.name
    shop = shop.to_frame()
    
    return shop[header].isin(shop_list)


def charity_shops(shop: pd.DataFrame) -> pd.DataFrame:
    '''function to identify c codes with suffix z (chairty shops)'''
    shop_list = ['410']
    header = shop.name
    shop = shop.to_frame()
    
    return shop[header].isin(shop_list)
