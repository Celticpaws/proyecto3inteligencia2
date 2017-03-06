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


def leer_archivo(N, k):

    n = float(N)/k
    casos = []
    for i in range(k):
        c = (random.uniform(-1, 1), random.uniform(-1, 1))
        s = random.uniform(0.05,0.5)
        x = []
        while len(x) < n:
            a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
            if abs(a) < 1 and abs(b) < 1:
                x.append([a,b])
        casos.extend(x)
    casos = np.array(casos)[:N]
    return casos

k = 6
lectura = np.loadtxt('bezdekIris.data',dtype=str,delimiter=",")
casos = lectura[:,0:4]
resultados = lectura[:,4]


c = (centrar(casos,k))[1]
p = promedio(c,k)

label_color = {0 : '#FF0000',1 : '#FFFF00',2 : '#0033CC',3 : '#00CC00',4 : '#660099',5 : '#FF9900',6 : '#000000',}


for i in range(k):
    plt.scatter(np.array(c[i])[:,0],np.array(c[i])[:,1],s=50, alpha = 0.5 ,c=label_color[i])
    plt.scatter(np.array(p[i])[0],np.array(p[i])[1],s=200, alpha = 1 ,c=label_color[i], marker="*")
plt.show()
