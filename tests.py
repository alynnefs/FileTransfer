import unittest
import shutil
import re
import os
from time import sleep, time


class scriptTest(unittest.TestCase):
    
    def setUp(self):
        self.regex = '(.*.txt)'

    def createFolder(self):
        """
        This method creates a folder named 'testes'
        """
        
        os.mkdir('testes')

    def createFiles(self):
        """
        This method creates 2 files .txt and 1 .rar
        """
        open('testes/1.txt', 'a').close()
        sleep(1)
        open('testes/2.rar', 'a').close()
        sleep(1)
        open('testes/3.txt', 'a').close()
        self.files = os.listdir('testes/')

    def cleanFiles(self):
        """
        This method deletes 'testes' folder
        """

        shutil.rmtree('testes')

    def cleanTarget(self):
        """
        This method deletes 'testes2' folder (target folder)
        """

        shutil.rmtree('testes2')

    def test_numberOfMatches(self):
        """
        This method tests the number of files matches
        """

        self.createFolder()
        self.createFiles()

        match = 0
        for file in self.files:
            m = re.search(self.regex, file)
            if m != None:
                match += 1

        self.cleanFiles()
        
        self.assertEqual(match, 2)

if __name__ == '__main__':
    unittest.main()
