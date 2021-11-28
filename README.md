# python_bmi_calculator
BMICalculator and Risk Determinator
Python BMI Calculator Coding Task V6

Problem Statement

Given the following JSON data

[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },

{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },

{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },

{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},

{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},

{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

as the input with weight and height parameters of a person, we have to perform the following:

Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health risk from Table 1 of the person and add them as 3 new columns
Count the total number of overweight people using ranges in the column BMI Category of Table 1, check this is consistent programmatically and add any other observations in the documentation
Create build, tests to make sure the code is working as expected and this can be added to an automation build / testing / deployment pipeline Formula 1 - BMI BMI(kg/m2) = mass(kg) / height(m)2 The BMI (Body Mass Index) in (kg/m2 ) is equal to the weight in kilograms (kg) divided by your height in meters squared (m)2 . For example, if you are 175cm (1.75m) in height and 75kg in weight, you can calculate your BMI as follows: 75kg / (1.75m²) = 24.49kg/m² Table 1 - BMI Category and the Health Risk. BMI Category BMI Range (kg/m2) Health risk Underweight 18.4 and below Malnutrition risk Normal weight 18.5 - 24.9 Low risk Overweight 25 - 29.9 Enhanced risk Moderately obese 30 - 34.9 Medium risk Severely obese 35 - 39.9 High risk Very severely obese 40 and above Very high risk Problem
Write a solid production-grade Python3 Program to solve this problem, imagine this will be used in-product for 1 Lac patients. We are only interested in a standalone backend application, we are NOT expecting a UI, webpage, frontend, Mobile App, microsite etc. We want to see what optimal solution you come up with to scale for larger JSON data and perform calculations quickly and write the output efficiently. Feel free to explore and use the standard Python libraries or any open source Python modules
