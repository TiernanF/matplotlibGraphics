import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 8, 4, 4]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['coral', 'mediumspringgreen', 'skyblue', 'plum' ]
explodelist = [0.1, 0.1, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
    	explode = explodelist, startangle = 150)
plot.axis('equal')
plot.savefig('piechart.png')
