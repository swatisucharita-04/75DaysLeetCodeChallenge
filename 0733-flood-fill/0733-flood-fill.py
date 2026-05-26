class Solution(object):
    def floodFill(self, image, sr, sc, color):

        original = image[sr][sc]

        # if already same color
        if original == color:
            return image

        def dfs(r, c):

            # boundary check
            if (
                r < 0 or
                c < 0 or
                r >= len(image) or
                c >= len(image[0])
            ):
                return

            # wrong color
            if image[r][c] != original:
                return

            # change color
            image[r][c] = color

            # explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image