class Solution(object):
    def cloneGraph(self, node):

        if not node:
            return None

        oldToNew = {}

        def dfs(node):

            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)

            oldToNew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)