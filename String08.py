def main(s):
    """
    A variable of type str is given. Make sure it only consists of uppercase letters.
    Args:
        s: str
    Returns:
        bool: answer
    """
    
    s=str(s)
    answer=s.isupper()
    return answer
print(main('SDFJsSLDFKJS'))