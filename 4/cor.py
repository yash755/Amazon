import csv

with open('batch1_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    for row in csv_reader:
        data = row
        # temp = []
        # for d in data:
        #     if d != '':
        #         temp.append(d)

        if line_count == 6:
            print (len(data))
            print (data)

        line_count = line_count+1

        if len(data) >= 6 and data[len(data)-1] != '':
            final_temp = []
            final_temp.append(data)

            with open('batch_final_1.csv', 'a+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(final_temp)

        else:
            final_temp = []
            final_temp.append(data)
            with open('batch_unfinal_1.csv', 'a+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(final_temp)
