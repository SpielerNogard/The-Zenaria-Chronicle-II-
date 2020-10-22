
class MusicController(object):
    def __init__(self):
        self.Villages = [[10,10],[11,10],[12,10],[11,11],[10,11],[10,12],[11,12],[12,15],[13,15],[12,16],[13,16],[6,4],[6,5],[7,5],[7,6],[6,6]]
        self.Castle = [[12,2],[12,1],[12,0],[13,4],[12,4],[14,4],[15,4],[13,3],[12,3],[14,3],[15,3],[13,2],[14,2],[15,2],[14,1],[13,1]]
        self.Dungeons = [[39,12],[40,0],[40,1],[40,2],[40,3],[40,4],[41,0],[41,1],[41,2],[41,3],[41,4],[42,0],[42,1],[42,2],[42,3],[42,4],[43,0],[43,2],[43,3],[43,4],[43,1]]
        self.music = 1

    def check_music(self,chunkx,chunky):
        Chunk = []
        Chunk.append(chunkx)
        Chunk.append(chunky)
        if Chunk in self.Villages :
            self.music = 2
        elif Chunk in self.Castle : 
            self.music = 3
        elif Chunk in self.Dungeons : 
            self.music = 0
        else:
            self.music = 1
        