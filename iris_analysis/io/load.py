import csv

def load_csv(filename):
    temp_lst=[]
    with open(filename, 'r', newline='') as csv_file:
        reader=csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        for line in reader:
            temp_lst.append(line)
    col_names=temp_lst[0][0:3]
    data_lst=[ele[0:3] for ele in temp_lst[1::]]
    return col_names, data_lst

if __name__ == '__main__':
    load_csv('D:\\python\\NPD\\pd2811_package\\modules\\data\\iris.csv')