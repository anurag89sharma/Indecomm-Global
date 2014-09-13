import sys
import csv
import pprint
from collections import OrderedDict

"""
Class for finding the maximum share price of each company.
The input is provided using a input-file where each row contains
the year, month and the price of share of each company at that time_period
of year.
"""
class Company_Shares(object):
    def __init__(self,fname):
        """
        Constructor of the class Company_Shares. It takes the given input file and 
        initializes the variables for finding the max share price for each company
        This method takes the single input parameter -- the input file containing the 
        share price of various companies, for each month and year
        """
        self.filename = fname
        # ordered dictionary for mapping the company name to the index of max_share_companies list
        # for example if the company has a index 'i' as its value then its corresponding information
        # of maximum share price and time(months and year) will be find in the "i-th" index of the list
        # max_share_companies
        self.company_index = OrderedDict()
        # This is basically a list of list where a single element of the list contain 2 parts- one the
        # maximum share pirce of the corresponding company, 2nd is a list of tuples storing the month and
        # year for which the maximum share price is recorded. Their cab be multiple month and year for 
        # which the share price is maximum for a particular company
        self.max_share_companies = []

    def create_ds(self,row):
        """
        Method for initilizing the data structure for holding the company names, its maximum share price
        and the time (month and year) during which the company share was at its maximum value. The maximum
        share price of every company is initialized to zero
        """
        companies = row[2:]
        for i in xrange(0,len(companies)):
            self.company_index[companies[i]] = i
            self.max_share_companies.append([0,[]])

    def process_row(self,row):
        """
        Method for processing a single row parsed by the "read_file" function. For each row the current
        month and year is extracted and then for every company, the current share price of the company 
        is matched with the max-share-price of that company(stored in max_share_companies[i][0], where i 
        is the company index). If current share price is greater than the max-share-price, the max-share-price
        is updated along with the current value of year and month. If current share price is equal to 
        max-share-price then the list containing the year and month is appended with the current month 
        and year values (year and month are updated/ added as a single entry using tuple)
        """
        year = row[0]
        month = row[1]
        prices = row[2:]
        for i in xrange(0,len(prices)):
            cur_price = int(prices[i])
            if self.max_share_companies[i][0] < cur_price:
                self.max_share_companies[i][0] = cur_price
                self.max_share_companies[i][1] = [(year,month)]
            elif self.max_share_companies[i][0] == cur_price:
                self.max_share_companies[i][1].append((year,month))
            else:
                pass

    def read_file(self):
        """
        Method for reading the given input file. A single line of the file is parsed and 
        is sent for processing. It uses two methos namely "create_ds" and "process_row"
        """
        index = 0
        try:
            f = open(self.filename, 'rb')
        except IOError:
            print "Could not read file:", self.filename
            sys.exit()

        with f:
            reader = csv.reader(f)
            for row in reader:
                if index == 0:
                    self.create_ds(row)
                    index += 1
                else:
                    self.process_row(row)
    
    def execute(self):
        """
        Wrapper function to find the maximum share price of each company. It first executes the read_file
        function and then outputs for each Company price, year and month in which the share price was highest.
        """
        self.read_file()
        print "Company\t\tPrice\tTime" 
        for key, val in self.company_index.iteritems():
            company_name = key
            price = self.max_share_companies[val][0]
            time_period = []
            for items in self.max_share_companies[val][1]:
                time = '%s, %s' % (items[0], items[1])
                time_period.append(time)
            time_period = '; '.join(time_period) 
            print  '%s\t%s\t%s' % (company_name, price, time_period)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'input.txt'
    obj = Company_Shares(filename)
    obj.execute()