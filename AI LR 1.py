import streamlit as st
from typing import Dict, List,Tuple, Any, Optional
import heapq

st.title("Breadth-First Search and Depth-First Search")
st.image("LabReport_BSD2513_#1.jpg") 

graph = {
    'A':['B','D'],
    'B':['C','E','G'],
    'C':['A'],
    'D':['C'],
    'E':['H'],
    'F':[],
    'G':['F'],
    'H':['G','F']
}

nodes = list(graph.keys())

algo = st.radio("Choose Traversal Algorithm:", ["Breadth-First Search", "Depth-First Search"])
start_node = st.selectbox("Select Start Node:", nodes)


def bfs(graph, start):
    visited = []
    queue = [start]
    order = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            order.append(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    queue.append(neigh)
    return order

def dfs(graph, start):
    visited = set()
    order = []
    def dfs_helper(node):
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neigh in graph[node]:
                dfs_helper(neigh)
    dfs_helper(start)
    return order


if st.button("Run Traversal"):
    if algo == "Breadth-First Search":
        order = bfs(graph, start_node)
        st.subheader("BFS Traversal Order")
    else:
        order = dfs(graph, start_node)
        st.subheader("DFS Traversal Order")
    
    st.write(" → ".join(order))



    
 
