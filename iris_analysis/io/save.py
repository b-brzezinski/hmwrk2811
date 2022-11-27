import csv

def save_csv(filaname,data_lst):
    with open(filaname, 'w', newline='') as csv_file:
        writer=csv.writer(csv_file)
        for ele in data_lst:
            writer.writerow(ele)

if __name__ == '__main__':
    save_csv('test.csv',[[0,0,1],[5,32,3],[2,3,4]])
