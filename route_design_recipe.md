Design the Route Signature:

# Sort names route
POST /sort-names
    names: string

Create Examples as Tests:
"""
POST /sort-names
    Parameters:
        names: Ben,Alex,Sarah,Millie
    Expected response (200 OK)

Sorted list of names
Alex,Ben,Millie,Sarah
"""

"""
POST /sort-names
    Parameters:
        names: none
        Expected response (400 Bad Request)

Please provide a list of names
"""