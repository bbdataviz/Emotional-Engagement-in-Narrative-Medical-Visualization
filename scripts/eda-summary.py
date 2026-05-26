import pandas as pd
import numpy as np
import csv
import importlib
importlib.reload(pd)

# df_peaks = pd.DataFrame({'P': [], 'story': [], 'storypiece': [], 'EdaScrAmplitudes_count': [], 'EdaScrAmplitudes_sum': [], 'EdaScl_mean': []}) 
feature_list = ['P', 'Group', 'story', 'n_amp', 'n_amp_per_min', 'sum_all_amp', 'amp_per_min', 'viewtime_sec', 'miss_perc', 'storypiece', 'max_peak', 'storypiece_sum', 'max_amp_sum', 'gender']
df_max = pd.DataFrame(0, index=np.arange(44), columns=feature_list)


def count_peaks(df, P, df_demo):
    for x in range(1,3): # for each story
        sum_all_amp = 0
        n_amp = 0
        sec = 0 # only seconds where scl > 0.3 (no missing)
        sec_all = 0 # all seconds spent in a story (incl miss data)
        max_peak = 0
        max_amp_sum = 0
        amp = 0
        for j in range(1,29): #[1,...,28] go through each storypiece
            amp_sum = 0 # sum of amplitudes for each story piece
            for i in df.index:
                s = df['story'].iloc[i]
                if s == x:
                    sp = df['storypiece'].iloc[i] 
                    if sp == j:
                        sec_all = sec_all + 1
                        
                        if df['EdaSclMean [uS]'].iloc[i] > 0:
                            sec = sec + 1
                            sum_all_amp = sum_all_amp + df['EdaScrAmplitudesMean [uS]'].iloc[i]  
                            amp = df['EdaScrAmplitudesMean [uS]'].iloc[i]
                            amp_sum += amp
                            if df['EdaScrAmplitudesMean [uS]'].iloc[i] > 0:
                                n_amp = n_amp + 1       

                        #calculate a single maximum peak
                        if amp > max_peak:
                           max_peak = amp
                           storypiece_max = j

                        # calculate storypiece with max sum of amplitudes
                        if amp_sum > max_amp_sum:
                            max_amp_sum = amp_sum
                            storypiece_max_amp = j
                      
            # save all values
            p = df['P'].iloc[1]
            #print("P: " + str(p) + "sec: " + str(sec) + "all_sec" + str(sec_all))
            row = P-1
            
            if sec == 0:
                n_amp_per_min = 'nan'
                amp_per_min = 'nan'
                miss = 'nan'
            else:
                n_amp_per_min = n_amp / (sec * (1/60)) # number of amp per min
                amp_per_min = sum_all_amp / (sec * (1/60))  # sum of amp per min
                miss = 100 * (sec_all - sec)/sec_all # percent missing data
            
            if x == 1:
                offset_max = 0
                story_no = 'ind'
            else:
                offset_max = 23
                story_no = 'xgen'

            if max_peak == 0:
                storypiece_max = 'nan'
            if max_amp_sum == 0:
                storypiece_max_amp = 'nan'

            if P % 2 == 0:
                group = 'B'
            else:
                group = 'A'
            
            gender = df_demo['gender'].iloc[P-1]
            if gender == 1 or gender == 3:
                gender = 'female'
            else:
                gender = 'male'
                        
                
            # max peak and max amplitude sum
            df_max.at[row+offset_max, 'P'] = p 
            df_max.at[row+offset_max, 'Group'] = group 
            df_max.at[row+offset_max, 'story'] = str(story_no)
            df_max.at[row+offset_max, 'n_amp'] = str(n_amp)
            df_max.at[row+offset_max, 'n_amp_per_min'] = str(n_amp_per_min)
            df_max.at[row+offset_max, 'sum_all_amp'] = str(sum_all_amp)
            df_max.at[row+offset_max, 'viewtime_sec'] = str(sec_all)
            df_max.at[row+offset_max, 'amp_per_min'] = str(amp_per_min)
            df_max.at[row+offset_max, 'miss_perc'] = str(miss)
            df_max.at[row+offset_max, 'storypiece'] = str(storypiece_max)
            df_max.at[row+offset_max, 'max_peak'] = str(max_peak)
            df_max.at[row+offset_max, 'storypiece_sum'] = str(storypiece_max_amp)
            df_max.at[row+offset_max, 'max_amp_sum'] = str(max_amp_sum)
            df_max.at[row+offset_max, 'gender'] = gender
            df_max.to_csv("Data_processed\\Eda-summaries-Ind+Gen\\Eda-summary.csv", index=False)


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


df_demo = pd.DataFrame(pd.read_csv("Data_processed\\personal_data.csv"))

count_peaks(df1, 1, df_demo)
count_peaks(df2, 2, df_demo)
count_peaks(df3, 3, df_demo)
count_peaks(df4, 4, df_demo)
count_peaks(df5, 5, df_demo)
count_peaks(df6, 6, df_demo)
count_peaks(df7, 7, df_demo)
count_peaks(df8, 8, df_demo)
count_peaks(df9, 9, df_demo)
count_peaks(df10, 10, df_demo)
count_peaks(df11, 11, df_demo)
count_peaks(df12, 12, df_demo)
count_peaks(df13, 13, df_demo)
count_peaks(df14, 14, df_demo)
count_peaks(df15, 15, df_demo)
count_peaks(df16, 16, df_demo)
count_peaks(df17, 17, df_demo)
count_peaks(df18, 18, df_demo)
count_peaks(df19, 19, df_demo)
count_peaks(df20, 20, df_demo)
count_peaks(df21, 21, df_demo)
count_peaks(df22, 22, df_demo)
count_peaks(df23, 23, df_demo)



