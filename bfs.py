def bfs(visited,graph,node):
    visited.append(node)
    q.append(node)
    while q:
        v=q.pop()
        print(v,end="")
        for u in graph[v]:
            if u not in visited:
                visited.append(u)
                q.append(u)
g={}
l=[]
nodes=[]
n=int(input("enter no of nodes"))
for i in range(n):
    l.append(input("enter node"))
for i in l:
    adj=int(input("enter no of adjacent nodes for"+i+":"))
    for j in range(adj):
        nodes.append(input("enter node:"))
    g[i]=[]+nodes
    nodes.clear()
root=input("enter root node:")
visited=[]
q=[]
bfs(visited,g,root)
s=input("enter the node to be searched:")
if s in visited:
    print("\n"+s+"is found")
else:
    print("\n"+s+"is not found")
