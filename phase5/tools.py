from langchain.tools import tool

@tool
def add_num(n1: int,n2:int) -> str:
    """Adds 2 numbers .use this when user wants to add 2 numbers"""
    return f"result{n1 + n2}"