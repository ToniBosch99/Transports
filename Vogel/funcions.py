import numpy as np

def Vogel(Mab, oferta ,demanda):

    ni, nj= np.shape(Mab)

    var = np.sum(oferta) - np.sum(demanda) 

    if var > 0:
        Z= np.zeros((ni,1))
        Mab = np.c_[Mab, Z]
        print(Mab)
        demanda = np.append(demanda, [var])

    elif var < 0:
        Z=np.zeros((1,nj))
        Mab = np.r_[Mab, Z]
        oferta = np.append(oferta, [-1*var])
       
    print(Mab)
    Mab0=Mab

    ni, nj= np.shape(Mab)

    Mc = np.zeros((ni,nj))
    noferta = ni
    ndemanda = nj
    cont = 0

    while (noferta>1) and (ndemanda>1):
        cont=cont+1
        print('-------------------------------\n')
        sca = np.zeros((1,ni))
        scb = np.zeros((1,nj))
        print(cont)
        
        for i in range(ni):
             V = Mab[i,:]
             min1 = np.nanmin(V)
             V = V-min1
             if np.sum(V)>0:
                sca[0,i] = np.nanmin(V[V>0])
             else:
                sca[0,i] = 0

        noferta -=1
        ndemanda -=1
        
        for j in range(nj):
            V=Mab[:,j]
            min1 = np.nanmin(V)
            V=V-min1
            if np.sum(V)>0:
                scb[0,j] = np.nanmin(V[V>0])
            else:
                scb[0,j] = 0
             
        print('sca:', sca)
        print('scb:', scb)  


        sc=np.append(sca, scb)
        print(sc)
        Ps1=[]
        for i in range(len(sc)):
            if sc[i]==max(sc):
                Ps1.append(i)
        
        print(Ps1)

        
        Vs=[]
        Ps2=[]
        D=[]
        for k in range(len(Ps1)):
            if Ps1[k] <= ni:      #Ps1 FILA
                V = Mab[Ps1[k],:]
                minV=np.min(V)
                indMin = np.argmin(V)
                Vs.append(minV)
                Ps2.append(indMin) #Ps2 COLUMNA
                D.append(min(oferta[Ps1[k]],demanda[Ps2[k]]))
            else:                          #Ps1-ni COLUMNA
                V = Mab[:,Ps1[k]-ni]
                minV=np.min(V)
                indMin = np.argmin(V)
                Vs.append(minV)
                Ps2.append(indMin) #Ps2 COLUMNA
                D.append(min(oferta(Ps2(k)),demanda(Ps1(k)-ni)))
        
        
        for k in range(len(Ps1)):
            if k==1:
                a=Vs[k]
                b=k
            else:
                if a > Vs[k]:
                    a = Vs[k]
                    b = k
                elif (a==Vs[k]) and (D[b]< D[k]):
                        a=Vs[k]
                        b=k

        print(Vs,Ps2, D)
    #     if Ps1(b)<=ni                       %Ps1 FILA
    #         V=[oferta(Ps1(b)) demanda(Ps2(b))];      %Ps2 COLUMNA
    #         [c,d]=min(V);
    #         oferta(Ps1(b))=oferta(Ps1(b))-c;
    #         demanda(Ps2(b))=demanda(Ps2(b))-c;
    #         Mc(Ps1(b),Ps2(b))=c;
    #         if d==1
    #             Mab(Ps1(b),:)=NaN;
    #         else
    #             Mab(:,Ps2(b))=NaN;
    #         end
    #         fprintf('* %d. PASO: (%d,%d)\n',cont,Ps1(b),Ps2(b));
    #     else                                %Ps1-ni COLUMNA
    #         V=[oferta(Ps2(b)) demanda(Ps1(b)-ni)];   %Ps2 FILA
    #         [c,d]=min(V);
    #         oferta(Ps2(b))=oferta(Ps2(b))-c;
    #         demanda(Ps1(b)-ni)=demanda(Ps1(b)-ni)-c;
    #         Mc(Ps2(b),Ps1(b)-ni)=c;
    #         if d==1
    #             Mab(Ps2(b),:)=NaN;
    #         else
    #             Mab(:,Ps1(b)-ni)=NaN;
    #         end
    #         fprintf('*  %d. PASO: (%d,%d)\n',cont,Ps2(b),Ps1(b)-ni);
    #     end
        
    #     noferta=0;
    #     for i=1:ni
    #         if oferta(i)>0
    #         noferta=noferta+1;
    #         end
    #     end
        
    #     ndemanda=0;
    #     for j=1:nj
    #         if demanda(j)>0
    #         ndemanda=ndemanda+1;
    #         end
    #     end
    #     Mab
    #     oferta
    #     demanda

    # end


    # for i=1:ni
    #     for j=1:nj
    #         if Mab(i,j)>0
    #             c=min(oferta(i),demanda(j));
    #             Mc(i,j)=c;
    #             oferta(i)=oferta(i)-c;
    #             demanda(j)=demanda(j)-c;
    #         end
    #     end
    # end
    # fprintf('----- SOLUCION-----\n');

    # end