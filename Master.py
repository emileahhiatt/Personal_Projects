import pandas as pd
from random import randint
import sys
from Functions import MealPlan, GroceryList


recipe_df = pd.read_excel('C:/Users/emile/OneDrive/Documents/Family_Manager_App/Recipe_List.xlsx', sheet_name='Meals')
staple_df = pd.read_excel('C:/Users/emile/OneDrive/Documents/Family_Manager_App/Recipe_List.xlsx', sheet_name='Staples')
old_meal_plan_df = pd.read_excel('C:/Users/emile/OneDrive/Documents/Family_Manager_App/Meal_Plan.xlsx', sheet_name='Meal Plan')

MealPlan(recipes=recipe_df, num_meals=5, rating1=3, rating2=2, old_plan=old_meal_plan_df)

new_meal_plan_df = pd.read_excel('C:/Users/emile/OneDrive/Documents/Family_Manager_App/Meal_Plan.xlsx', sheet_name='Meal Plan')

GroceryList(meal_plan=new_meal_plan_df, staples=staple_df)