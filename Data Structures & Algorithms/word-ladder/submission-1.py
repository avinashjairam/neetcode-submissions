class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord is not in the wordlist, no transformation is possible
        if endWord not in wordList:
            return 0

        # Step 1: Build a dict to map generic patterns to actual words 
        # For example: '*ot' -> ['hot', 'dot', 'lot']
        nei = collections.defaultdict(list) # pattern -> list of words matching pattern 

        # include the beginWord in the word list for pattern mapping
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                # replace each character with a '*' to form a pattern 
                pattern = word[:j] + '*' + word[j + 1: ]
                nei[pattern].append(word)

        # Step 2: Initialize BFS
        visit = set([beginWord]) # track visited words to avoid cycles 
        q = deque([beginWord]) # start BFS from beginWord 
        res = 1 # Number of transformation steps (beginWord counts as step 1 )

        # Step 3: Perform BFS 
        while q:
            for i in range(len(q)):
                word = q.popleft()

                # if we reach the endWord, return the number of steps taken 
                if word == endWord:
                    return res 

                # try all possible patterns of the current word
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]

                    # for each pattern, explore all words that match it 
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            # mark as visited 
                            visit.add(neiWord)
                            # add to BFS queue for next level
                            q.append(neiWord)

            # increment stepcount after processing one level
            res += 1 

        # if BFS ends without finding the end word, return 0
        return 0

        