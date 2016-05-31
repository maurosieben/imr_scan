import os, subprocess, math, numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# arrays to save he1 and he2 data
he1_data =[]
he2_data =[]

# max decrease of he
diff_def = 0.1

# mp default value 
set_mp = 15.3

# mp value when valve opens
valv_mp = 16

# max cold head temperature
cht_max = 50

# temperature when sensor is unplugged
cht_disc = 27.3

prog_dir  = os.path.dirname(os.path.abspath(__file__))

# returns the percentage difference
def diff(old, new):
    res = (1-(new/old))*100
    return res

# checks mp values and generates a log file
def mpcheck():
    fw = open("%s/mp.log" %prog_dir, "w")
    fr = open("%s/data.csv" %prog_dir, "r")
    for lines in fr:
        line = lines.split(",")
        if float(line[8]) > set_mp:
            if float(line[8]) < valv_mp:
                fw.write("On %s high pressure, mp = %s \n" %(line[1],line[8]))
            else:
                fw.write("On %s open valve, mp = %s \n" %(line[1],line[8]))
        else:
            pass
    fw.close()
    fr.close()
    subprocess.Popen("gedit %s/mp.log  &" %prog_dir, stderr= subprocess.PIPE,stdout= subprocess.PIPE,shell=True)

# checks cht values and generates a log file    
def chtcheck():
    fw = open("%s/cht.log" %prog_dir, "w")
    fr = open("%s/data.csv" %prog_dir, "r")
    for lines in fr:
        line = lines.split(",")
        print float(line[4])
        if float(line[4]) > cht_max:
            fw.write("On %s hot cold head, cht = %s \n" %(line[1],line[4]))
            
        elif float(line[4]) == cht_disc:
            fw.write("On %s sensor disconnected, cht = %s \n" %(line[1],line[4]))
        else:
            pass
    fw.close()
    fr.close()
    subprocess.Popen("gedit %s/cht.log  &" %prog_dir, stderr= subprocess.PIPE,stdout= subprocess.PIPE,shell=True)



# plots He graph
def plot_he(array1,array2,array3,array4):
    plt.plot(array1, 'r')
    plt.plot(array2, 'b')
    plt.plot(array3, 'ro')
    plt.plot(array4, 'bo')
    red_patch = mpatches.Patch(color='red', label='He1')
    blue_patch = mpatches.Patch(color='blue', label='He2')
    plt.legend(handles=[red_patch])
    plt.legend(handles=[red_patch,blue_patch])
    plt.ylabel('He1/He2')
    plt.xlabel('Leitura')
    plt.show()
    
#print an array
def print_array(array):
    for iten in array:
        print iten    
        
#raise an array to the power p and returns the sum of it
def sum_p(array,p):
    array_2 = []
    for iten in array:
        array_2.append(math.pow(iten,p))
    return math.fsum(array_2)

#return array to the power p
def array_p(array,p):
    array_2 = []
    for iten in array:
        array_2.append(math.pow(iten,p))
    return array_2

# quadratic approximation
# references: http://ssdi.di.fct.unl.pt/comp/1112/aulas/teoricas/aulaT10.pdf
def adjcurve():
    fr = open("%s/data.csv" %prog_dir, "r+")
    global he1_data 
    global he2_data
    # measurements array
    leit = []
    count = 0
    for lines in fr:
        line = lines.split(",")
        he1_data.append(float(line[2]))
        he2_data.append(float(line[3]))
        leit.append(count)
        count = count + 1
    fr.close()
    m= 2
    n= len(leit)
    # first order sum
    he1_sum = math.fsum(he1_data)
    he2_sum = math.fsum(he2_data)
    leit_sum = math.fsum(leit)
    # averages
    he1_av = numpy.mean(he1_data)
    he2_av = numpy.mean(he2_data)
    leit_av = numpy.mean(leit)
    # second, third and forth order sum
    leit_sum2 = sum_p(leit, 2)
    leit_sum3 = sum_p(leit, 3)
    leit_sum4 = sum_p(leit, 4)
    #products of the arrays 
    he1xleit = numpy.multiply(he1_data, leit)
    he2xleit = numpy.multiply(he2_data, leit)
    leit2 = array_p(leit,2)
    he1xleit2 = numpy.multiply(he1_data, leit2)
    he2xleit2 = numpy.multiply(he2_data, leit2)
    # sum of the products
    he1xleit_sum = math.fsum(he1xleit)
    he2xleit_sum = math.fsum(he2xleit)
    he1xleit2_sum = math.fsum(he1xleit2)
    he2xleit2_sum = math.fsum(he2xleit2)
    
    #building the system
    N = numpy.array([[n, leit_sum, leit_sum2 ],[leit_sum, leit_sum2, leit_sum3], [leit_sum2, leit_sum3, leit_sum4]])

    he1_r = numpy.array([he1_sum, he1xleit_sum, he1xleit2_sum])
    he2_r = numpy.array([he2_sum, he2xleit_sum, he2xleit2_sum])

    #solving the system
    he1_a = numpy.linalg.solve(N,he1_r)
    he2_a = numpy.linalg.solve(N,he2_r)

    #building the aproximated functions
    he1 = he1_a[0] + numpy.multiply(leit,he1_a[1]) + numpy.multiply(leit2,he1_a[2])
    he2 = he2_a[0] + numpy.multiply(leit,he2_a[1]) + numpy.multiply(leit2,he2_a[2])
    return he1, he2

#chtcheck()
#mpcheck()
#plot_he()
he1,he2 = adjcurve()

plot_he(he1,he2,he1_data,he2_data)
#plot_he(he1_data,he2_data)
