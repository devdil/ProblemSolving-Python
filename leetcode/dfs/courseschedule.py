class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        being_visited = set()
        visited = set()
        unvisited = set()
        adjacency_map = {}

        # add everything to my unvisited set
        for vertex_pair in prerequisites:

            unvisited.add(vertex_pair[0])
            unvisited.add(vertex_pair[1])

            if vertex_pair[0] in adjacency_map:
                adjacency_map[vertex_pair[0]].append(vertex_pair[1])
            else:
                adjacency_map[vertex_pair[0]] = [vertex_pair[1]]

        for vertex in unvisited:
            if self.dfs(vertex, visited, unvisited, being_visited, adjacency_map):
                return False

        return len(visited) == len(unvisited)

    """
        Returns True if a cycle is found else False
    """

    def dfs(self, vertex, visited, unvisited, being_visited, adjacency_map):

        # mark the current node as visited
        being_visited.add(vertex)

        # for all the adjacent vertices for current vertex, call dfs again
        adjacent_vertexes = adjacency_map.get(vertex, None)

        for adjacent_vertex in adjacency_map.get(vertex, None):
            if adjacent_vertex in visited:
                # don't do anything
                continue
            if adjacent_vertex in being_visited:
                # something is really suspicious, nah I am kidding its a cycle
                return True

            if self.dfs(adjacent_vertex, visited, unvisited, being_visited, adjacency_map):
                return True

        # if all the exploration is complete
        being_visited.remove(vertex)
        visited.add(vertex)

        #by this time everything should be complete
        return False


