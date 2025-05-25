# Problem-10: The list below is the collection of the ages of people from a village. Clean up the data and store only numbers in another list.
# data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
cleaned_data = [item for item in data_list if isinstance(item, int)]

print(cleaned_data)