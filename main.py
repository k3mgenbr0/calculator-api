from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both parameters must be valid numbers."
        )

    result = a + b
    return {
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    """
    Subtract two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both parameters must be valid numbers."
        )

    result = a - b
    return {
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    """
    Multiply two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both parameters must be valid numbers."
        )

    result = a * b
    return {
        "a": a,
        "b": b,
        "result": result
    }

@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    """
    Divide two numbers together.

    Parameters:
    - a: First number
    - b: Second number

    Returns:
    - JSON object with the result
    """

    # Convert inputs to floats
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both parameters must be valid numbers."
        )

    # Handle division by zero
    if b == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Division by zero is not allowed."
        )

    # Perform division
    result = a / b

    return {
        "a": a,
        "b": b,
        "operation": "division",
        "result": result
    }
@app.get("/average/{a}/{b}/{c}/{d}/{e}", status_code=200)
def average(a: str, b: str, c: str, d: str, e: str):
    """
    Calculate the average of three numbers.

    Parameters:
    - a: First number
    - b: Second number
    - c: Third number
    - d: Fourth number
    - e: Fifth number

    Returns:
    - JSON object containing the three inputs and their average
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="All parameters must be valid numbers."
        )

    result = (a + b + c + d + e) / 3

    return {
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "e": e,
        "result": result
    }    

import math

@app.get("/hypotenuse/{a}/{b}", status_code=200)
def hypotenuse(a: str, b: str):
    """
    Calculate the hypotenuse of a right triangle using the Pythagorean theorem.

    Parameters:
    - a: Length of the first side
    - b: Length of the second side

    Returns:
    - JSON object containing the side lengths and the calculated hypotenuse.
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both parameters must be valid numbers."
        )

    result = math.sqrt(a**2 + b**2)

    return {
        "side_a": a,
        "side_b": b,
        "result": result
    }

@app.get("/rectangle-area/{length}/{width}", status_code=200)
def rectangle_area(length: str, width: str):
    """
    Calculate the area of a rectangle.

    Parameters:
    - length: The rectangle's length
    - width: The rectangle's width

    Returns:
    - JSON object containing the length, width, and computed area
    """
    try:
        length = float(length)
        width = float(width)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both parameters must be valid numbers."
        )

    result = length * width

    return {
        "length": length,
        "width": width,
        "result": result
    }