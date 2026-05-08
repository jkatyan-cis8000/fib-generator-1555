def generate_fibonacci(limit: int) -> list[int]:
    """Generate Fibonacci numbers up to and including the limit.
    
    Args:
        limit: Upper bound for Fibonacci numbers (inclusive).
        
    Returns:
        List of Fibonacci numbers up to the limit.
        
    Raises:
        ValueError: If limit is negative.
    """
    if limit < 0:
        raise ValueError("Limit must be non-negative")
    
    if limit < 1:
        return []
    
    result = []
    a, b = 0, 1
    
    while a <= limit:
        result.append(a)
        a, b = b, a + b
    
    return result
