import sys
from Utility import FileProcessor
from Theater import MovieTheater


def main():
    if len(sys.argv) > 0:
        file = FileProcessor(sys.argv[0])
        mt = MovieTheater()
        try:
            with open(sys.argv[1], "r") as f:
                temp = f.readline()
                while temp != "":
                    output = mt.reserveSeats(temp)
                    if output == 1:
                        print("Cannot process request", temp[0:4],  "due to invalid number of seats")
                    if output == -1:
                        print("Cannot process request", temp[0:4],  "due to insufficient seats")
                    temp = f.readline()

                file.writeToFile(mt.getAllocation())
                mt.printTheater()
                mt.TheaterStats()
        except FileNotFoundError:
            print("Input File Not Found.")
            exit()
        except IOError:
            print("IO Error")
        except Exception as e:
            print(e, "Exception Occurred")


if __name__ == "__main__":
    main()
