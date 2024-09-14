import random
import streamlit as st

# List 1
list1 = [
    "Mary", "Betty", "Barbara", "Shirley", "Patricia", "Dorothy", "Joan", "Margaret", "Nancy", "Helen", "Ruth", 
    "Virginia", "Dolores", "Doris", "Frances", "Joyce", "Jean", "Elizabeth", "Alice", "Phyllis", "Rose", "Marie", 
    "Lois", "Martha", "Irene", "Gloria", "Evelyn", "Eleanor", "Marjorie", "Beverly", "Ann", "June", "Lillian", 
    "Florence", "Lucille", "Clara", "Mildred", "Katherine", "Louise", "Edna", "Esther", "Wilma", "Bernice", 
    "Caroline", "Vera", "Thelma", "Pauline", "Ethel", "Marilyn", "Sarah", "James", "John", "Robert", "William", 
    "Charles", "George", "Donald", "Richard", "Joseph", "Edward", "Frank", "Thomas", "Harold", "Paul", "Raymond", 
    "Walter", "Jack", "Albert", "Henry", "Arthur", "Fred", "Kenneth", "Eugene", "David", "Carl", "Ralph", "Louis", 
    "Howard", "Clarence", "Lawrence", "Roy", "Ernest", "Harry", "Leonard", "Samuel", "Earl", "Francis", "Alfred", 
    "Stanley", "Joe", "Bernard", "Herbert", "Norman", "Marvin", "Anthony", "Clyde", "Melvin", "Lester", "Edwin", 
    "Philip"
]

# List 2
list2 = [
    "Weave", "Glide", "Slip", "Navigate", "Push", "Squeeze", "Maneuver", "Dodge", "Wade", "Shove", "Shuffle", 
    "Wriggle", "Step", "Hustle", "Elbow", "Sidestep", "Thread", "Skirt", "Flow", "Press", "Bustle", "Sneak", "Barrel", 
    "Charge", "Part", "Stream", "Plow", "Creep", "Edge", "Hurdle", "Grapple", "Worm", "Cram", "Rush", "March", 
    "Push", "Tread", "Breeze", "Jostle", "Sidle"
]

# List 3
list3 = [
    "Turkey", "Bacon", "Lettuce", "Mayo", "Cheddar", "Tomato", "Ham", "Pickles", "Mustard", "Swiss", "Avocado", 
    "Chicken", "Pesto", "Arugula", "Salami", "Hummus", "Provolone", "Egg", "Tuna", "Onion", "Beef", "Spinach", 
    "Butter", "Brie", "Cucumber", "Berry", "Pork", "Rye", "Focaccia", "Oil", "Pepper", "Chicken", "Salmon", 
    "Radish", "Slaw", "Pepper", "Dijon", "Kraut", "Ciabatta", "Relish", "Kimchi", "Basil", "Baguette", "Apple", 
    "Honey", "Shrimp", "Aioli", "Cress", "Shroom", "Feta", "Caper", "Ham", "Dill", "Prosciutto", "Butter", 
    "Havarti", "Anchovies", "Muenster"
]

# Function to generate a random combination
def random_combination():
    return '{} {}{}'.format(random.choice(list1), random.choice(list2), random.choice(list3))

# Streamlit app code
st.title("Random Combination Generator")
if st.button('Generate'):
    st.write(random_combination())
