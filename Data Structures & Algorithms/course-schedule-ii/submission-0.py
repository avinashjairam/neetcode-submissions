class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list where each course maps to its list of prerequisites
        preq = {c: [] for c in range(numCourses) }

        # populate the prerequistes 
        for crs, pre in prerequisites:
            preq[crs].append(pre)

        # list to store course order 
        order = []

        # sets to store visited courses
        visited = set()
        cycle = set()

        def dfs(c):
            if c in cycle:
                return False 

            if c in visited:
                return True 

            # add course to DFS path
            cycle.add(c)

            # for each course, recursively check its prereqs
            for crc in preq[c]:
                if not dfs(crc):
                    return False 

            # remove from current path
            cycle.remove(c)
            # mark as fully processed
            visited.add(c)

            # add course to output list (post order for topological sort)
            order.append(c)

            return True

        # visit each course
        for c in range(numCourses):
            # if any cycle is detected, it is impossible to finish all courses 
            if dfs(c) == False:
                return []

        # return reversed post order (reverse not needed because we're adding after all prereqs)
        return order
        