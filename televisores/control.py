class Control:
    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)
        
    def getTv(self):
        return self._tv
    
    def setTv(self,tv):
        self._tv = tv
    
    def turnOn(self):
        if self._tv != None:
            return self._tv.turnOn()
    
    def turnOff(self):
        if self._tv != None:
            return self._tv.turnOff()

    def canalUp(self):
        if self._tv != None:
            return self._tv.canalUp()
    
    def canalDown(self):
        if self._tv != None:
            return self._tv.canalDown()
    
    def volumenUp(self):
        if self._tv != None:
            return self._tv.volumenUp()
    
    def volumenDown(self):
        if self._tv != None:
            return self._tv.volumenDown()
    
    def setCanal(self,canal):
        if self._tv != None:
            return self._tv.setCanal(canal)
    
    def setVolumen(self,volumen):
        if self._tv != None:
            return self._tv.setVolumen(volumen)