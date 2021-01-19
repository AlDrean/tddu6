#test_capitalize.py 

import collections 

from os import listdir
from os.path import isfile, join
import pytest

class Program:

    def __init__(self, directory):
        self.directory = directory
        self.onlyfiles = ""
        self.selectFile = -1
        self.file_content = ""
        self.file_recents = []
        self.file_recents_num = []


    def list_files(self):        
        #refactory ok
        self.onlyfiles = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        return (self.onlyfiles)
    
    def open_file(self,numFile):
        #no refactory nedeed
        self.selectFile = numFile
        f = open(self.directory+self.onlyfiles[self.selectFile], "r")
        self.file_content = f.read()
        f.close()

        return self.file_content
    

    def recentList(self):
        return self.file_recents

    def recentList_num(self):
        return self.file_recents_num
    
    def recentList_add(self,num,name):
        if name in self.file_recents:
            self.file_recents.remove(name)
            self.file_recents.insert(0,name)

            self.file_recents_num.remove(num)
            self.file_recents_num.insert(0,name)
        else:
            self.file_recents.insert(0,name)
            self.file_recents_num.insert(0,num)



files_directory = 'files/'


class Teste:

    def test_listFiles(self,capsys):
        program =Program(files_directory)
        program.list_files()

        f = open ("tests/list_file.out","r")
        expect = (f.read())

        x = program.list_files()
        print(*x, sep = "\n") 
        captured = capsys.readouterr()
        

        assert (captured.out == expect)


    def test_openFile(self,capsys):
        program =Program(files_directory)
        program.list_files()

        program.open_file(5)
        f = open ("tests/open_file.out","r")
        expect = (f.read())
        
        selectedfile = 5
        out = program.open_file(selectedfile)
        
        assert out == expect

    def test_recentListEmpty(self,capsys):
        program =Program(files_directory)
        program.list_files()
        out = program.recentList()
        expected = []

        assert out == expected

    def test_recentList_add_a(self):
        #esperada saida dos noems dos arquivos com o primeiro primeiro sendo o 5;
        program =Program(files_directory)
        program.open_file(5)
        program.open_file(6)

        expected = [6,5]
        out = program.recentList_num()
        assert out == expected
    
    def test_recentList_add_b(self):
        #esperada saida dos noems dos arquivos com o primeiro primeiro sendo o 5;
        program =Program(files_directory)
        program.open_file(5)
        program.open_file(6)
        program.open_file(5)

        out = program.recentList_num()

        expected = [5,6]
        assert out == expected


