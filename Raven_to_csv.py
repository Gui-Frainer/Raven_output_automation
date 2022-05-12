#Converting txt files from Raven into .csv in two clicks:
#Species: In this case, the file name is 'filename.wav'
import pandas as pd
import os

folder_Dd = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Ddelphis/1_labels/txt/'
folder_Oo = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Oorca/1_labels/txt/'
folder_Sp = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Splumbea/1_labels/txt/'
folder_Ta = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Taduncus/1_labels/txt/'

def convert_Raven_files (folder):
    
    for path, folders, files in os.walk(folder):        
        duration = 0
        
        for txt in files:
            df = pd.read_csv(folder+txt, sep="	", index_col=False)
            #print(df)
            df1 = df[['Begin Time (s)','End Time (s)','Delta Time (s)']]
            df1 = df1.rename(columns={'Begin Time (s)': 'Start','End Time (s)':'End','Delta Time (s)':'Duration'})
            duration_call_file = df1['Duration'].sum()
            duration = duration + duration_call_file
            #print(duration_call_file)
            if not os.path.exists(folder +'ready_to_go_csv'):
                os.makedirs(folder + 'ready_to_go_csv')
            
            filename = os.path.basename(txt)
            #print(filename)
            filename = filename.split(".")
            filename = filename[0]
            #print(filename)
            df1.to_csv(folder + 'ready_to_go_csv/{}.csv'.format(filename),index=False) 

        print(duration//60)
            
            
print('Converting files from folder... ')
print()
print("Duration Delphinus")           
convert_Raven_files(folder_Dd)
print("Duration Orca") 
convert_Raven_files(folder_Oo)
print("Duration Sousa") 
convert_Raven_files(folder_Sp)
print("Duration Tursiops") 
convert_Raven_files(folder_Ta)
print()
print('If you need to do it AGAIN, please delete all the files generated previously.')

#Soundscape: In this case, the file name is 'device.date.wav'

import pandas as pd
import os

Mooring_1 = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Mooring 1/txt/'
Mooring_2 = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Mooring 2/txt/'
Mooring_3 = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Mooring 3/txt/'
Mooring_4 = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Mooring 4/txt/'
Mooring_5 = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Mooring 5/txt/'
Mooring_6 = 'D:/Postdoc/1_Paper_Machine learning/2_WhistleID/WhistleID/Raw_data/Mooring 6/txt/'

def convert_Raven_files_soundscape(folder):
    total_duration = []
    for path, folders, files in os.walk(folder):        
        duration = 0
        
        for txt in files:
            df = pd.read_csv(folder+txt, sep="	", index_col=False)
            #print(df)
            df1 = df[['Begin Time (s)','End Time (s)','Delta Time (s)']]
            df1 = df1.rename(columns={'Begin Time (s)': 'Start','End Time (s)':'End','Delta Time (s)':'Duration'})
            duration_call_file = df1['Duration'].sum()
            duration = duration + duration_call_file
            #print(duration_call_file)
            if not os.path.exists(folder +'ready_to_go_csv'):
                os.makedirs(folder + 'ready_to_go_csv')
            
            filename = os.path.basename(txt)
            #print(filename)
            filename = filename.split(".")
            filename_device = filename[0]
            filename_date = filename[1]
            #print(filename)
            df1.to_csv(folder + 'ready_to_go_csv/{}.{}.csv'.format(filename_device,filename_date),index=False) 
            
            
        print(duration//60)
            
    
    
           
print('Converting files from folder... ')
print()
print("Duration Mooring 1")           
convert_Raven_files_soundscape(Mooring_1)
print("Duration Mooring 2") 
convert_Raven_files_soundscape(Mooring_2)
print("Duration Mooring 3") 
convert_Raven_files_soundscape(Mooring_3)
print("Duration Mooring 4") 
convert_Raven_files_soundscape(Mooring_4)
print("Duration Mooring 5") 
convert_Raven_files_soundscape(Mooring_5)
print("Duration Mooring 6") 
convert_Raven_files_soundscape(Mooring_6)
print()
print('If you need to do it AGAIN, please delete all the files generated previously.')


