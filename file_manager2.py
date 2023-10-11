import os
from datetime import date
import pathlib
class Filemanager:
    main_dir = 'CDR'
    dir_src = 'unprocess'
    dir_dest = 'processed'
    #os.mkdir(main_dir)
    #os.mkdir(dir_src)
    #os.mkdir(dir_dest)
    set_dir = r'CDR\unprocess\test'
    os.chdir(set_dir)
    def __init__(self):
        self.curpath = os.getcwd()
        print(self.curpath)
        self.new_filename = 'x_' + str(date.today().strftime("%Y%m%d")) + '.xlsx'
        print(self.new_filename)
        #self.path_src = os.path.join(self.main_dir, self.dir_src, '*.xlsx')
        self.filenames = pathlib.Path(self.curpath)
        #print(self.path_src)
        #self.filenames = glob.glob(self.path_src)
        #self.filenames = os.path.basename(self.path_src)
        print(list(self.filenames.iterdir()))
        #print(list(self.filenames.glob('test/*.csv')))

        print([item for item in self.filenames.iterdir() if item.is_file()])
        #self.path_dest = os.path.join(self.main_dir, self.dir_dest,filename)

        #self.filename = filename
        #self.src = src  #source folder
        #self.des = des  #destination folder
    def find_file(self):
        for item in self.filenames.iterdir():
            if item.is_file():
                if item == self.new_filename:
                    return 1
                else:
                    return 0

    '''@property
    def path(self):
        return  '{}/{}'.format(self.src,self.filename)

    def exist(self):
        if os.path.exists(self.path) == True:
            return 1
        else:
            return 0

    def rename_copy(self,new_name):
        if os.path.exists(self.path) == True:
            self.newname = des + '/' + new_name
            return os.rename(self.path,self.newname)
        else:
            print("file doesnot exist!")



    def read_file(self,new_name):
        #print(self.rename_copy(new_name))
        self.new_path = self.des + '/' +new_name
        f = open(self.new_path,'r')
        print(f.read())

src = r'filemanager_files'
des = r'filemanager_files\dest'''
fl = Filemanager()
print(fl.find_file())
'''print(fl.path)
print(fl.exist())
fl.rename_copy('test2.txt')
fl.read_file('test2.txt')'''
