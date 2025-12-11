from Modelo_botella import Botella

class Botella_plastico(Botella):
    def __init__(self,Material_2):
        super().__init__(Material_2)
        self.tinte=""
        self.Reutilizable=""
        self.cierre=""
        self.resistencia=""
        
    def Definir_datos_plasti(self,tinte_1,reutilizable_1,cierre_1,resistencia_1,Capacidad_1,Forma_1,Diseño_1,Grabados_1):
        self.tinte=tinte_1
        self.Reutilizable=reutilizable_1
        self.cierre=cierre_1
        self.resistencia=resistencia_1
        super().Contener_liquido(Capacidad_1)
        super().forma_botella(Forma_1)
        super().diseño_botella(Diseño_1)
        super().Grabados_botella(Grabados_1)
        
    def imprimir_info(self):
        super().imprimir_info()
        print("----------------------------------------------------------------------------------------")
        print(f"el tinte es: {self.tinte} \nes reutilizable: {self.Reutilizable} \ncon un cierre: {self.cierre} \nresistencia de liquido: {self.resistencia}")