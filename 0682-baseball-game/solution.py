class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                b = stack[-1]
                a = stack[-2]
                stack.append(a + b)
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
            
        return sum(stack) or 0
