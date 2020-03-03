import random
import os

min_request = 50
max_request = 400

max_limit = 400

min_latency = 8
max_latency = 40

n_nodes = 10

graph = "graph{\n"
for i in range(0, n_nodes):
    request = random.uniform(min_request, max_request)
    limit = random.uniform(request, max_limit)
    graph += "\"" + str(i) + "[label=\"cpuOffloading - request:" + str("{0:.2f}".format(request)) + " - limit:"+ str("{0:.2f}".format(limit))
    graph += "\""
    graph += ", label=\"n" + str(i) + "\""
    graph += "];\n"

maxEdges = int((n_nodes * (n_nodes-1))/10)

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

f = open("graphs/depGraph.dot", "w")
f.write(graph)
f.close()
