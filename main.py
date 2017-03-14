from k_means import *
from PIL import Image
import random
import os

def iteracion(bin_dat,k,scatter,label_color,graph_color,folder):
	#Resultados del clasificador
	c = (centrar(np.array(bin_dat[:,:4]),k))[1]
	colores = []
	# Revisando conjuntos para casa caso
	for i in range(len(bin_dat)):
		revisar = bin_dat[i,:4]
		j = k-1
		while (j >= 0) :
			if ((c[j] == np.array(revisar)).all(axis=1)).any():
				colores.append(j)
				j = 0
			j=j-1

	#ScatterPlot de las 2 primeras variables
	if scatter:
		for i in range(k):
			plt.scatter(np.array(c[i])[:,0],np.array(c[i])[:,1],s=50, alpha = 1 ,c=graph_color[i])
		plt.savefig(folder+'/k_scatter_'+str(k)+'.png')

	#Creacion de la imagen por pixeles clasificada
	img = Image.new( 'RGB', (300,200), "black")
	pixels = img.load()
	for i in range(15):
	 for j in range (10):
		pixels[20*i,20*j] = label_color[colores[i*10+j]]
		for m in range (20):
			for l in range(20):
				pixels[20*i+m,20*j+l] = label_color[colores[i*10+j]]
	img.save(folder+'/Imagen_K'+str(k)+'.jpg')


#Lectura del archivo y organizacion de los datos
try:
	os.makedirs("Ejercicio_a")
except OSError:
    pass
try:
	os.makedirs("Ejercicio_b")
except OSError:
    pass

lectura = np.loadtxt('bezdekIris.data',dtype=str,delimiter=",")
bin_dat = np.matrix(map(to_ternary,lectura),dtype=np.float)
lc = range(130)
gc = range(130)
for i in range(130):
	lc[i]= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	gc[i]= '#%02x%02x%02x' % lc[i]

#Ejercicio a
iteracion(bin_dat,2,1,lc,gc,"Ejercicio_a")
iteracion(bin_dat,3,1,lc,gc,"Ejercicio_a")
iteracion(bin_dat,4,1,lc,gc,"Ejercicio_a")
iteracion(bin_dat,5,1,lc,gc,"Ejercicio_a")

#Ejercicio b
iteracion(bin_dat,2,0,lc,gc,"Ejercicio_b")
iteracion(bin_dat,4,0,lc,gc,"Ejercicio_b")
iteracion(bin_dat,8,0,lc,gc,"Ejercicio_b")
iteracion(bin_dat,16,0,lc,gc,"Ejercicio_b")
iteracion(bin_dat,32,0,lc,gc,"Ejercicio_b")
iteracion(bin_dat,64,0,lc,gc,"Ejercicio_b")
iteracion(bin_dat,128,0,lc,gc,"Ejercicio_b")