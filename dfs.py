def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for v in graph[node]:
            dfs(visited,graph,v)
    #return visited
g = {}

l=[]

nodes=[]
visited=[]
n=int(input("Enter number of nodes:"))

for i in range(n):

    l.append(input("Enter node:"))

for i in l:

    adj=int(input("Enter number of adjacent nodes for "+i+":"))

    for j in range(adj):

        nodes.append(input("Enter node:"))

    g[i]=[]+nodes

    nodes.clear()

root=input("Enter the root node:")
dfs(visited,g,root)
s=input("\nenter search node:")
if s in visited:
    print("\n"+s+" is found")
else:
    print("\n"+s+" is not found")
