import os
import shutil
import re
from time import sleep, time
import yaml

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

    def move(self):
        """
        This method moves files based on the filename name and
        the operation mode
        """

        print("Searching files")
        with open('config_file.yaml', 'r') as f:
            doc = yaml.load(f)

        source = doc["source"]
        target = doc["target"]

        files = os.listdir(source)

        if doc["mode"] == 1:
            """
            This mode moves all file matches
            """

            for file in files:
                if self.match(doc['regex'], file):
                    command = "%s%s" %(source, file)
                    shutil.move(command, target)
                    print("%s was moved." %file)

        sleep(doc["period"])

if __name__ == '__main__':
    while True:
        moveFiles().move()