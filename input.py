from graph_conversion_assingment1_abhijeet import *
import pprint
print("1. to convert adjacency matrix to list\n 2. to convert list to adjacency matrix.\n 3. to convert incidece matrix to adjacency list\n 4. to convert adjacency list to adjacency matrix\n 5. to convert adjacency matrix to incidence matrix\n 6. to convert Incident matrix to adjacent matrix");
choice = raw_input("enter choice:\n")
if(choice=="1"):
	print("conversion of adjacency matrix to adjacency list")

	matrix=[]
	matrix.append([0, 1, 1, 1, 1, 1])
	matrix.append([1, 0, 1, 1, 1, 1])
	matrix.append([1, 1, 0, 1, 1, 1])
	matrix.append([1, 1, 1, 0, 1, 1])
	matrix.append([1, 1, 1, 1, 0, 1])
	matrix.append([1, 1, 1, 1, 1, 0])
	print("adjacency matrix")
	pprint.pprint(matrix)
	print("adjacency list")
	
	pprint.pprint(adjacency_matrix_to_adjacency_list(matrix))
if(choice=="2"):
	print("convert adjacency list to adjacency matrix") 
	adj_list = {0: [1, 2, 3, 4, 5],
                     1: [0, 2, 3, 4, 5],
                     2: [0, 1, 3, 4, 5],
                     3: [0, 1, 2, 4, 5],
                     4: [0, 1, 2, 3, 5],
                     5: [0, 1, 2, 3, 4]}
	print("adjacency list")
	pprint.pprint(adj_list)
	print("adjacency matrix")
	
	pprint.pprint(adjacency_list_to_adjacency_matrix(adj_list)) 
if(choice=="3"):
	print("convert incidence matrix to adjacency list")
	incident_matrix = [[1, 1, 0, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0],
                          [1, 0, 0, 1, 0, 0],
                          [1, 0, 0, 0, 1, 0],
                          [1, 0, 0, 0, 0, 1],
                          [0, 1, 1, 0, 0, 0],
                          [0, 1, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 1],
                          [0, 0, 1, 1, 0, 0],
                          [0, 0, 1, 0, 1, 0],
                          [0, 0, 1, 0, 0, 1],
                          [0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 1, 0, 1],
                          [0, 0, 0, 0, 1, 1]]
	print("incidence matrix")
	pprint.pprint(incident_matrix)
	print("adjacency list")
	
	pprint.pprint(incident_matrix_to_adjacency_list(incident_matrix))
if(choice=="4"):
	print("adjacency list to adjacency matrix")
	adj_list = {0: [1, 2, 3, 4, 5],
                     1: [0, 2, 3, 4, 5],
                     2: [0, 1, 3, 4, 5],
                     3: [0, 1, 2, 4, 5],
                     4: [0, 1, 2, 3, 5],
                     5: [0, 1, 2, 3, 4]}
	print("adjacency list")
	pprint.pprint(adj_list)
	print("adjacency matrix")
	
	pprint.pprint(adjacency_list_to_adjacency_matrix(adj_list))
if(choice=="5"):
	print("adjacent matrix to incidence matrix")
	matrix = []
	matrix.append([0, 1, 1, 1, 1, 1])
	matrix.append([1, 0, 1, 1, 1, 1])
	matrix.append([1, 1, 0, 1, 1, 1])
	matrix.append([1, 1, 1, 0, 1, 1])
	matrix.append([1, 1, 1, 1, 0, 1])
	matrix.append([1, 1, 1, 1, 1, 0])
	print("adjacent matrix")
	pprint.pprint(matrix)
	print("Incident matrix")
	
	pprint.pprint(adjacency_matrix_to_Incidence_matrix(matrix))
if(choice=="6"):
	print("Incident matrix to adjacent matrix")
	incident_matrix = [[1, 1, 0, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0],
                          [1, 0, 0, 1, 0, 0],
                          [1, 0, 0, 0, 1, 0],
                          [1, 0, 0, 0, 0, 1],
                          [0, 1, 1, 0, 0, 0],
                          [0, 1, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 0],
                          [0, 1, 0, 0, 0, 1],
                          [0, 0, 1, 1, 0, 0],
                          [0, 0, 1, 0, 1, 0],
                          [0, 0, 1, 0, 0, 1],
                          [0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 1, 0, 1],
                          [0, 0, 0, 0, 1, 1]]
	print("Incident Matrix")
	pprint.pprint(incident_matrix)
	print("adjacent matrix")
	pprint.pprint(incident_matrix_to_adjacency_matrix(incident_matrix))
	
