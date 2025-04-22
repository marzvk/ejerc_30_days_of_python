#  clases

import statistics

ages = [
    31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37,
    31, 34, 24, 33, 29, 26
]
print('1-')

class Statistics:

    def __init__(self, dtata_list):
        self.data = dtata_list

    def count(self):
        return len(self.data)

    def sum(self):
        total = 0
        for i in self.data:
            total += i
        return total

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        rango = sorted(self.data)
        return (rango[-1] - rango[0])

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        return (statistics.mode(self.data), (statistics.Counter(
            self.data)).get(statistics.mode(self.data)))

    def std(self):
        return statistics.stdev(self.data)

    def var(self):
        return statistics.variance(self.data)

    def freq_dist(self):
        salida = []
        dic = statistics.Counter(self.data)
        largo = len(self.data)
        for a in dic:
            salida.append(((dic[a] * 100 / largo), a))
        salida.sort(key=lambda a: a[0], reverse=True)
        return salida


data = Statistics(ages)  # objeto data de la clase statistics

print('Count: ', data.count())
print('Sum: ', data.sum())
print('Min :', data.min())
print('Max: ', data.max())
print('Rango: ', data.range())
print('Mean/Average :', data.mean())
print('Median: ', data.median())
print('Mode :', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())

