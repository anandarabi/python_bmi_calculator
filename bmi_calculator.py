import json

def BMICalculator():
    # Load Json data from local storage
    with open('bmi.json', 'r') as reader:
        data = json.load(reader)   
    # The maximum value of range is assumed to be 60. But it will not have any impact.
    BMIRange = {0:[0,18.5], 1:[18.5,24.9], 2:[25,29.9], 3:[30,34.9], 4:[35,39.9], 5:[40,60]}
    HealthRisk = ["Malnutrition risk","Low risk","Enhanced risk","Medium risk","High risk","Very high risk"]
    BMICategory = ["Underweight","Normal weight","Overweight","Moderately obese","Severely obese","Very severely obese"]
    # The Result_Table will store all the BMI and other details based on given data and will store in Dictionary using key 1,2,3,...
    Result_Table = {}

    for (i, person) in enumerate(data):
        bmiVal = round(person["WeightKg"]/(person["HeightCm"]/100)**2, 2)
        for index in BMIRange:
            if index == 5:
                Result_Table[str(i)] = {"Gender":person["Gender"], "HeightCm":person["HeightCm"], "WeightKg":person["WeightKg"], "BMI":bmiVal, "HealthRisk":HealthRisk[index], "BMICategory":BMICategory[index]}
                break
            if bmiVal >= BMIRange[index][0] and bmiVal < BMIRange[index + 1][0]:
                Result_Table[str(i)] = {"Gender":person["Gender"], "HeightCm":person["HeightCm"], "WeightKg":person["WeightKg"], "BMI":bmiVal, "HealthRisk":HealthRisk[index], "BMICategory":BMICategory[index]}
                break
    return Result_Table

if __name__=='__main__':
    Result_Table = BMICalculator()
    total_count_overweighted_person = 0
    for index in Result_Table:
        print(Result_Table[index])
        if "Overweight" in Result_Table[index].values():
            total_count_overweighted_person += 1
    # The following code writes the final result as json object on local storage
    with open('bmiFinal.json', 'w') as writer:
        json.dump(Result_Table, writer)
    print(Result_Table)
    print(f"Total Number of Overweighted person {total_count_overweighted_person}")