class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create an adjacency list to represent the directed graph
        # each character is a node, and we'll add edges based on character relationship
        adj = {c: set() for w in words for c in w}

        # keep track of incoming edges (indegree for each character)
        # this will be used for topological sorting 
        indegree = {c: 0 for c in adj}

        # compare adjacent words to build the graph
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # check for invalid case: if w1 is longer than w2 and w1 starts before w2
            # then w1 should come after w2 lexicographically, not before 
            # example: ['apple', 'app'] is invalid because 'apple' should come after 'app' 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''

            # Find the first character that differs between the two words 
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # w1[j] comes before w2[j] in the alien alphabet 
                    # add an edge from w1[j] to w2[j] if it doesn't already exists 
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1

                    # only need the first different character 
                    break 

        # perform topological sort using BFS
        # start with characters that have 0 indegree (no characters come before them)
        q = deque([c for c in indegree if indegree[c]==0])
        res = []

        # process each character with 0 indegree
        while q:
            char = q.popleft()
            res.append(char) # add to the result order 

            # reduce indegree of all neighbors 
            for neighbor in adj[char]:
                indegree[neighbor] -= 1 

                # if a neighbor now has 0 in degree, add it to the queue 
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # if we couldn't process all characters, there must be a cycle 
        # a cycle means there's a contradiction in the character order 
        if len(res) != len(indegree):
            return ''

        # return the characters in their determined order 
        return ''.join(res)


