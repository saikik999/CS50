from collections import deque

actors_movies = {
    "Emma Watson": ["Harry Potter and the Order of the Phoenix", "Beauty and the Beast"],
    "Brendan Gleeson": ["Harry Potter and the Order of the Phoenix", "Trespass Against Us"],
    "Michael Fassbender": ["Trespass Against Us", "X-Men: First Class"],
    "Jennifer Lawrence": ["X-Men: First Class", "The Hunger Games"]
}

def build_graph(actors_movies):
    graph = {}
    for actor, movies in actors_movies.items():
        if actor not in graph:
            graph[actor] = set()
        for movie in movies:
            for coactor in actors_movies:
                if coactor != actor and movie in actors_movies[coactor]:
                    graph[actor].add(coactor)
                    if coactor not in graph:
                        graph[coactor] = set()
                    graph[coactor].add(actor)
    return graph

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        (current, path) = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    
    return None

def degrees_of_separation(actor1, actor2):
    graph = build_graph(actors_movies)
    path = bfs(graph, actor1, actor2)
    
    if path:
        degrees = len(path) - 1
        print(f"{degrees} degrees of separation.")
        for i in range(len(path) - 1):
            print(f"{i+1}: {path[i]} and {path[i+1]} starred in a movie together.")
    else:
        print("No connection found.")


degrees_of_separation("Emma Watson", "Jennifer Lawrence")