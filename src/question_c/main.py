from question_c import get_most_likely_ancestor_consensus


def validate_dna_string(dna_string, min_length, max_length):
    """Validate that DNA string contains only valid characters and proper length"""
    valid_chars = set('ATCG')
    
    # Check length
    if len(dna_string) < min_length or len(dna_string) > max_length:
        return False
    
    # Check if all characters are valid DNA characters
    if not all(char in valid_chars for char in dna_string):
        return False
    
    return True


def get_valid_dna_string(prompt, min_length, max_length):
    """Get and validate DNA string from user"""
    while True:
        dna_string = input(prompt).upper()
        
        if validate_dna_string(dna_string, min_length, max_length):
            return dna_string
        else:
            print(f"Invalid input. Please enter a DNA string with {min_length}-{max_length} characters (A, T, C, G only).")


def main():
    """Main program with continuous loop"""
    while True:
        print("\n" + "="*60)
        print("DNA Substring Finder")
        print("="*60)
        
        # Prompt for DNA string (8 < length <= 16)
        dna_string1 = get_valid_dna_string(
            "Enter a DNA string (greater than 8, less than or equal to 16 characters): ",
            9, 16
        )
        
        # Prompt for DNA substring (exactly 4 characters)
        dna_string2 = get_valid_dna_string(
            "Enter a DNA substring (exactly 4 characters): ",
            4, 4
        )
        
        # Call the function with user-provided values
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        
        # Display the result
        print("\n" + "="*60)
        print(f"DNA String: {dna_string1}")
        print(f"Substring: {dna_string2}")
        
        if result:
            print(f"Found at positions: {' '.join(map(str, result))}")
        else:
            print("Substring not found in DNA string.")
        print("="*60)
        
        # Ask user if they want to continue
        continue_choice = input("\nDo you want to continue? (yes/no): ").lower()
        if continue_choice != 'yes' and continue_choice != 'y':
            print("Thank you for using the DNA Substring Finder!")
            break


# Run the main program
main()