# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 03:28:30 2023

@author: Asama
"""

def is_valid_value(val):
    '''
    is_valid_value -> Check whether the input is valid or not 
    Return true if the value is positive then return True else return false 
    '''
    
    return val.isnumeric() and float(val) > 0 ;
        

def calculate_bmi(weight,height):
    '''
        calculate_bmi -> bmi=weight / height^2
    '''
    if not is_valid_value(weight) or not is_valid_value(height):
        
        print ("invalid input,Try again ")
        return False
    height = float(height) / 100
    weight = float(weight) 
    return weight / height**2        
    
def interpret_bmi(val):
    '''
        interpret_bmi is responsible on print bmi's information 
    '''
    if val < 18.5 :
        print("Underweight")
    elif val >= 18.5 and val < 25 :
        print("Normal weight")
    elif val >= 25 and val < 30 :
        print("Overweight")
    elif val >= 30 :
        print("Obase")
    








def main():
    print("=================== Hello in my BMI calculator =================== ")
    print("=================== The weight should be in kilogram and height in meter")
    while True :
        weight = input("Enter weight:")
        height = input("Enter height:")
        bmi = calculate_bmi(weight,height)
        if bmi==False:
            continue
        interpret_bmi(bmi)
        break
    
main()
            
        
 
 





















