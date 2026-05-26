import pandas as pd
import csv


def clear(df, path):  # remove all rows with zeros
    df_transpose = df.T
    for i in df.index:
        val = df['story'].iloc[i]  # save abs time at index i
        if val == 0:
            df_transpose.pop(i)
            df_transpose.to_csv(
                path + "Results-labeled-clear.csv", index=False)
    df = df_transpose.T
    df.to_csv(path + "Results-labeled-clear.csv", index=False)
    
    
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

file = "Results-labeled-missing.csv"

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
    
# clear(df1, path1)
# clear(df2, path2)
# clear(df3, path3)
# clear(df4, path4)
# clear(df5, path5)
# clear(df6, path6)
# clear(df7, path7)
# clear(df8, path8)
# clear(df9, path9)
# clear(df10, path10)
# clear(df11, path11)
# clear(df12, path12)
# clear(df13, path13)
# clear(df14, path14)
# clear(df15, path15)
# clear(df16, path16)
# clear(df17, path17)
# clear(df18, path18)
# clear(df19, path19)
# clear(df20, path20)
# clear(df21, path21)
# clear(df22, path22)
# clear(df23, path23)

def clearraw(df, path):  # remove all rows with zeros
    df_transpose = df.T
    for i in df.index:
        val = df['EdaScl_mean'].iloc[i]  # save abs time at index i
        if val == 0:
            df_transpose.pop(i)
            df_transpose.to_csv(
                path + "alldata_storypieces_raw_nomiss.csv", index=False)
    df = df_transpose.T
    df.to_csv(path + "alldata_storypieces_raw_nomiss.csv", index=False)
    
pathraw = "D:\\__MASTER_STUDY\\EXDA\\datasets\\Eda-summaries-Ind+Gen\\"
fileraw = "alldata_storypieces_raw.csv"

df = pd.DataFrame(pd.read_csv(pathraw + fileraw, quoting=csv.QUOTE_ALL))

clearraw(df, pathraw)