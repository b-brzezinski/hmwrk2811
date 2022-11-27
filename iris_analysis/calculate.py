import statistics

def calculate_stats(data):
    avg=[statistics.mean(data[::][i]) for i in range(len(data[0]))]
    med=[statistics.median(data[::][i]) for i in range(len(data[0]))]
    std=[statistics.stdev(data[::][i]) for i in range(len(data[0]))]
    return [avg,med,std]


    