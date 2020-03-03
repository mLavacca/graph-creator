import random
import os

max_amount = 1000
min_amount = 500

minR = 0
minL = 0

min_cost = 0.4
max_cost = 1

min_latency = 4
max_latency = 20

n_nodes = 500
graph = "graph{\n"
for i in range(0, n_nodes):
    amount = random.uniform(min_amount, max_amount)
    maxL = amount
    maxR = amount
    cost = random.uniform(min_cost, max_cost)
    graph += "\t" + str(i) + "[label=\"cpu - amount:" + str("{0:.2f}".format(amount)) + " - cost:"+ str("{0:.2f}".format(cost))
    graph += " - minR:" + str(minR) + " - maxR:" + str("{0:.2f}".format(maxR)) + " - minL:" + str(minL) + " - maxL:" + str("{0:.2f}".format(maxL))
    graph += "\""
    graph += ", label=\"n" + str(i) + "\""
    graph += "];\n"

for i in range(0, n_nodes):
    for j in range(0, i):
        latency = random.uniform(min_latency, max_latency)
        cost = random.uniform(min_cost, max_cost)
        graph += "\t" + str(i) + " -- " + str(j) + "[label=\"latency - value:" + str("{0:.2f}".format(latency)) + " - cost:" + str("{0:.2f}".format(cost)) + "\""
        graph += ", label=\"n" + str(i) + "-n" + str(j) + "\""
        graph += "];\n"

graph += "}\n"

f = open("graphs/fedGraph.dot", "w")
f.write(graph)
f.close()
