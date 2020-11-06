import numpy as np  #Library for support for large, multi-dimensional arrays and matrices

#Table for MIN Ejercicio 1
Table = np.array(((1, 0, 1000), #Constraints
                  (0, 1, 2000),   #Constraints
                  (1, 0, 0), #Slack variables
                  (0, 1, 0), #Slack variables
                  (0.55, 0.23, 0.0))) #Z

# #Table for MIN Ejercicio 2
# Table = np.array(((-0.2, -0.32, -0.25), #Constraints
#                   (1, 1, 1),   #Constraints
#                   (-1, -1, -1), #Slack variables
#                   (1, 0, 0), #Slack variables
#                   (0, 1, 0), #Slack variables
#                   (80, 60, 0.0))) #Z


# #Table for MIN Ejercicio 3
# Table = np.array(((0.1, 0.3, 0.1, 12), #Constraints
#                   (0.2, 0.1, 0.1, 16),   #Constraints
#                   (1, 0, 0, 0), #Slack variables
#                   (0, 1, 0, 0), #Slack variables
#                   (0, 0, 1, 0), #Slack variables
#                   (10, 12, 8, 0.0))) #Z

# #Table for MAX Ejercicio 4
# Table = np.array(((0, 1, 1, 1, 0, 30), #Constraints
#                   (0, 0.2, 1, 0, 1, 300),   #Constraints
#                   (700, -480, -80, 0, 0, 0.0))) #Z


# #Table for MIN Ejercicio 5
# Table = np.array(((1, 1, 1, 1, 1, 1, 1000), #Constraints
#                   (0.36, 0.24, 0.05, 0.31, 0.29, 0, 0),   #Constraints
#                   (-0.06, 0.06, 0.25, -0.01, 0.01, 0, 0), #Slack variables
#                   (0.06, 0.09, 0.22, -0.13, 0.135, 0, 0), #Slack variables
#                   (0.29, 0.26, 0.13, 0.48, 0.485, 0, 0), #Slack variables
#                   (-0.07, 0.02, 0.08, 0.16, 0.19, 0, 0), #Slack variables
#                   (0.27, 0.18, 0.12, 0.04, 0.11, 0, 0), #Slack variables
#                   (0, 0, 0, -0.02, -0.025, 0.97, 0), #Slack variables
#                   (-0.8, -0.8, -0.8, 1.2, 1.2, 0, 0), #Slack variables
#                   (1.2, 1.2, 1.2, -0.8, -0.8, 0, 0), #Slack variables
#                   (1, 0, 0, 0, 0, 0, 0),
#                   (0, 1, 0, 0, 0, 0, 0),
#                   (0, 0, 1, 0, 0, 0, 0),
#                   (0, 0, 0, 1, 0, 0, 0),
#                   (0, 0, 0, 0, 1, 0, 0),
#                   (0, 0, 0, 0, 0, 1, 0),
#                   (22, 31, 45, 17, 15, 125, 0.0))) #Z

decision = input("Max or Min: ") #Deciding if is maximization or minimization
variables = input("No. variables: ")  #How many variables

def maximization(var):
    for i in range(var):    #Loop to print the variables
        if (sum(Table[:,i+1])==1):  #Check if the column is == 1 (Finding X and check if is the real variable)
            rowX = np.where(Table[:,i+1]==1)   #Get the row of the variable X
            x = Table[int(rowX[0])][-1]    #Save the solution for X[i]
        else:
            x = 0   #If there is no solution assign 0
        print("X"+str(i+1)+": "+str(x)) #Print the variables X[i]
    print("Z:", Table[-1][-1])    #Print function Z

def minimization(var):
    for i in range(var):    #Loop to print the variables
        x = TableT[-1][-2-i]    #Get the row of the variable X
        print("X"+str(i+1)+": "+str(x)) #Print the variables X[i]
    print("Z:", TableT[-1][-1])    #Print function Z

def min():
    flag = 1 #Flag to know if we finished (There is no negatives on last row (Z))
    while(flag != 0):   #Loop to remove the negatives on Z
        radQuots = []  #Array for the radius quotient
        minFunZ = np.amin(TableT[-1][:])   #Find the min of the last row (Z)
        pivotC = np.where(TableT[-1][:] == minFunZ) #Find the column of the minFunZ
        if minFunZ < 0:  #If the min of function Z is < 0
            positivesRows = np.where((TableT[:,pivotC[0][0]] > 0))  #Getting the positives values for the pivot column
            for i in range(len(positivesRows[0])):     #Getting the min radius quotient 
                radQuot = (TableT[positivesRows[0][i]][-1])/(TableT[positivesRows[0][i]][pivotC[0][0]]) #Dividing the radius quotient
                radQuots.append(radQuot)  #Puttin them on a list
                pivotQuot = np.amin(radQuots)  #Getting the min of the radQuots
                samePivotQuot = [j for j, samePivotQuot in enumerate(radQuots) if samePivotQuot == pivotQuot] #Saving all the min radius quotient
                pivotR = positivesRows[0][int(samePivotQuot[0])]  #If there is more than 1 min radius quotient select the first one
            TableT[pivotR][:] = (TableT[pivotR][:])/(TableT[pivotR][pivotC[0][0]]) #Recalculate the pivotR, that it will be our objective row
            for i in range(len(TableT)):   #Recalculating the rows remaning
                if (i != pivotR):  #Modifying all but the objective row
                    TableT[i][:] = TableT[i][:] - (TableT[i][pivotC[0][0]]*TableT[pivotR][:])   #Formula to calculate the new rows
        else:
            flag = 0    #There is no negative numbers in the last row (funZ)
    #print(TableT) #Printing the entire table

def max():
    flag = 1 #Flag to know if we finished (There is no negatives on last row (Z))
    while(flag != 0):   #Loop to remove the negatives on Z
        radQuots = []  #Array for the radius quotient
        minFunZ = np.amin(Table[-1][:])   #Find the min of the last row (Z)
        pivotC = np.where(Table[-1][:] == minFunZ) #Find the column of the minFunZ
        if minFunZ < 0:  #If the min of function Z is < 0
            positivesRows = np.where((Table[:,pivotC[0][0]] > 0))  #Getting the positives values for the column pivot
            for i in range(len(positivesRows[0])):     #Getting the min radius quotient 
                radQuot = (Table[positivesRows[0][i]][-1])/(Table[positivesRows[0][i]][pivotC[0][0]]) #Dividing the radius quotient
                radQuots.append(radQuot)  #Puttin them on a list
                pivotQuot = np.amin(radQuots)  #Getting the min of the radQuots
                samePivotQuot = [j for j, samePivotQuot in enumerate(radQuots) if samePivotQuot == pivotQuot] #Saving all the min radius quotient
                pivotR = positivesRows[0][int(samePivotQuot[0])]  #If there is more than 1 min radius quotient select the first one
            Table[pivotR][:] = (Table[pivotR][:])/(Table[pivotR][pivotC[0][0]]) #Recalculate the pivotR
            for i in range(len(Table)):   #Recalculating the rows remaning
                if (i != pivotR):  #Modifying all but the objective row
                    Table[i][:] = Table[i][:] - (Table[i][pivotC[0][0]]*Table[pivotR][:])   #Formula to calculate the new rows
        else:
            flag = 0    #There is no negative numbers in the last row (funZ)

if(decision == "Max" or decision == "max"): #If is maximization
    max()   #Calling the max function
    print(Table)
    maximization(int(variables))    #Calling the maximization function passing the number of variables
elif(decision == "Min" or decision == "min"):  #If is minimization
    TableT = np.transpose(Table)    #Transposing the original Table to do the dual method
    TableT[-1][:] *= -1 #Multiplying by -1 the last row (Z) (To make the equality)
    print(TableT)
    min()   #Calling the min function
    minimization(int(variables))    #Calling the maximization function passing the number of variables