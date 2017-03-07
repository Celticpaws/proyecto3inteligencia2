from k_means import *

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
