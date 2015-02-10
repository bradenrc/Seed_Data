import os
import itertools
import datetime

"""
Desired output of data
       [ 'A', 'X', 5 ],
       [ 'A', 'Y', 7 ],
       [ 'A', 'Z', 6 ],
       [ 'B', 'X', 2 ],
       [ 'B', 'Y', 9 ],
       [ 'B', 'Z', 4 ]
"""

with open("alldata.csv") as f:
    content = f.readlines()

accounts = []
for row in content:
    r_list = row.split(",")
    if not accounts.__contains__(r_list[0]):
        accounts.append(r_list[0])

transfers = []

for act in accounts:
    for row in content:
        r_list = row.split(",")
        to = r_list[2]
        if act == r_list[0] and accounts.__contains__(to):
            transfers.append([act,to,r_list[3].replace("\n","")])


data = ""

keyfunc = lambda t: (t[0], t[1])
transfers.sort(key=keyfunc)
for key, rows in itertools.groupby(transfers, keyfunc):
    ks = str(key).split(",")
    frm = ks[0].replace("(", "")
    to = ks[1].replace(")", "")
    data = data + "[" + frm + "," + to + "," + str(sum(float(r[2]) for r in rows)*-1) + "],\n"

#print data

output = open("sankey_html_template.txt", "r").read()
output = output.replace("##data##", data)
output_file = open("sankey_report.html", "w")
output_file.writelines(output)



