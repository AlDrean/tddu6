#test_capitalize.py 

import collections 

from os import listdir
from os.path import isfile, join
import pytest

class Program:

    def __init__(self, directory):
        self.directory = directory
        self.onlyfiles = ""

    def list_files(self):        
        self.onlyfiles = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        print(*self.onlyfiles, sep = "\n") 
        





files_directory = 'files/'
program =Program(files_directory)
program.list_files()
testCase = ''

class Teste:

    def test_listFiles(self,capsys):
        f = open ("tests/list_file.out","r")
        expect = (f.read())

        program.list_files()
        captured = capsys.readouterr()
        

        assert (captured.out == expect)




