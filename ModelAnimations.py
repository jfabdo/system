

class Character():

    def __init__(self,model=None, weaponleft=None,weaponright=None,magic=None) -> None:
        if model == None:
            self.character = Actor(path[0]+'/models/ball.bam', {
                    'walk': path[0]+'/models/bouncing ball.bam',
                    'jump': path[0]+'/models/jumping ball.bam'
                })
        else:
            self.character = model
        
        if weaponleft == None:
            self.weaponleft = None
        elif weaponleft == 'elf sword':
            self.weaponleft = 'elf sword'
        else:
            self.weaponleft = weaponleft
        
        if weaponright == None:
            self.weaponright = None
        elif weaponright == 'elf sword':
            self.weaponright = 'elf sword'
        else:
            self.weaponright = weaponright
        
        if magic == None:
            self.magic = None
        else:
            self.magic = magic
    
    def swing(self):
        pass

    def jump(self):
        pass

    def chargespell(self):
        pass
    
    def shootspell(self):
        pass

    