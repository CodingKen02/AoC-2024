from collections import Counter

def read_lists(file_path):
    list1 = []
    list2 = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # Splitting the line by whitespace
            parts = line.split()
            
            # Creating the strings into integers and adding them to their lists
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))
    
    return list1, list2

def calculate_total_distance(list1, list2):
    # Ascending (low to high)
    list1.sort()
    list2.sort()
    
    # Creating pairs of the lists for each line; calculating/storing absoulte total difference
    total_distance = 0
    for a, b in zip(list1, list2):
        total_distance += abs(a - b)
    
    return total_distance

def calculate_similarity_score(list1, list2):
    # Creating a Counter object to count occurrences of each number in list2
    count_right_list = Counter(list2)
    
    total_similarity_score = 0
    
    for number in list1:
        # Multiplying each number by the count of its appearances in list2
        total_similarity_score += number * count_right_list.get(number, 0)
    
    return total_similarity_score

file_path = 'day1.txt'
list1, list2 = read_lists(file_path)

# Calculating and print the total distance
distance_result = calculate_total_distance(list1, list2)
print(distance_result)
similarity_score = calculate_similarity_score(list1, list2)
print(similarity_score)
