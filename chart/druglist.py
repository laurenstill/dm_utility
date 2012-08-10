# formats information from the Drugs@FDA Data file into something more usable
# will be used primarily for predictive text selection on user input models for medication tracting and management
# also may be nice for drug information, but realistically need different db
# http://www.fda.gov/Drugs/InformationOnDrugs/ucm079750.htm 

import sys

def load_medications(filename):
	meds_dict = {}
	f = open(filename)
	line = " "
	# print f.read()
	for line in f:
		fields = line.split("\t")
		ApplNo = fields[0]
		ProductNo =	fields[1]
		Form = fields[2]
		Dosage = fields[3]
		ProductMktStatus = fields[4]
		TECode = fields[5]
		ReferenceDrug = fields[6]
		DrugName = fields[7]
		ActiveIngred = fields[8]

		meds = {
				"ApplNo": ApplNo,	
				"ProductNo": ProductNo,	
				"Form":	Form,
				"Dosage": Dosage,	
				"ProductMktStatus":	ProductMktStatus,
				"TECode": TECode,
				"ReferenceDrug": ReferenceDrug,	
				"DrugName":	DrugName,
				"ActiveIngred": ActiveIngred
			}		
		meds_dict[DrugName] = meds
	f.close()
	return meds_dict


def main():
	x = load_medications("druglist.txt")
	print x["RUBRATOPE-57"]
	# print x.keys()




if __name__ == "__main__":
    main()



