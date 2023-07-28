#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a python program that simulates a simple network topology 


# In[ ]:


#with at least five nodes. Calculate and display the shortest path 


# In[ ]:


#between two nodes using Dijkstra's algorithm


# In[25]:


#Creating an Adjacency List with varying lengths (m)
NetTop = {
    'Switch A': {'Router A': 12, 'Computer A': 5, 'Computer B': 7, 'Switch B': 20},
    'Computer A':{'Switch A': 5, 'Computer B': 5},
    'Computer B':{'Switch A': 7, 'Computer A': 5},
    'Switch B':{'Router A': 4, 'Computer C': 4, 'Computer D': 6, 'Switch A': 20},
    'Computer C':{'Switch B': 4, 'Computer D': 6},
    'Computer D':{'Switch B': 6, 'Computer C': 6},
    'Router A': {'Switch A': 12, 'Switch B': 4}
}

def NetTopAdjList(net):
    for node, adj_nodes in net.items():
        connections = []
        for adj_node, length in adj_nodes.items():
            connections.append(
                f"{adj_node} (length: {length})"
            )
        print(f"{node} is connected to {', '.join(connections)}.")
        
NetTopAdjList(NetTop)


# In[26]:


#Represent the adjacency list in the form of a toplogy
import networkx as nx
import matplotlib.pyplot as plt

N = nx.Graph()

for node, neighbors in NetTop.items():
    for neighbor in neighbors:
        N.add_edge(node, neighbor)
        
nx.draw(N, with_labels=True)
plt.show()


# In[ ]:


#Writing dijkstra's algorithm pertinent to this topology
import sys

def dijkstra(NetTop, Device1, Device2):
    shortest_distance = {node:
                   (None, sys.maxsize) for node in NetTop
               }
    shortest_distance[Device1] = (None, 0)
    
    unknown_nodes = list(NetTop)
    
    while unknown_nodes:
        current_node = min([(node, shortest_distance[node][1]) 
                            for node in unknown_nodes], key=lambda x: x[1])[0]
        unknown_nodes.remove(current_node)
        
        if shortest_distance[current_node][1] == sys.maxsize:
            break
            
        for neighbor, distance in NetTop[current_node].items():
            alt_distance = shortest_distance[current_node][1] + distance
            if alt_distance < shortest_distance[neighbor][1]:
                shortest_distance[neighbor] = (current_node, alt_distance)
                
    path = []
    while Device2 is not None:
        path.append(Device2)
        next_node = shortest_distance[Device2][0]
        Device2 = next_node
    path = path[::-1]
    
    return path, shortest_distance[path[-1]][1]

while True:
    Device1 = input('Enter the source node: ')
    if Device1 not in NetTop:
        print(f"Node '{Device1}' is not in the network. Please reference the topology and enter a valid node.")
        continue
    break

while True:
    Device2 = input('Enter the source node: ')
    if Device2 not in NetTop:
        print(f"Node '{Device2}' is not in the network. Please reference the topology and enter a valid node.")
        continue
    break

path, distance = dijkstra(NetTop, Device1, Device2)

print(f"Shortest path: ", " -> ".join(path))
print(f"Minimum distance: ", distance)


# In[ ]:





# In[ ]:




