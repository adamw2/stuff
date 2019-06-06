import os
import glob
import pandas as pd

os.chdir("/Users/adamw/Documents/emails")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine stuff into one csv
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export it
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
