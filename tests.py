import os
import re
import shutil
import unittest
from time import sleep, time


class scriptTest(unittest.TestCase):
    
    def setUp(self):
        self.regex = '(.*.txt)'

    def createDirectorySource(self):
        """
        This method creates a folder named 'testes'
        """
        
        os.mkdir('testes')

    def createDirectoryTarget(self):
        """
        This method creates a folder named 'testes2'
        """

        os.mkdir('testes2')

    def createFiles(self):
        """
        This method creates 2 files .txt and 1 .rar
        """
        open('testes/1.txt', 'a').close()
        sleep(0.01)
        open('testes/2.rar', 'a').close()
        sleep(0.01)
        open('testes/3.txt', 'a').close()
        self.files = os.listdir('testes/')

    def cleanSource(self):
        """
        This method deletes 'testes' folder (source folder)
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

        self.createDirectorySource()
        self.createFiles()

        match = 0
        for file in self.files:
            m = re.search(self.regex, file)
            if m != None:
                match += 1

        self.cleanSource()
        
        self.assertEqual(match, 2)

    def test_verifySource(self):
        """
        This method tests if the source folder was created
        """

        self.createDirectorySource()

        response = os.listdir()
        
        self.cleanSource()

        self.assertEqual('testes' in response, True)

    def test_verifyMoveFiles(self):
        """
        This method tests if the files were moved
        """

        target = 'testes2/'
        self.createDirectorySource()
        self.createDirectoryTarget()
        self.createFiles()

        for file in self.files:
            m = re.search(self.regex, file)
            if m != None:
                command = "%s%s" %('testes/', file)
                shutil.move(command, target)

        after = os.listdir('testes/')
        moved = os.listdir('testes2/')

        self.assertEqual(len(after), len(self.files)-2)
        self.assertEqual(len(moved), 2)

        self.cleanSource()
        self.cleanTarget()

    def test_theMostRecent(self):
        """
        This method tests if the file is the most recent
        """

        self.createDirectorySource()
        self.createDirectoryTarget()
        self.createFiles()

        time_newest = 0

        for file in self.files:
            time_file = os.path.getmtime('%s%s' %('testes/', file))            
            if time_file > time_newest \
               and re.match(self.regex, file):
                time_newest = time_file
                name_file = file
        
        self.cleanSource()
        self.cleanTarget()

        self.assertCountEqual(name_file, '3.txt')

    def test_theOldest(self):
        """
        This method tests if the file is the oldest
        """

        self.createDirectorySource()
        self.createDirectoryTarget()
        self.createFiles()

        time_oldest = time()

        for file in self.files:
            time_file = os.path.getmtime('%s%s' %('testes/', file))            
            if time_file < time_oldest \
               and re.match(self.regex, file):
                time_oldest = time_file
                name_file = file
        
        self.cleanSource()
        self.cleanTarget()

        self.assertCountEqual(name_file, '1.txt')


if __name__ == '__main__':
    unittest.main()
