import ast

class Chunk(object):
    def __init__(self,Screenwidth, Screenheight):
        #Standartauflösung 1024x576
        #StandartAssetgröße 32x32
        #Standart Assets in Breite 32
        #Standart Assets in Höhe 18

        self.screenwith = Screenwidth
        self.screenheight = Screenheight

        self.name = "Chunk"
        self.actual_Chunk = []
        self.realactual_chunk=[]
        self.realactual_chunk2 =[]
        self.Assetwidth = 32
        self.Assetheight = 32

        self.Assetheightscal = 0
        self.Assetwidthscal = 0

        self.calculate_Assetnumbers()
        
        self.geladener_chunk_x = -2
        self.geladener_chunk_y = -2
        
    def calculate_Assetnumbers(self):
        self.Assetwidth = self.screenwith/32
        self.Assetheight = self.screenheight/18

        self.Assetheightscal = self.Assetheight - 32
        self.Assetwidthscal = self.Assetwidth - 32


    def load_chunk(self,x,y):
        if self.geladener_chunk_x != x or self.geladener_chunk_y != y:
            Chunkname = "Chunks/chunk"+str(x)+"_"+str(y)+".txt"
            #print(Chunkname)
            self.actual_Chunk = open(Chunkname).read()
            self.actual_Chunk = ast.literal_eval(self.actual_Chunk)
            #for a in self.actual_Chunk:
            #print(a)
            
        
        #print(self.actual_Chunk)
        return(self.actual_Chunk)

