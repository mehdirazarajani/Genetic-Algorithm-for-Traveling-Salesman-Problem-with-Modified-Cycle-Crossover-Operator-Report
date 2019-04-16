from random import randint
import random
from CX import crossoverOperator
from CX import crossoverOperator2

population = []  # list that holds paths
population_size = 10  # max 120 combinations
mutate_prob = 0.1
n_generations = 1
routes_length = [0]*population_size
fitness = [0]*population_size
best_path = 1000

cities = [0, 1, 2, 3, 4,5,6,7,8,9]
#,10,11,12,13,14,15,16.17,18,19,20
# distance matrix for our cities
distances1= [[0, 4, 4, 7, 3],
             [4, 0, 2, 3, 5],
             [4, 2, 0, 2, 3],
             [7, 3, 2, 0, 6],
             [3, 5, 3, 6, 0]]

distances = [
   [ 0,   510     ,0,   635   ,355 ,    0 ,   91,   415,   605,  0],
   [ 385  , 585   ,390  , 350     ,0 ,  155 ,  475 ,  495  , 120   ,240],
   [0   ,110 ,  480 ,  570    ,78     ,320  ,  96 ,    0,   130 ,  500],
   [540 ,   97,   285,    36   , 29    , 0  , 490  , 605 ,  295 ,  460],
   [120  , 350 ,  425 ,  390   ,  0   ,370  , 320  , 700  , 0  , 590],
   [365   ,350  , 370  , 625   ,  0   ,155  , 380  , 640   , 63  , 430],
   [200   ,160   ,175  , 535   ,240   ,  0   , 68  , 440  , 575  ,  27],
   [320   , 91   , 48  ,  67   ,430   ,300   , 90  ,   0  , 610  , 360],
   [705   ,520  , 835  , 605   ,590   ,610   ,865  , 250  , 480  , 545],
   [0   ,655   ,235  , 585   ,555   ,750   ,615  , 625  , 645   ,775]
]


# calculates distance between 2 cities
def calc_distance(city1, city2):
    print('hello')
    print(city2)
    return distances[city1][city2]  # ord('A')=65


# creates a random route
def create_route():
    list=[]
    y=randint(0,len(cities))
    for i in range(0,cities.__len__()):
        list.append(cities[(i+y)%cities.__len__()])

    print('list')
    print(list)
    return list


# calculates length of an route
def calc_route_length():
    for i in range(population_size):
        route_l = 0
        for j in range(1, len(cities)):
            # print('hello ')
            # print(type(i))
            print(population[i][j])
            print(population)
            route_l = route_l + calc_distance(population[i][j - 1], population[i][j])
            # route_l = route_l + calc_distance(population[i][len(cities)-1], population[i][1]) calculate distance from last to first
        routes_length[i] = route_l
        fitness[i] = 1 / routes_length[i]


# creates starting population
def create_population():
    for i in range(population_size):
        population.append(create_route())


# swap with a probability 2 cities in a route
def swap_mutation(ind):
    picks = random.sample(range(len(cities)), 2)
    temp = population[ind][picks[0]]
    population[ind][picks[0]] = population[ind][picks[1]]
    population[ind][picks[1]] = temp
    # print("Mutated path: ", population[ind])


# PMX crossover
def partially_matched_crossover(ind1, ind2):
    size = len(cities)
    p1, p2 = [0] * size, [0] * size

    # Initialize the position of each indices in the individuals
    for k in range(size):
        p1[ind1[k]] = k
        p2[ind2[k]] = k
    # Choose crossover points
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

# Apply crossover between cx points
    for k in range(cxpoint1, cxpoint2):
    # Keep track of the selected values
        temp1 = ind1[k]
        temp2 = ind2[k]
    # Swap the matched value
        ind1[k], ind1[p1[temp2]] = temp2, temp1
        ind2[k], ind2[p2[temp1]] = temp1, temp2
    # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return ind1, ind2


# function that picks a parent Fitness Proportionate Selection
def roulette_wheel_selection():
    s = 0
    partial_s = 0
    ind = 0
    for m in range(population_size):
        s = s + fitness[m]
    rand = random.uniform(0, s)
    for m in range(population_size):
        if partial_s < rand:
            partial_s = partial_s + fitness[m]
            ind = ind + 1
    if ind == population_size:  # prevent out of bounds list
        ind = population_size - 1
    return ind


# find fittest path called every generation
def find_fittest():
    key = 1000
    fittest = 0
    for i in range(population_size):
        if routes_length[i] < key:
            key = routes_length[i]
            fittest = i


    print('ddfdd')
    print(fittest)
    return fittest


# sorts parallely the lists
#def sort_alongside(routes_length, population):
#    routes_length, population = (list(i) for i in zip(*sorted(zip(routes_length, population))))


# initialize algorithm
create_population()
print("Population initialization:", "\n", population)
calc_route_length()
print("Population's paths length:", "\n", routes_length)

for j in range(n_generations):
    for i in range(0, population_size, 2):
        # pick parents for crossover
        parent1 = roulette_wheel_selection()
        parent2 = roulette_wheel_selection()
        # always pick different parents (not necessary)
        while True:
            if parent1 == parent2:
                parent2 = roulette_wheel_selection()
            else:
                break
        # update population
       # population[i], population[i + 1] = partially_matched_crossover(population[parent1], population[parent2])
        population[i], population[i + 1] = crossoverOperator(population[parent1], population[parent2])
        # calculate lengths for updated generation
        calc_route_length()

    # pick the paths for mutation based on a probability
    for i in range(population_size):
        rand = random.uniform(0, 1)
        if rand < mutate_prob:
            swap_mutation(i)

    # calculate lengths after mutation
    calc_route_length()
    index=0
    # find best path overall
    if routes_length[find_fittest()] < best_path:
        print('shakeeb')
        print(index)

        index = find_fittest()
        best_path = routes_length[index]

    print("Best route of generation", j+1, ": ", population[find_fittest()], "\n" "Route length: ",
          routes_length[find_fittest()])
    # print("Population of generation", j+1, ": \n", population)
    print("Routes lengths:", routes_length, "\n")
    print("Best path is:", population[index], "with length", best_path)