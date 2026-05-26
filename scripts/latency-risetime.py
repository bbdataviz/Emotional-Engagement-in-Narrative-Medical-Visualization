import pandas as pd
import csv

# calculate storypiece by substracting rise time and latency of 1.8 s from skin conductance response
def latency(df, path):
    latency = 1.8
    #add new column
    df.insert(6,'storypiece_response', 0)
    df.insert(7,'stimulus_time', 0)

    for i in df.index:
        resp = df['EdaScrCount []'].iloc[i] # check for response
        if resp == 1:
            rise = df['EdaScrRiseTimesMean [s]'].iloc[i]
            rel = df['Time rel [s]'].iloc[i]
            stimulus_time = int(rel - rise - latency) # substract rise time and latency
            #print('float: ' + str(stimulus_time_float) + ', int: ' + str(stimulus_time))
            for j in df.index:
                if df['Time rel [s]'].iloc[j] == stimulus_time:
                    story_stimulus = df['storypiece'].iloc[j] # find stimulus caused
                    stimulus_time = df['Time abs [hh:mm:ss]'].iloc[j]  
                    df.at[i, 'storypiece_response'] = story_stimulus
                    df.at[i, 'stimulus_time'] = stimulus_time
                    df.to_csv(path + "Results-labeled-stimulus.csv", index=False)
                   

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


latency(df1, path1)
latency(df2, path2)                    
latency(df3, path3)
latency(df4, path4)  
latency(df5, path5)
latency(df6, path6)  
latency(df7, path7)
latency(df8, path8)  
latency(df9, path9)
latency(df10, path10)  
latency(df11, path11)
latency(df12, path12)  
latency(df13, path13)
latency(df14, path14)  
latency(df15, path15)
latency(df16, path16)  
latency(df17, path17)
latency(df18, path18)  
latency(df19, path19)
latency(df20, path20)  
latency(df21, path21)
latency(df22, path22)  
latency(df23, path23)