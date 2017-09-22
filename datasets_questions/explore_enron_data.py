#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("- How many data points (people) are in the dataset? ",len(enron_data.keys()))
print("- For each person, how many features are available? ",len(enron_data["SKILLING JEFFREY K"].values()))

poi_count = 0
for k in enron_data:
    if enron_data[k]["poi"] == 1:
        poi_count += 1
print("- How many POIs are in the dataset? ",poi_count)

fo = open('../final_project/poi_names.txt','r')
fr = fo.readlines()
print("- How many POIs were there in total?", len(fr[2:]))
fo.close()

print("- What is the total value of the stock belonging to James Prentice?", enron_data["PRENTICE JAMES"]["total_stock_value"])

print("- How many email messages do we have from Wesley Colwell to persons of interest?", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print("- What’s the value of stock options exercised by Jeffrey K Skilling?", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print("- Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)?")
print("   - Lay",enron_data["LAY KENNETH L"]["total_payments"])
print("   - Skilling",enron_data["SKILLING JEFFREY K"]["total_payments"])
print("   - Fastow",enron_data["FASTOW ANDREW S"]["total_payments"])

quant_salary_count = 0
known_email_count = 0
for k in enron_data:
    if enron_data[k]["salary"] != "NaN":
        quant_salary_count += 1
    if enron_data[k]["email_address"] != "NaN":
        known_email_count += 1
print("- How many folks in this dataset have a quantified salary?",quant_salary_count)
print("- What about a known email address?",known_email_count)

nan_total_pay_count = 0
for k in enron_data:
    if enron_data[k]["total_payments"] == "NaN":
        nan_total_pay_count += 1
perc = nan_total_pay_count / len(enron_data.keys())
print("- What percentage of people in the dataset have NaN for their total payments?",round(perc,3))

poi_nan_total_pay_count = 0
for k in enron_data:
    if enron_data[k]["total_payments"] == "NaN" and enron_data[k]["poi"] == 1:
        poi_nan_total_pay_count += 1
perc = poi_nan_total_pay_count / len(enron_data.keys())
print("- What percentage of POIs in the dataset have NaN for their total payments?",round(perc,3))

