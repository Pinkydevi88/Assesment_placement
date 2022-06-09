import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
fh = open("example.txt", 'w+')
fh.write("This is a placement assignment")
logging.info("This is a placement assignment")
fh.close()


class file:
    def __init__(self, ff):
        logging.info("Creating file instance variable")
        self.ff = ff

    def readfile(self):
        logging.info("executing read method")
        try:
            with open(f"{self.ff}", 'r') as f:
                file2 = f.read()
                return file2
        except FileNotFoundError as e:
            logging.error("Error occured while opening the file ")
            logging.exception(f"Error is {e}")

    def writefile(self):
        logging.info("executing write method")
        try:
            with open(f"{self.ff}", 'w') as f:
                file2 = f.write(lines)
        except FileNotFoundError as e:
            logging.error("Something is going wrong")
            logging.exception(f"Error is {e}")


class file1(file):
    def read(self):
        pass


ff = r'example.txt'
lines = 'Placement should be replaced by screening.'
logging.info('Placement should be replaced by screening.')
read_write = file1(ff)
read_write.writefile()
read_write.readfile()