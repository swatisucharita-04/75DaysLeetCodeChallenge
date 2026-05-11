class Solution(object):
    def decodeString(self, s):
        stack = []
        currentStr = ""
        currentNum = 0

        for char in s:
            
            if char.isdigit():
                currentNum = currentNum * 10 + int(char)

            elif char == "[":
                stack.append((currentStr, currentNum))
                currentStr = ""
                currentNum = 0

            elif char == "]":
                prevStr, num = stack.pop()
                currentStr = prevStr + num * currentStr

            else:
                currentStr += char

        return currentStr