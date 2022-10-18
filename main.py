import cv2 #Bibliotexa usada para ler a img
import matplotlib.pyplot as plt #Biblioteca usada para visualizar as operações

img = cv2.imread("meteor_challenge_01.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Convertendo a matriz de BGR para RGB

m,n,cor = img.shape
#print("Altura:",m)
#print("Largura:",n)
#print("Cores:",cor)

meteoro = 0
estrela = 0
agua = 0

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#Iniciando varredula simples na matriz
for i in range(m):
    for j in range(n):
        #print(img[i][j])
        if img[i][j][0] == 255:
            if img[i][j][1] == 0 and img[i][j][2] == 0: #Testa se é um meteoro                
                meteoro = meteoro + 1
                ax.add_patch(plt.Circle((j, i), 1, color="purple", linewidth=2, fill=False)) #Circula o meteoro de roxo
                for k in range(i,704,1):
                    if img[k][j][0] == 0 and img[k][j][1] == 0 and img[k][j][2] == 255:
                        agua = agua + 1
                        ax.add_patch(plt.Circle((j, i), 1, color="red", linewidth=2, fill=False)) #Circulas o meteoro que irá cair na agua de vermelho
                        break
                    
            if img[i][j][1] == 255 and img[i][j][2] == 255: #Testa se é uma estrela
                estrela = estrela + 1
                ax.add_patch(plt.Circle((j, i), 1, color="black", linewidth=2, fill=False)) #Circula a estrela de preto

print("Estrelas:",estrela)
print("Meteoros:",meteoro)
print("Meteros caindo na agua:",agua)
ax.set_axis_off()
plt.imshow(img)
plt.show()