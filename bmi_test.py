import json
from bmi_calculator import BMICalculator
from deepdiff import DeepDiff

def TestBMICalculator(fileTest):
    Result_Table = BMICalculator()
    total_count_overweighted_person = 0
        # Load Json data from local storage
    with open(fileTest, 'r') as reader:
        data = json.load(reader)
    # if not data == Result_Table:
    #     return False 
    diff = DeepDiff(Result_Table, data)
    print(diff)
    if len(diff) != 0:
         return False
    for index in Result_Table:
        if "Overweight" in Result_Table[index].values():
            total_count_overweighted_person += 1
    if total_count_overweighted_person != 1:
        return False
    return True
if __name__== '__main__':
    test_result = TestBMICalculator('bmiFinal.json')
    if test_result == True:
        print("Passed")
    else:
        print("Failed")