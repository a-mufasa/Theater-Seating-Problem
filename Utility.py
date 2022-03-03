class FileProcessor:
    fileName = ""
    numLines = 0

    def __init__(self, input):
        self.fileName = input
        self.numLines = 0

    def readFile(self, input_file):
        contents = None
        try:
            with open(input_file, "r") as file_in:
                request = file_in.readline()
                while request is not None:
                    contents += " " + request
                    self.numLines += 1
        except FileNotFoundError:
            print("Input File Not Found")
        except IOError:
            print("IO Error")
        return contents

    def writeToFile(self, seat_allocation):
        try:
            with open("output.txt", "w+") as file_out:
                for res_id in seat_allocation:
                    file_out.write(str(res_id) + " " + ",".join(seat_allocation[res_id]) + "\n")
        except IOError:
            print("IO Error")