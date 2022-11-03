import pyxel
import random

class vector2():
    def __init__(self,xv,yv):
        self.x = xv
        self.y=yv
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
v2 = vector2(5,2)
print(v2.x)
class snowflake():
    def __init__(self):
        self.pos = vector2(random.randint(1,pyxel.width),0)
        self.dir = vector2(random.randint(-3,3)/10,random.randint(3,5)/10)
    def draw(self):
        pyxel.rect(self.pos.x,self.pos.y,1,1,7)
    def update(self):
        self.pos += self.dir
    def canlive(self):
        if(self.pos.x < -0.5 or self.pos.x>pyxel.width or self.pos.y > pyxel.height):
            #print("delete at"+str(self.pos))
            return True

class App:
    def __init__(self):
        pyxel.init(128, 128)
        self.snowflakes = []
        self.x = 0
        self.lenghindex = 0
        self.cliche=""
        for x in range(20):
            self.snowflakes.append(snowflake())
        pyxel.run(self.update, self.draw)





    def update(self):
        if(pyxel.btnr(key=pyxel.KEY_SPACE)):
            self.cliche=""
            self.x += 1
            with open('cliches.txt') as f:
                lines = f.readlines()[random.randint(0,3969)]
                print(lines)
                for l in lines:
                    if(l==" "):
                        self.lenghindex+=1
                        if(self.lenghindex>3):
                            self.cliche += "\n"
                            self.lenghindex=0
                        self.cliche += l
                    else:
                        self.cliche += l

    def draw(self):
        pyxel.cls(0)
        for sn in self.snowflakes:
            if(sn.canlive()):
                self.snowflakes.remove(sn)

        for sn in self.snowflakes:
            sn.update()
            sn.draw()
        self.snowflakes.append(snowflake())
        pyxel.text(pyxel.width / 2-30, pyxel.height / 2, self.cliche, col=pyxel.COLOR_CYAN)

App()