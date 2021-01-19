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

    def list_files(self):        
        self.onlyfiles = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        return (self.onlyfiles)
    
    def open_file(self,numFile):
        self.selectFile = numFile
        f = open(self.directory+self.onlyfiles[self.selectFile], "r")
        self.file_content = f.read()
        f.close()
        return self.file_content
    




files_directory = 'files/'

program =Program(files_directory)
program.list_files()
program.open_file(5)
testCase = ''

class Teste:

    def test_listFiles(self,capsys):
        f = open ("tests/list_file.out","r")
        expect = (f.read())

        x = program.list_files()
        print(*x, sep = "\n") 
        captured = capsys.readouterr()
        

        assert (captured.out == expect)


    def test_openFile(self,capsys):
        f = open ("tests/open_file.out","r")
        expect = (f.read())
        
        selectedfile = 5
        out = program.open_file(selectedfile)
        
        assert out == expect


