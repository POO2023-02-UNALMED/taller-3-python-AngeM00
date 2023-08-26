class TV: 
    _numTv = 0
  
    def __init__(self, marca, estado):
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._marca = marca
        self._estado = estado
        self._numTv += 1
    
    #Metodos get y set para los atributos marca,canal,volumen,precio y control
    def getMarca(self):
        return self._marca
        
    def setMarca(self,marca):
        self._marca = marca
    
    def getCanal(self):
        return self._canal
    
    def setCanal(self,canal):
        if self._estado == 1:
            self._canal = canal
    
    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self,volumen):
        self._volumen = volumen
        
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self,precio):
        self._precio = precio
        
    def setControl(self,control):
        self._control = control
        
    def getControl(self):
        return self._control
    
    def turnOn(self):
        self._estado = 1
    
    def turnOff(self):
        self._estado = 0
    
    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado == 1 and self._canal < 120:
            self._canal += 1
    
    def canalDown(self):
        if self._estado == 1 and self._canal > 1:
            self._canal -= 1
    
    def volumenUp(self):
        if self._estado == 1 and self._canal < 7:
            self._volumen += 1
    
    def volumenDown(self):
        if self._estado == 1 and self._volumen > 0:
            self._volumen -= 1
    
    @classmethod
    def getNumTV(cls):
        return cls._numTv
    
    @classmethod
    def setNumTV(cls,num):
        cls._numTv = num
    
    

        