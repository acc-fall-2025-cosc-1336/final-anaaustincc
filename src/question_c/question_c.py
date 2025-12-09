#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    """
    Find all locations of dna_string2 as a substring in dna_string1
    Returns the beginning positions as multiple Python parameters (unpacked tuple)
    Positions are 1-indexed (add 1 to account for 0-based indexing)
    """
    positions = []
    
    # Iterate through dna_string1 to find all occurrences of dna_string2
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        # Check if substring matches at position i
        if dna_string1[i:i + len(dna_string2)] == dna_string2:
            # Add 1 to convert from 0-indexed to 1-indexed position
            positions.append(i + 1)
    
    # Return positions as unpacked tuple (multiple parameters)
    return tuple(positions)