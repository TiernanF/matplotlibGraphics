# I dont know if I did this entirely right but I suppose it works
import queue

list = open('input queue-1-1.txt')
# Reads from text file
premium = []
standard = []
economy = []
# Establishes arrays
for line in list:
    priority, name = line.split()
    if priority == 'P':
        premium.append(name)
    elif priority == 'S':
        standard.append(name)
    elif priority == "E":
        economy.append(name)
# Appends names to arrays with proper priority
print("Premium Queue:", premium)
print("Standard Queue:", standard)
print("Economy Queue:", economy)
queue = []
while premium or standard or economy:
    queue.extend(premium[:3])
    del premium[:3]
    queue.extend(standard[:2])
    del standard[:2]
    queue.extend(economy[:1])
    del economy[:1]
# Takes the names from priority and adds them to the final queue and deletes them from array
print("Final order:", queue)
