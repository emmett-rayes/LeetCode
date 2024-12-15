def corresponding(s: str) -> str:
    if s == ")":
        return "("
    if s == "}":
        return "{"
    if s == "]":
        return "["


def valid_parentheses(s: str) -> bool:
    stack = []
    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c)
        else:
            other = corresponding(c)
            if len(stack) == 0 or other != stack[-1]:
                return False
            else:
                stack.pop()
    return len(stack) == 0
