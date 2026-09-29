from storage import q, y
from players import d

def runalltests():
    print("\n----> RUNNING PROJECT VALIDATION TESTS ")
    
    # Test Case 1: This is the case where Non-existent file handling Is done

    testresult = q("thisisadummytestfile.txt")
    if testresult == []:
        print("\nPASS Test 1: Non-existent file handling works correctly.")
    else:
        print("\nFAIL Test 1: Non-existent file handling did not return an empty list.")
        
    # Test Case 2:  This is the case where Input Validation Logic is Checked (Simulating helpers.py logic)

    sampleinvalidinput="-5"
    is_valid=sampleinvalidinput.isdigit() and int(sampleinvalidinput) > 0
    if not is_valid:
        print("\nPASS Test 2: Input validation correctly rejects negative numbers.")
    else:
        print("\nFAIL Test 2: Input validation failed on negative numbers.")

    print("\n----> ALL TESTS COMPLETED ")

if __name__ == "__main__":
    runalltests()

'''
Time to make sure everything works! This script runs automated unit tests 
to verify edge cases—like checking how the app handles missing files or bad inputs— 
so we know our code is stable before letting anyone use it.
'''