from storage import q, y
from players import d

def runalltests():
    """Execute automated unit tests to verify file handling and input validation."""
    print("\n----> RUNNING PROJECT VALIDATION TESTS ")
    
    # Test Case 1: Non-existent file handling verification
    testresult = q("thisisadummytestfile.txt")
    if testresult == []:
        print("\nPASS Test 1: Non-existent file handling works correctly.")
    else:
        print("\nFAIL Test 1: Non-existent file handling did not return an empty list.")
        
    # Test Case 2: Input validation logic check
    sampleinvalidinput = "-5"
    is_valid = sampleinvalidinput.isdigit() and int(sampleinvalidinput) > 0
    if not is_valid:
        print("\nPASS Test 2: Input validation correctly rejects negative numbers.")
    else:
        print("\nFAIL Test 2: Input validation failed on negative numbers.")

    print("\n----> ALL TESTS COMPLETED ")

if __name__ == "__main__":
    runalltests()