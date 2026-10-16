"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():
    temp_days = [24, 41, 22, 44, 33, 22, 23]
    return temp_days

def analyze_temps(temps_list):
    avg = sum(temps_list) / len(temps_list)
    high = max(temps_list)
    low = min(temps_list)
    return (avg, high, low)

def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print(f"average : {avg} C")
    print(f"highest :{high} C")
    print(f"lowest :{low} C")

temps = get_temperatures()
print(temps)

result = analyze_temps(temps)
print(result)

display_analysis(result[0],result[1],result[2])




