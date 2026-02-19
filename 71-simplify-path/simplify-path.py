class Solution:
    def simplifyPath(self, path: str) -> str:
        filename = path.split("/")
        stack = []
        for f in filename:
            if f == "" or f == ".":
                continue
            elif f == "..": # Because the parent directory is previusly added to stack we need to remove it
                if stack:
                    stack.pop()
            else:
                stack.append(f)
        return "/" + "/".join(stack)