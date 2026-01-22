#!/usr/bin/env python
from pprint import pprint


# Modify this function signature and fill in the details
def parse_line()
    pass


###Sample code below
# Initialize string with sample data for temporary testing
#readin = "1	1041648	263158	G	T	.	.	AF_ESP=0.00500;AF_EXAC=0.00488;AF_TGP=0.00240;ALLELEID=249308;CLNDISDB=MedGen:C3808739,OMIM:615120|MedGen:CN169374|MedGen:CN517202;CLNDN=Myasthenic_syndrome,_congenital,_8|not_specified|not_provided;CLNHGVS=NC_000001.11:g.1041648G>T;CLNREVSTAT=criteria_provided,_multiple_submitters,_no_conflicts;CLNSIG=Benign/Likely_benign;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=AGRN:375790;MC=SO:0001583|missense_variant;ORIGIN=1;RS=138031468"

# Split data into list
#txt = readin
#x = txt.split(";")
#print(x)

# Create dict from list
#my_dict = {item.split('=')[0]: item.split('=')[1] for item in x}

# Just prints out the dictionary entries for easy viewing
#print(my_dict)
#for key, value in my_dict.items():
#    print(key, "-", value)

# Checks if allele frequency is at threshold
#float(my_dict["AF_EXAC"]) < 0.0001

# Split the diseases into its own string
#diseases = my_dict["CLNDN"]
#diseases

# Pipe delimiter separates into list entries
#disease_list = diseases.split("|")
#disease_list

# Add items to our list to pass back to calling function, removing not specified and not provided 
#to_add = []
#for item in disease_list:
#    if item != "not_specified" and item != "not_provided":
#        to_add.append(item)
#print(to_add)



# Modify this function signature and fill in the details
def read_file()
    pass


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))