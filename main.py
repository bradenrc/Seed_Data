import datetime,time
from datetime import timedelta
import random,os


#clear folder
outfolder = "./output/"
for file in os.listdir(outfolder):
    os.remove(outfolder + file)

#optional - singlefile
outall = open("alldata.csv", "w")

#define the date range of transactions for each account
#order: act#, begdate, enddate, list of possible target accounts for transfers
act = []
act.append(["12345", datetime.date(2007, 12, 1), datetime.date(2014, 12, 1), ["55554", "656547", "32325"]])
act.append(["55554", datetime.date(2008, 6, 1), datetime.date(2011, 7, 1), ["65874", "656547", "32325"]])
act.append(["656547", datetime.date(2008, 6, 1), datetime.date(2011, 7, 1), ["55554", "656547", "32325"]])
act.append(["32325", datetime.date(2008, 6, 1), datetime.date(2011, 7, 1), ["656547", "32325"]])
act.append(["65874", datetime.date(2008, 6, 1), datetime.date(2011, 7, 1), ["32325"]])


#create list of companies and functions to grab random company
company_list = open("company_names.txt", "r")
companies = []
for x in company_list:
    companies.append(x.replace("\n", ""))

def random_company():
    i = random.randint(1,1400)
    return companies[i]

#functions to create a random transaction
def create_trans(date):
    d_or_c = random.randint(-1,1)
    if d_or_c == 0: d_or_c = -1
    amnt = random.random() * random.randint(1,10000) * d_or_c
    return [date.isoformat(), random_company(), round(amnt,2)]

def create_random_transfer(date, act_from):
    #only return on in 1 random transactions
    if random.randint(1,10) == 1:
        amnt = random.random() * random.randint(1,10000) * -1
        for x in act:
            if x[0] != act_from:
                return [date.isoformat(), random.choice(x[3]), round(amnt,2)]

#        return [date.isoformat(), random_company(), round(amnt,2)]


def create_act_record(actnt):

    beg_date = actnt[1]
    end_date = actnt[2]
    current_date = beg_date

    statement_month = current_date.month
    statement_day = current_date.day
    statement_year = current_date.year

    current_file = "./output/{}_".format(actnt[0]) + "{}_{}_{}.csv".format(statement_month,statement_day,statement_year)
    of = open(current_file, "w")

    while current_date <= end_date:

        if statement_month != current_date.month: #start a new month, reset counters and open the next file
            statement_month = current_date.month
            statement_day = current_date.day
            statement_year = current_date.year
            current_file = "./output/{}_".format(actnt[0]) + "{}_{}_{}.csv".format(statement_month,statement_day,statement_year)
            of = open(current_file, "w")
        else:
            statement_day = current_date.day

        for trans_count in range(1,random.randint(1,8)):
            t = create_trans(current_date)
            of.writelines(','.join(str(e) for e in t) + "\n")

            trxfr = create_random_transfer(current_date, actnt[0])
            if trxfr != None:
                of.writelines(','.join(str(e) for e in trxfr) + "\n")
                #optional:
                outall.writelines(str(actnt[0]) + "," + ','.join(str(e) for e in trxfr) + "\n")
                print (str(actnt[0]) + "," + ','.join(str(e) for e in trxfr) + "\n")

            #optional:
            outall.writelines(str(actnt[0]) + "," + ','.join(str(e) for e in t) + "\n")

        current_date =  current_date + timedelta(days=1)


for a in act:
    create_act_record(a)

