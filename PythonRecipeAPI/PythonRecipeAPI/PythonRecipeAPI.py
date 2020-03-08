import requests
import sys
def getRecipeByIngredients(ingredients):
    payload = {
        'q': ingredients,
    }
    endpoint = "http://www.recipepuppy.com/api/"

    header = {'Content-Type': 'application/json'}
    
    response = requests.get(url = endpoint,params=payload, headers = header)
    data = response.json()
    Title = []
    Link = []
    print("Your Options are as follows: "+"\n")
    for x in range(5):
        Title.append(data['results'][x]['title'])
        Link.append(data['results'][x]['href'])
        print(Title[x])
        print(Link[x])
        print("\n")
ingred = input("Enter Your Ingredients: ")
getRecipeByIngredients(ingred)
           
