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
