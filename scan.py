import os, subprocess
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

diff_def = 0.1
set_mp = 15.3
valv_mp = 16 
cht_max = 50
cht_disc = 27.3
prog_dir  = os.path.dirname(os.path.abspath(__file__))

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
def plot_he():
    fr = open("%s/data.csv" %prog_dir, "r+")
    fw = open("%s/cht.log" %prog_dir, "w")
    count = 0
    he1_data =[]
    he2_data =[]
    for lines in fr:
        line = lines.split(",")
        he1_data.append(line[2])
        he2_data.append(line[3])
        count = count + 1
        
    fr.close()
    plt.plot(he1_data, 'r')
    plt.plot(he2_data, 'b')
    red_patch = mpatches.Patch(color='red', label='He1')
    blue_patch = mpatches.Patch(color='blue', label='He2')
    plt.legend(handles=[red_patch])
    plt.legend(handles=[red_patch,blue_patch])
    plt.ylabel('He1/He2')
    plt.xlabel('Leitura')
    plt.show()
    print count 
#he2_data.remove('He2')
#he1_data.remove('He1')

chtcheck()
mpcheck()
plot_he()
#print diff(79.1,79.0209)
