from math import sqrt,inf


def get_distance(x1, y1, x2, y2):
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

def shortest_path(M, start, goal):
    if start == goal:
        return [start]
    
    h_value={}
    for node, coordinates in M.intersections.items():
        h_value[node] = get_distance(coordinates[0], coordinates[1], M.intersections[goal][0], M.intersections[goal][1])
    dis={}
    dis[start]=h_value[start]
    dis_from_start={}
    dis_from_start[start]=0
    route={}
    route[start]=[start]
    visited=set()
    cur=start
    while cur!=goal:
        for node in M.roads[cur]:
            x=get_distance(M.intersections[cur][0], M.intersections[cur][1], M.intersections[node][0], M.intersections[node][1])+dis_from_start[cur]
            h=h_value[node]
            y=h+x
            if node in dis:
                if y<=dis[node]:
                    dis[node]=y
                    dis_from_start[node]=x
                    if node in visited:
                        visited.discard(node)
                    route[node]=route[cur].copy()
                    route[node].append(node)
            else:
                dis[node]=y
                dis_from_start[node]=x
                route[node]=route[cur].copy()
                route[node].append(node)
        visited.add(cur)
        min_value=inf
        for node in dis:
            if dis[node]<min_value and node not in visited:
                cur=node
                min_value=dis[cur]
    return route[goal]
                
                
        
    

