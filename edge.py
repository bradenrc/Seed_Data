import os
import itertools
import json
from collections import OrderedDict

"""
Desired output of data

[{
	"name": "flare.analytics.cluster.AgglomerativeCluster",
	"imports": [""]
},
{
	"name": "flare.analytics.cluster.CommunityStructure",
	"imports": [""]
},
{
	"name": "flare.actone.cluster.CommunityStructure",
	"imports": ["flare.analytics.cluster.AgglomerativeCluster"]
}
]

"""

with open("alldata.csv") as f:
    content = f.readlines()

accounts = []
for row in content:
    r_list = row.split(",")
    if not accounts.__contains__(r_list[0]):
        accounts.append(r_list[0])

payees = []
for row in content:
    r_list = row.split(",")
    if not payees.__contains__(r_list[2]) and accounts.__contains__(r_list[0]):
        payees.append(r_list[2])


all = []


for act in accounts:
    node = {}
    node["name"] = "flair.actcluster." + act
    node["imports"] = []

    for row in content:
        r_list = row.split(",")

        if accounts.__contains__(r_list[2]):
            payee = "flair.actcluster." + r_list[2]
        else:
            payee = r_list[2]

        if r_list[0] == act and not node["imports"].__contains__(payee):
            node["imports"].append(payee)
            print "Account node: ", r_list[0], payee
    all.append(node)

for py in payees:
    node = {}
    if accounts.__contains__(py):
        node["name"] = "flair.actcluster." + py
    else:
        node["name"] = py

    print "Payee Node: ", py
    all.append(node)

# data_str = json.dumps(all)
# print data_str

output = open("flare-imports.json", "w")
output.writelines(json.dumps(all))

"""
all = []

test = {}
test["name"] = "flare.analytics.cluster.AgglomerativeCluster"
test["imports"] = []
test["imports"].append("flare.analytics.cluster.CommunityStructure")
all.append(test)

test = {}
test["name"] = "flare.analytics.cluster.CommunityStructure"
test["imports"] = []
all.append(test)

test = {}
test["imports"] = []
test["name"] = "flare.analytics.cluster.3Structure"
all.append(test)

data_str = json.dumps(all)
print data_str
"""