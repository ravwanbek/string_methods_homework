def main(s):
    """
    A string containing the letter "x" is given. Find the index of the letter "x" in this variable.
    Args:
        s: str
    Returns:
        str: answer
    """
    s=str(s)
    answer=s.find('x')
    return answer
print(main('adadadcx'))