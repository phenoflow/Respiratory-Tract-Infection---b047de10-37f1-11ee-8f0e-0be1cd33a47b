# Rebecca M Joseph, Mohammad Movahedi, William G Dixon, Deborah PM Symmons, 2023.

import sys, csv, re

codes = [{"code":"A15.3","system":"icd10"},{"code":"A15.9","system":"icd10"},{"code":"A16.9","system":"icd10"},{"code":"J12.9","system":"icd10"},{"code":"J15.9","system":"icd10"},{"code":"J18","system":"icd10"},{"code":"J18.0","system":"icd10"},{"code":"J18.1","system":"icd10"},{"code":"J18.2","system":"icd10"},{"code":"J18.8","system":"icd10"},{"code":"J18.9","system":"icd10"},{"code":"J20.8","system":"icd10"},{"code":"J20.9","system":"icd10"},{"code":"J21.8","system":"icd10"},{"code":"J21.9","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('respiratory-tract-infection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["respiratory-tract-infection-specified---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["respiratory-tract-infection-specified---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["respiratory-tract-infection-specified---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
