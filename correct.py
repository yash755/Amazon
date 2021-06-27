import csv

with open('main.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        data = row
        temp = []
        for d in data:
            if d != '':
                temp.append(d)


        if len(temp) == 6:
            a1 = temp[4]
            a2 = temp[5]

            temp[4] = ''
            temp[5] = a1
            temp.append(a2)



        final_temp = []

        final_temp.append(temp)

        with open('main1.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(final_temp)

