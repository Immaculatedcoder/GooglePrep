# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



from collections import defaultdict
from collections import deque
def ladderLength(self, beginWord, endWord, wordList):
    # Task 1: Build an adjaceny list from begin to end.
    def isValid(word1, word2):
        # We want to test if words differ by one character
        # Provided that word1 is different from word 2
        if len(word1) != len(word2):
            return False

        differ = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differ += 1
        if differ == 1:
            return True
        return False



    graph = defaultdict(list)
    for word1 in [beginWord, *wordList]:
        for word2 in [beginWord, *wordList]:
            if word1 == word2:
                continue
            if isValid(word1, word2):
                graph[word1].append(word2)

    # Task 2: Now do BFS to take the 
    def bfs(start, endWord):
        q = deque()
        q.append(start)
        seen.add(start)
        count = 1
        while q:
            current_node = q.popleft()
            if current_node == endWord:
                return count
            for nei_node in graph[current_node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
                    count += 1
        return 0
    seen = set()
    return bfs(beginWord, endWord)


