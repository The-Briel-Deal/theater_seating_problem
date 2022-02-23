import os
import sys

class MovieTheaterChallenge:
    def __init__(self) -> None:
        self.inputPath = sys.argv[1]
        self.inputReservations = self.getInput()
        self.parsedReservations = self.parseReservations()
        self.seating = self.createSeating()
        self.reservationsSeating = []
        

    def createSeating(self) -> object:
        # Creates and returns seating matrix with all chairs unfilled (0)
        seating = []
        for x in range(10):
            seating.append([])
            for y in range(20):
                seating[x].append(0)
        return seating

    def getInput(self) -> object:
        # Gets input in input.txt and returns it as an array of each line
        with open(self.inputPath, 'r') as inputFile:
            return inputFile.readlines()
    
    def setOutput(self, output: str) -> None:
        # Takes in output as a string and writes it to output.txt
        with open('output.txt', 'w') as outputFile:
            outputFile.write(output)

    def parseReservations(self) -> object:
        # Parses reservation to JSON
        parsedReservations = []
        for reservation in self.inputReservations:
            reservationNumber = int(reservation[1:4])
            reservationPeople = int(reservation[4:])
            parsedReservations.append({"Number":reservationNumber,
                                       "People": reservationPeople})
        return parsedReservations
    def seatingAlgorithm(self) -> None:
        # Seats everyone and outputs there seats using setOutput method
        for reservation in self.parsedReservations:
            seatPositions = []
            reservationNumber = reservation["Number"]
            reservationPeople = reservation["People"]
            targetColumn = ((reservationNumber % 10) - 1)
            targetLeft = True if reservationNumber % 2 == 1 else False
            if targetLeft:
                seatTaken = True
                currentSeat = 0
                if self.seating[targetColumn][currentSeat] == 0:
                    seatTaken = False
                while seatTaken:
                    if self.seating[targetColumn][currentSeat] == 1:
                        currentSeat += 1
                    else:
                        currentSeat += 3
                for i in range(reservationPeople):
                    self.seating[targetColumn][currentSeat+i] = 1
                    seatPositions.append({"col": (currentSeat+i), "row": targetColumn})
            else:
                seatTaken = True
                currentSeat = -1
                if self.seating[targetColumn][currentSeat] == 0:
                    seatTaken = False
                while seatTaken:
                    if self.seating[targetColumn][currentSeat] == 1:
                        currentSeat -= 1
                    else:
                        currentSeat -= 3
                for i in range(reservationPeople):
                    self.seating[targetColumn][currentSeat-i] = 1
                    seatPositions.append({"col": (currentSeat-i), "row": targetColumn})
            
            seatsInReservation = []
            for position in seatPositions:
                row = position["row"]
                col = (position["col"] % 20) + 1
                rowLetter = chr(row+65)
                seatPos = f"{rowLetter}{col}"
                seatsInReservation.append(seatPos)
            reservationPrefix = f"R{str(reservationNumber).rjust(3, '0')} "
            reservationSuffix = ",".join(seatsInReservation)
            reservationLine = reservationPrefix + reservationSuffix
            self.reservationsSeating.append(reservationLine)
        self.setOutput("\n".join(self.reservationsSeating))
            
if len(sys.argv) == 2:
    movieTheaterChallenge = MovieTheaterChallenge()
    movieTheaterChallenge.seatingAlgorithm()
    print(f"{os.getcwd()}/output.txt")
else:
    print("Please input the filepath as a parameter.")

