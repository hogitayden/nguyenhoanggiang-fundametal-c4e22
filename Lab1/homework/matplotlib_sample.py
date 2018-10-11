from matplotlib import pyplot

#prepare data
machine_counts = [18, 4, 2]

#prepare labels
machine_labels = ['PC', 'MAC', 'Linux']

#draw pie
pyplot.pie(machine_counts, labels = machine_labels, autopct='%.1f%%', shadow= True, explode=[0, 0.2, 0])
pyplot.title('Laptop usage in class C4E22')
pyplot.axis('equal')
#show
pyplot.show()