import pandas as pd
import tkinter as tk
import os
import platform
from tkinter.filedialog import askopenfilename

userhome = os.path.expanduser('~')
desktop = 'C:\\Users\\jfber\\OneDrive\\Desktop\\'
window = tk.Tk()
window.withdraw()

file_name = askopenfilename()
#add path to roster csv file
roster_df = pd.read_csv(file_name)

data = pd.DataFrame(roster_df)


data.drop(['StudMi', 'GrpGroupName', 'StaffLname',
          'StaffFname', 'StaffMi', 'DormId', 'Resident', 'StudentGroupGroupId',
           'StaffId', 'GrpGroupTypeCd', 'SortBy', 'LOS'], axis=1, inplace=True)
# data['FullName'] = data['StudentFName'] + ' ' + data['StudentLName']
# data.drop(['StudentFName', 'StudentLName'], axis=1, inplace=True)
data = data.sort_values('BehaviorDt')
data.to_csv("Current_IncVol_Cleaned.csv")