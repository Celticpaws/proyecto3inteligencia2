from k_means import *
from PIL import Image

try:
    k = int(raw_input("Introduzca un k: "))
except Exception as e:
    k = 3
print(k)

#Lectura del archivo y organizacion de los datos
lectura = np.loadtxt('bezdekIris.data',dtype=str,delimiter=",")
bin_dat = np.matrix(map(to_ternary,lectura),dtype=np.float)

#Resultados del clasificador
c = (centrar(np.array(bin_dat[:,:4]),k))[1]
label_color = {0 : (255,255,0),1 : (0,0,255),2 : (255,0,0),3 : (255,0,255),4 : (0,255,255),5 : (0,255,0),6 : (255,255,255),}
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


#Creacion de la imagen por pixeles clasificada
img = Image.new( 'RGB', (300,200), "black")
pixels = img.load()
for i in range(15):
 for j in range (10):
	pixels[20*i,20*j] = label_color[colores[i*10+j]]
	for k in range (20):
		for l in range(20):
			pixels[20*i+k,20*j+l] = label_color[colores[i*10+j]]
img.show()
