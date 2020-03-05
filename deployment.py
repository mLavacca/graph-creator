import random
import math
import os

def getRandomColor():
    letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    color = '#'

    for i in range(0, 6, 1):
        color += letters[random.randint(0, 15000) % 16]
        
    return color

min_request = 50
max_request = 300

max_limit = 400

min_latency = 8
max_latency = 30

n_nodes = 12

color = getRandomColor()

graph = "graph{\n"
graph += "\tnode[style=\"filled\", color=\"" + color + "\"]\n"

for i in range(0, n_nodes):
    request = random.uniform(min_request, max_request)
    limit = random.uniform(request, max_limit)
    graph += "\t" + str(i) + "[label=\"cpuOffloading - request:" + str("{0:.2f}".format(request)) + " - limit:"+ str("{0:.2f}".format(limit))
    graph += "\""
    graph += ", label=\"n" + str(i) + "\""
    graph += "];\n"

maxEdges = int((n_nodes * (n_nodes-1))/6)

for i in range(0, maxEdges):
    k = random.randint(0, n_nodes-1)
    l = k

    while (k == l):
        l = random.randint(0, n_nodes-1)
    
    latency = random.uniform(min_latency, max_latency)
    graph += "\t" + str(k) + " -- " + str(l) + "[label=\"latency - value:" + str("{0:.2f}".format(latency)) + "\""
    graph += ", label=\"n" + str(k) + "-n" + str(l) + "\""
    graph += "];\n"
            
graph += "}\n"

f = open("exp_graphs/depGraph2.dot", "w")
f.write(graph)
f.close()




