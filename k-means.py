import numpy as np
import random
import matplotlib.pyplot as plt
 
def puntos_del_cluster(casos, media):
    clusters  = {}
    for x in casos:
        bestmukey = min([(i[0], np.linalg.norm(x-media[i[0]])) \
                    for i in enumerate(media)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters
 
def iteracion(media, clusters):
    nuevo_m = []
    keys = sorted(clusters.keys())
    for k in keys:
        nuevo_m.append(np.mean(clusters[k], axis = 0))
    return nuevo_m
  
def centrar(casos, K):
    viejo_m = random.sample(casos, K)
    media = random.sample(casos, K)
    while not (set([tuple(a) for a in media]) == set([tuple(a) for a in viejo_m])):
        viejo_m = media
        clusters = puntos_del_cluster(casos, media)
        media = iteracion(viejo_m, clusters)
    return(media, clusters)

def to_binary(row):
    if row[-1] == 'Iris-setosa':
        return np.append(row[:-1],"1.0")
    else:
        return np.append(row[:-1],"0.0")
v_to_binary = np.vectorize(to_binary)

def to_ternary(row):
    if row[-1] == 'Iris-setosa':
        return np.append(row[:-1],[1,0,0],axis=0)
    elif row[-1] == 'Iris-versicolor':
        return np.append(row[:-1],[0,1,0],axis=0)
    else:
        return np.append(row[:-1],[0,0,1],axis=0)
v_to_ternary = np.vectorize(to_ternary)

try:
    k = int(raw_input("Introduzca un k: "))
except Exception as e:
    k = 3
print(k)

lectura = np.loadtxt('bezdekIris.data',dtype=str,delimiter=",")
bin_dat = np.matrix(map(to_binary,lectura),dtype=np.float)
c = (centrar(np.array(bin_dat),k))[1]
print c
label_color = {0 : '#FF0000',1 : '#FFFF00',2 : '#0033CC',3 : '#00CC00',4 : '#660099',5 : '#FF9900',6 : '#000000',}
for i in range(k):
    plt.scatter(np.array(c[i])[:,0],np.array(c[i])[:,1],s=50, alpha = 0.5 ,c=label_color[i])
plt.show()
