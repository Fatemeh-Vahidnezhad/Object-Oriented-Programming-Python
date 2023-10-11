import os
class Filemanager:
    def __init__(self, filename, src, des):
        self.filename = filename
        self.src = src  #source folder
        self.des = des  #destination folder

    @property
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
des = r'filemanager_files\dest'
fl = Filemanager("test1.txt", src, des)
print(fl.path)
print(fl.exist())
fl.rename_copy('test2.txt')
fl.read_file('test2.txt')
