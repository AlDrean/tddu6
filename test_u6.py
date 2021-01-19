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
        self.recentlist_status = 1


    def list_files(self):        
        #refactory ok
        self.onlyfiles = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        return (self.onlyfiles)
    
    def open_file(self,numFile):
        #no refactory nedeed
        self.selectFile = numFile
        f = open(self.directory+self.onlyfiles[self.selectFile], "r")
        self.recentList_add(self.selectFile,self.onlyfiles[self.selectFile])
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
            self.file_recents_num.insert(0,num)
        else:
            self.file_recents.insert(0,name)
            self.file_recents_num.insert(0,num)

    def blockRecentlist(self):
        self.recentlist_status = 0

    def freeRecentlist(self):
        self.recentlist_status = 1
    





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
        #esperada saida dos noems dos arquivos com o primeiro primeiro sendo o 6;
        program =Program(files_directory)
        program.list_files()
        program.open_file(5)
        program.open_file(6)

        expected = [6,5]
        out = program.recentList_num()
        assert out == expected
    
    def test_recentList_add_b(self):
        #esperada saida dos noems dos arquivos com o primeiro primeiro sendo o 5;
        #teste de acesso sucessivo de um arquivo
        program =Program(files_directory)
        program.list_files()
        program.open_file(5)
        program.open_file(6)
        program.open_file(5)

        out = program.recentList_num()

        expected = [5,6]
        assert out == expected


    

    def test_recentList_add_c(self):
        #teste para verifciar o limite do tamanho da fila e sua ciclicidade
        program =Program(files_directory)
        program.list_files()
        program.open_file(5)
        program.open_file(1)
        program.open_file(2)
        program.open_file(3)
        program.open_file(4)
        program.open_file(5)
        program.open_file(6)
        program.open_file(7)
        program.open_file(8)
        program.open_file(9)
        program.open_file(10)
        program.blockRecentlist()
        program.open_file(11)
        program.open_file(12)
        program.open_file(13)
        program.open_file(14)
        program.open_file(15)
        program.freeRecentList()
        program.open_file(16)
        program.open_file(17)

        out = program.recentList_num()        
        expected = [17,16,10,9,8,7,6,5,4,3]
        assert expected == out
        


