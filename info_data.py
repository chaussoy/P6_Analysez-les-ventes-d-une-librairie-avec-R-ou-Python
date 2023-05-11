#!/usr/bin/env python
# coding: utf-8

# In[2]:


def info_data(df):
    print('\033[1;34mContrôle_import_dataframe\033[0m')
    print(df.head())
    print ('-'*45)
    print('\033[1;34mInfos_du_dataframe\033[0m')
    print(df.info())
    print ('-'*45)
    print('\033[1;34mRecherche_des_doublons\033[0m')
    print(df.duplicated().sum())
    print ('-'*45)
    print('\033[1;34mRecherche_des_valeurs_manquantes\033[0m')
    print(df.isna().sum())
    print ('-'*45)
    print('\033[1;34mNombre_de_valeurs_uniques_par_variables\033[0m')
    print(df.nunique())
    print ('-'*45)
    print('\033[1;34mIndicateurs statistiques\033[0m')
    print(df.describe())
    print ('-'*45) 
    

