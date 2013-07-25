ptree = {'A': ['B', 'C', 'D'],
         'B': ['E', 'F'],
         'F': ['O'],
         'C': ['G'],
         'D': ['I','J','K','L'],
         'E': ['M'],
         'M': ['N','O'],
         'O': ['P','Q']
        }
print ptree

for k in ptree.keys():
#    print k
#    print val
    for v in ptree[k]:
#        print '-->',v
        if v in ptree.keys() and k not in ptree[v]:
            ptree[v].append(k)
        elif v not in ptree.keys():
            ptree[v]=k

print '--------------------------------'
print ptree

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
print '_______________________________________________________________'
print find_all_paths(ptree, 'B', 'Q')
print find_all_paths(ptree, 'G', 'Q')

