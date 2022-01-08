def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    s=str(s)
    answer=s.islower()
    return answer
print(main('assalomu alayKum'))