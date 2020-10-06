import sys, os, pandas, csv, math, numpy, random

board_emails = [] #Remember to put the emails in here later

response_data = pandas.read_csv("data.csv", header=None)
number_of_responses = initial_data.shape[0]

category_indices = [5, 8, 9, 10, 11]
category_weights = [1, 1, 1, 1, 1]

#Next task: filter the responses into mentors and mentees
board_info = []
mentee_info = []
for row_number in range(number_of_responses):
  if(response_data.iloc[row_number, 1] in board_emails):
    board_info.append(response_data.iloc[row_number,1])
  else:
    mentee_info.append(response_data.iloc[row_number,1])

#Next task: Check how similar each mentee is to each board member
mentee_values = [numpy.zeroes((len(board_emails),5))] * len(mentee_info)
for mentee_index in range(len(mentee_info)):
  for mentor_index in range(len(board_info)):
    for category_index in range(len(category_indices)):
      similarity_count = 0
      for priority_index in range(len(board_info[mentor_index].iloc[category_indices[category_index]].split(", "))):
        if(mentee_info[mentee_index].str.contains(board_info[mentor_index].iloc[category_indices[category_index.split(", ")[priority_index], case=False).any()):
          similarity_count += 1
      mentee_values[mentor_index][category_index] = similarity_count

#Next Task: Create a manipulatable data set for easy access during assignment
mentee_array = numpy.zeroes((len(mentee_info), len(board_info) + 1))
for mentee_index in range(len(mentee_info)):
  for mentor_index in range(len(board_info)):
    mentee_array[mentee_index][mentor_index] = numpy.inner(mentee_values[mentee_index][mentor_index], category_weights)
  mentee_array[mentee_index][-1] = mentee_index

#Next Task: Assignment
assignments = [[]] * len(board_info)
for mentee_index in range(len(mentee_info)):
  mentee_array = mentee_array[numpy.argsort(mentee_array[:, mentee_index % len(board_info)])]
  match_count = 0
  row = 1
  while (match_count = 0):
    for day_index in range(len(board_info[mentor_index].iloc[7].split(", "))):
      if(mentee_info[mentee_array[-row][-1].iloc[7].str.contains(board_info[mentor_index].iloc[7].split(", ")[day_index], case=False).any()):
        match_count = 1
    row += 1 
  assignments[mentee_index % len(board_info)].append(mentee_info[mentee_array[1-row][-1]])
  numpy.delete(mentee_array, 1-row, 0)

#Next Task: Output the assignments to a csv file
with open("./master.csv", 'w') as output_file:        
  master_writer = csv.writer(master_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  for mentor_index in range(len(assignments)):
    master_writer.writerow(board_info[mentor_index].iloc[2])
    for mentee_index in range(len(assignments[mentor_index])):
      current_mentee_info = mentee_info[assignments[mentor_index][mentee_index]]
      master_writer.writerow([current_mentee_info.iloc[2], current_mentee_info.iloc[1], current_mentee_info.iloc[6]])
    

