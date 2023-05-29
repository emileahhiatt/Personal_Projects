import pandas as pd
from random import randint
import sys

def MealPlan(recipes, num_meals, rating1, rating2, old_plan):

    meal_len = len(recipes)-1
    meal_plan = []
    rate_lst = []
    ing_lst = []
    while len(meal_plan) < num_meals:
        rand = randint(0, meal_len)
        if recipes['Meal'][rand] in list(old_plan['Meal']):
            continue
        elif rating1 in rate_lst and recipes['Rating'][rand] == rating1:
            continue
        elif rate_lst.count(rating2) == rating2 and recipes['Rating'][rand] == rating2:
            continue
        else:
            meal_plan.append(recipes['Meal'][rand])
            rate_lst.append(recipes['Rating'][rand])
            ing_lst.append(recipes['Ingredients'][rand])
            if len(set(meal_plan)) != len(meal_plan):
                del meal_plan[-1]
                del rate_lst[-1]
                del ing_lst[-1]
    
    new_meal_plan_df = pd.DataFrame({'Meal':meal_plan, 'Rating':rate_lst, 'Ingredients':ing_lst}, columns=['Meal', 'Rating', 'Ingredients'])
    new_meal_plan_df.to_excel('C:/Users/emile/OneDrive/Documents/Family_Manager_App/Meal_Plan.xlsx', sheet_name='Meal Plan', index=False)
    
    return new_meal_plan_df;
	
def GroceryList(meal_plan, staples):
    
    ing_df = meal_plan['Ingredients'].str.split(pat=',', expand=True)
    ing_df = ing_df.apply(lambda x: x.str.strip())
    staple_df = staples['Items'].str.split(pat=',', expand=True)
    staple_df = staple_df.apply(lambda x: x.str.strip())
    all_food_df = ing_df.append(staple_df, ignore_index=True)
    
    groc_lst = []
    groc_dct = {}
    for index, row in all_food_df.iterrows():
        for index, ing in row.items():
            groc_lst.append(ing)
            groc_dct[ing] = groc_lst.count(ing)
    
    groc_df = pd.DataFrame(list(groc_dct.items()), columns=['Item', 'Number of Meals'])
    groc_df.dropna(axis=0, subset=['Item'], inplace=True)
    groc_df.to_excel('C:/Users/emile/OneDrive/Documents/Family_Manager_App/Grocery_List.xlsx', sheet_name='Grocery List', index=False)
    
    return groc_df;
	
	