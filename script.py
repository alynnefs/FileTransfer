import errno
import os
import re
import shutil
import yaml
from time import sleep, time

class moveFiles():
    """
    This class moves files based on the filename name
    """

    def match(self, regex, file):
        """
        This method verifies the match.
        Return True if it matches and False if it doesn't match.
        """

        m = re.search(regex, file)
        return True if m != None else False

    def move(self, source, file, target):
        command = "%s%s" %(source, file)
        try:
            shutil.move(command, target)
            print("%s was moved." %file)
        except IOError as e:
            if e.errno != errno.ENOENT:
                print(e)
            os.makedirs(target)
            shutil.move(command, target)
            print("%s was moved." %file)

    def main(self):
        """
        This method moves files based on the filename name and
        the operation mode
        """

        with open('config_file.yaml', 'r') as f:
            doc = yaml.load(f)

        print("Searching files") if doc["mode"] == 1 or doc["mode"] ==  2 else print("Incorrect mode")

        source = doc["source"]
        target = doc["target"]

        try:
            files = os.listdir(source)
        except IOError as e:
            if e.errno != errno.ENOENT:
                print(e)
            os.makedirs(source)
            files = os.listdir(source)
            print("Directory %s was created." %source)

        if doc["mode"] == 1:
            """
            This mode moves all file matches
            """

            for file in files:
                if self.match(doc['regex'], file):
                    self.move(source, file, target)

        elif doc["mode"] == 2 and doc["recent"] == True:
            """
            This mode moves the most recent file match in each period
            """

            time_newest = 0
            name_file = ""
            for file in files:
                time_file = os.path.getmtime('%s%s' %(source, file))
                if time_file > time_newest \
                   and self.match(doc['regex'], file):
                    time_newest = time_file
                    name_file = file
            if name_file != "":      
                self.move(source, name_file, target)

        elif doc["mode"] == 2 and doc["recent"] == False:
            """
            This mode moves the oldest file match in each period
            """

            time_oldest = time()
            name_file = ""
            for file in files:
                time_file = os.path.getmtime('%s%s' %(source, file))
                if time_file < time_oldest \
                and self.match(doc['regex'], file):
                    time_oldest = time_file
                    name_file = file
            if name_file != "":      
                self.move(source, name_file, target)

        sleep(doc["period"])

if __name__ == '__main__':
    while True:
        moveFiles().main()