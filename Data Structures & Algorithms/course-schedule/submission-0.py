class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # step 1 - create an adjacent list (course -> list of prerequisites)
        preMap = {i : [] for i in range(numCourses)} # initialize with empty lists

        for crs, pre in prerequisites:
            preMap[crs].append(pre) # crs depends on pre 

        # step 2 - use a set to track courses in the current dfs path (to detect cycles)
        visiting = set()

        # step 3 - dfs function to check if we can complete the course 
        def dfs(crs):
            if crs in visiting:
                # cycle detected - cannot finish courses
                return False 

            if preMap[crs] == []:
                # no prerequistes (or already verified) - can complete
                return True 

            # mark course as being visited
            visiting.add(crs)

            # visit all prerequisites for this course
            for pre in preMap[crs]:
                if not dfs(pre):
                    # if any prereq leads to a cycle, return False
                    return False

            # done exploring this path
            visiting.remove(crs)

            # memoize: mark course as having no further prereq to check
            return True 

        # Step 4: check all courses
        for c in range(numCourses):
            if not dfs(c):
                # if any course has a cycle, return False
                return False

        return True 



        