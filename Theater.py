from collections import OrderedDict


class MovieTheater:
    rows, cols = 10, 20  # defined boundaries for the theatre
    safety_buffer = 4  # value - 1 = actual buffer (allows for iteration)
    maxSeats = 200 // safety_buffer  # maximum seats (accounts for social distancing)
    seat_allocation = OrderedDict()  # maintains insertion order, better for output
    seats = [[None for _ in range(20)] for _ in range(10)]  # Initially setting all the seats to none(empty)
    availableSeats = [20 for _ in range(10)]  # Setting all the seats initially as available.
    satisfaction, totalCustomers = 0, 0  # Set initial req and customers to 0

    def reserveSeats(self, reservation):
        user_input = reservation.split()
        if not user_input:  # check for handling blank lines in the input file.
            return -1
        res_id = user_input[0]  # Reservation ID
        num_booked = int(user_input[1])  # Number of seats to be booked per group.
        group = num_booked

        if num_booked > 0:
            if self.maxSeats >= num_booked:
                self.totalCustomers += num_booked
                if group > 20:   # check and break up groups larger than 20 people
                    while group > 20:
                        self.allocate(res_id, 20)
                        group -= 20
                    output = self.allocate(res_id, group)
                else:
                    output = self.allocate(res_id, group)

                return output
            else:  # number of seats booked by a group must be < maximum seats
                return -1
        else:  # number of seats booked by a group must be > 0
            return 1

    def allocate(self, res_id, seatsToBook):
        row_iter = 1  # increments row # to be filled
        fill_below = True
        r = (self.rows // 2) - 1
        while 0 <= r < self.rows:
            if self.availableSeats[r] >= seatsToBook:
                c = 0
                while c < 20 and seatsToBook > 0:
                    if self.seats[r][c] is None:
                        self.seats[r][c] = res_id
                        if res_id in self.seat_allocation:
                            self.seat_allocation[res_id].append(chr(r + 65) + str(c + 1))  # ASCII conversion
                        else:
                            self.seat_allocation[res_id] = [chr(r + 65) + str(c + 1)]

                        self.availableSeats[r] -= 1
                        self.maxSeats -= 1
                        seatsToBook -= 1
                        self.satisfaction += 1
                    c += self.safety_buffer  # increment column by social distance buffer
            if fill_below:  # start filling up the row behind current
                r += row_iter
                row_iter += 1
                fill_below = False
            else:  # alternate to filling row above
                r -= row_iter
                row_iter += 1
                fill_below = True

        if seatsToBook == 0:
            return 0
        else:  # we need to allocate seats to people who don't fit perfectly in one row; exceed 1 row
            i = (self.rows // 2) - 1
            while 0 <= i < self.rows:
                if self.availableSeats[i] > 0:
                    j = (self.cols // self.safety_buffer) - 1  # max # of seats allocated in this loop; col identifier
                    while self.seats[i][j] is None:
                        self.seats[i][j] = res_id
                        if res_id in self.seat_allocation:
                            self.seat_allocation[res_id].append(chr(i + 65) + str(j + 1))
                        else:
                            self.seat_allocation[res_id] = [chr(i + 65) + str(j + 1)]

                        seatsToBook -= 1
                        self.maxSeats -= 1
                        self.availableSeats[i] -= 1
                        j -= 1
                if fill_below:
                    i += row_iter
                    row_iter += 1
                    fill_below = False
                else:
                    i -= row_iter
                    row_iter += 1
                    fill_below = True
            return 0

    def getAllocation(self):
        return self.seat_allocation

    def TheaterStats(self):
        print("Statistics:")
        print("Total number of reservation requests: ", len(self.seat_allocation))
        print("Total Customers :", self.totalCustomers)
        print("Total number of Satisfied Customers: ", self.satisfaction)
        if (self.totalCustomers > 0):
            print("% of Customers Satisfied :", round((self.satisfaction * 100 / self.totalCustomers), 3))
        print("% Theater Utilization: ", self.satisfaction / 2)  # 200 seats total

    def printTheater(self):
        for row in range(10):
            print(chr(row + 65))
            for col in range(20):
                print(self.seats[row][col], " ", end="")
            print()
        print()

