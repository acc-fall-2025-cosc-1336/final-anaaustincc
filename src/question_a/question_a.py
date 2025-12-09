#write functions here, don't add input('') statements here!

def create_multiplication_table():
    """Create a multiplication table using nested lists"""
    table = []
    
    # Use nested looping to create the table
    for i in range(1, 6):  # Rows 1-5
        row = []
        for j in range(1, 11):  # Columns 1-10
            row.append(i * j)
        table.append(row)
    
    return table


def display_multiplication_table(table):
    """Display the multiplication table with proper formatting"""
    for row in table:
        # Display each element separated by spaces
        print(' '.join(f"{num:2d}" for num in row))


def test_config():
    return True