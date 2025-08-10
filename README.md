# Matrix Utilities in Python

A small Python project implementing basic matrix operations with a focus on clarity and reusability.

## Features
- Basic matrix functions (determinant, minors, cofactors, adjugate, etc.)
- Works better for small to medium-sized matrices
- Memoization for faster repeated computations
- Handles ill-conditioned (ill-treated) matrices gracefully
- Pure Python, no external dependencies

## Notes
- This is intended for educational and light computational purposes, not heavy-duty numerical workloads.
- For very large matrices, consider optimized libraries like NumPy.
- Functions are written to be easy to read and adapt for your own projects.

## Example Usage
```python
from Matrix import determinant, adjugate

mat = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

print("Determinant:", determinant(mat))
print("Adjugate:", adjugate(mat))
