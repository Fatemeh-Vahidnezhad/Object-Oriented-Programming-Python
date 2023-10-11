import os
from datetime import date
import pathlib
import pandas as pd


class Filemanager:
    main_dir = 'CDR'
    dir_src = 'unprocess'
    dir_dest = 'processed'
    curtpath = os.getcwd()

    # set_dir = r'CDR\unprocess'
    # os.chdir(set_dir)

    def __init__(self):
        self.set_dir = os.path.join(self.main_dir, self.dir_src)
        print(os.getcwd())
        os.chdir(self.set_dir)
        print(os.getcwd())
        self.des = os.path.join(self.curtpath, self.main_dir, self.dir_dest)

        # print(self.des)
        # print(os.getcwd())
        self.create_date_cnt = None
        self.create_date_cnt_new = None

        self.new_filename = 'Subs_Profile_Report_' + str(date.today().strftime("%Y%m%d")) + '.csv'
        # print(self.new_filename)
        self.filenames = pathlib.Path(os.getcwd())  # it shows the list of files and directories
        # print(list(self.filenames.iterdir()))
        # print([os.path.basename(item) for item in self.filenames.iterdir() if item.is_file()])

    def match_filename(self):
        for item in self.filenames.iterdir():
            if item.is_file():
                if os.path.basename(item) == self.new_filename:
                    return 1
                else:
                    return 0

    def aggregate_data(self):

        df = pd.read_csv(self.new_filename)
        # print(df.head())
        self.create_date_cnt = df['CREATE_DATE'].value_counts().rename_axis('unique_values').reset_index(name='counts')
        os.chdir(self.des)
        print('des:', os.getcwd())
        source_dataset = pd.read_csv('agg.csv')
        self.create_date_cnt_new = pd.concat([self.create_date_cnt, source_dataset], ignore_index=True)

        self.create_date_cnt_new.to_csv('agg.csv')


fl = Filemanager()
# fl.des
# print(fl.match_filename())
fl.aggregate_data()
'''print(fl.path)
print(fl.exist())
fl.rename_copy('test2.txt')
fl.read_file('test2.txt')'''
