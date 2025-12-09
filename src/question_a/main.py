from question_a import create_multiplication_table, display_multiplication_table

# Main program loop
continue_program = True

while continue_program:
    # Call create_multiplication_table and save the result
    table = create_multiplication_table()
    
    # Call display_multiplication_table with the table variable
    display_multiplication_table(table)
    
    # Ask user if they want to continue or quit
    user_choice = input("\nDo you want to continue? (yes/no): ").lower()
    
    if user_choice != 'yes' and user_choice != 'y':
        continue_program = False
        print("Thank you for using the multiplication table program!")
