def main(s):
    """
    A variable of type str is given. Check that it consists of letters only.
    Args:
        s: str
    Returns:
        bool: answer
    """
    
    s=str(s)
    answer=s.isalpha()
    return answer
print(main('adadadxcx'))