import pandas as pd
import csv


def missing(df, P, G, path):
    df.insert(0, 'P', P)
    df.insert(1, 'Group', G)
    
    # label missing values for scl < 0.3 microsiemens s
    for i in df.index:
        scl = df['EdaSclMean [uS]'].iloc[i] # check for response
        amp = df['EdaScrAmplitudesMean [uS]'].iloc[i]
        if scl < 0.3 and amp == 0:
            df.at[i, 'EdaSclMean [uS]'] = 0
            df.to_csv(path + "Results-labeled-missing-0.csv", index=False)
            

def missamps(df, path):
    # label missing value for a story piece if all values are 'nan'
    for x in range(1,3):
        for j in range(1,29):
            scl_check = 0
            # print(scl_check)
            for i in df.index:
                s = df['story'].iloc[i]
                if s == x: 
                    p = df['storypiece'].iloc[i]
                    if p == j:
                        check_miss = df['EdaSclMean [uS]'].iloc[i]
                        if check_miss != 0:  # if one is not NaN
                            scl_check = 1
        
            # mark all values with NaN for a storypiece                
            if scl_check == 0:
                print('true')
                story = x
                storypiece = j
                for c in df.index:
                    if df['story'].iloc[c] == story and df['storypiece'].iloc[c] == storypiece:
                        df.at[c,'EdaScrAmplitudesMean [uS]'] = "NaN"
                        df.to_csv(path + "Results-labeled-missing.csv", index=False)
        df.to_csv(path + "Results-labeled-missing.csv", index=False)
    

path1 = "Data_processed\\P1\\"
path2 = "Data_processed\\P2\\"
path3 = "Data_processed\\P3\\"
path4 = "Data_processed\\P4\\"
path5 = "Data_processed\\P5\\"
path6 = "Data_processed\\P6\\"
path7 = "Data_processed\\P7\\"
path8 = "Data_processed\\P8\\"
path9 = "Data_processed\\P9\\"
path10 = "Data_processed\\P10\\"
path11 = "Data_processed\\P11\\"
path12 = "Data_processed\\P12\\"
path13 = "Data_processed\\P13\\"
path14 = "Data_processed\\P14\\"
path15 = "Data_processed\\P15\\"
path16 = "Data_processed\\P16\\"
path17 = "Data_processed\\P17\\"
path18 = "Data_processed\\P18\\"
path19 = "Data_processed\\P19\\"
path20 = "Data_processed\\P20\\"
path21 = "Data_processed\\P21\\"
path22 = "Data_processed\\P22\\"
path23 = "Data_processed\\P23\\"

file = "Results-labeled-missing-0.csv"

df1 = pd.DataFrame(pd.read_csv(path1 + file, quoting=csv.QUOTE_ALL))
df2 = pd.DataFrame(pd.read_csv(path2 + file, quoting=csv.QUOTE_ALL))
df3 = pd.DataFrame(pd.read_csv(path3 + file, quoting=csv.QUOTE_ALL))
df4 = pd.DataFrame(pd.read_csv(path4 + file, quoting=csv.QUOTE_ALL))
df5 = pd.DataFrame(pd.read_csv(path5 + file, quoting=csv.QUOTE_ALL))
df6 = pd.DataFrame(pd.read_csv(path6 + file, quoting=csv.QUOTE_ALL))
df7 = pd.DataFrame(pd.read_csv(path7 + file, quoting=csv.QUOTE_ALL))
df8 = pd.DataFrame(pd.read_csv(path8 + file, quoting=csv.QUOTE_ALL))
df9 = pd.DataFrame(pd.read_csv(path9 + file, quoting=csv.QUOTE_ALL))
df10 = pd.DataFrame(pd.read_csv(path10 + file, quoting=csv.QUOTE_ALL))
df11 = pd.DataFrame(pd.read_csv(path11 + file, quoting=csv.QUOTE_ALL))
df12 = pd.DataFrame(pd.read_csv(path12 + file, quoting=csv.QUOTE_ALL))
df13 = pd.DataFrame(pd.read_csv(path13 + file, quoting=csv.QUOTE_ALL))
df14 = pd.DataFrame(pd.read_csv(path14 + file, quoting=csv.QUOTE_ALL))
df15 = pd.DataFrame(pd.read_csv(path15 + file, quoting=csv.QUOTE_ALL))
df16 = pd.DataFrame(pd.read_csv(path16 + file, quoting=csv.QUOTE_ALL))
df17 = pd.DataFrame(pd.read_csv(path17 + file, quoting=csv.QUOTE_ALL))
df18 = pd.DataFrame(pd.read_csv(path18 + file, quoting=csv.QUOTE_ALL))
df19 = pd.DataFrame(pd.read_csv(path19 + file, quoting=csv.QUOTE_ALL))
df20 = pd.DataFrame(pd.read_csv(path20 + file, quoting=csv.QUOTE_ALL))
df21 = pd.DataFrame(pd.read_csv(path21 + file, quoting=csv.QUOTE_ALL))
df22 = pd.DataFrame(pd.read_csv(path22 + file, quoting=csv.QUOTE_ALL))
df23 = pd.DataFrame(pd.read_csv(path23 + file, quoting=csv.QUOTE_ALL))

missing(df1, 'P01', 'A', path1)
missing(df2, 'P02', 'B', path2)                    
missing(df3, 'P03', 'A', path3)
missing(df4, 'P04', 'B', path4)  
missing(df5, 'P05', 'A', path5)
missing(df6, 'P06', 'B', path6)  
missing(df7, 'P07', 'A', path7)
missing(df8, 'P08', 'B', path8)  
missing(df9, 'P09', 'A', path9)
missing(df10, 'P10', 'B', path10)  
missing(df11, 'P11', 'A', path11)
missing(df12, 'P12', 'B', path12)  
missing(df13, 'P13', 'A', path13)
missing(df14, 'P14', 'B', path14)  
missing(df15, 'P15', 'A', path15)
missing(df16, 'P16', 'B', path16)  
missing(df17, 'P17', 'A', path17)
missing(df18, 'P18', 'B', path18)  
missing(df19, 'P19', 'A', path19)
missing(df20, 'P20', 'B', path20)  
missing(df21, 'P21', 'A', path21)
missing(df22, 'P22', 'B', path22)  
missing(df23, 'P23', 'A', path23)

missamps(df1, path1)
missamps(df2, path2)                    
missamps(df3, path3)
missamps(df4, path4)  
missamps(df5, path5)
missamps(df6, path6)  
missamps(df7, path7)
missamps(df8, path8)  
missamps(df9, path9)
missamps(df10, path10)  
missamps(df11, path11)
missamps(df12, path12)  
missamps(df13, path13)
missamps(df14, path14)  
missamps(df15, path15)
missamps(df16, path16)  
missamps(df17, path17)
missamps(df18, path18)  
missamps(df19, path19)
missamps(df20, path20)  
missamps(df21, path21)
missamps(df22, path22)  
missamps(df23, path23)


