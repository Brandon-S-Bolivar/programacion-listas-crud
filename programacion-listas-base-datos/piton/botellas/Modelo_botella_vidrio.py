from Modelo_botella import Botella

class Botella_vidrio(Botella):
    
    def __init__(self, Material_3):
        super().__init__(Material_3)
        self.Transporte=""
        self.compatibilidad=""
        self.Reutilizable=""
        self.cierre=""
        self.resistencia=""
    
    def Definir_datos_vidrio(self,transporte_1,compatibilidad_1,reutilizable_1,cierre_1,resistencia_1,Capacidad_2,Forma_2,Diseño_2,Grabados_2):
        self.Transporte=transporte_1
        self.compatibilidad=compatibilidad_1
        self.Reutilizable=reutilizable_1
        self.cierre=cierre_1
        self.resistencia=resistencia_1
        super().Contener_liquido(Capacidad_2)
        super().forma_botella(Forma_2)
        super().diseño_botella(Diseño_2)
        super().Grabados_botella(Grabados_2)
        
        
    def imprimir_info(self):
        super().imprimir_info()
        print("----------------------------------------------------------------------------------------")   
        print(f"el transporte es: {self.Transporte} \nla compatibilidad es: {self.compatibilidad} \nes reutilizable: {self.Reutilizable} \ncon un cierre: {self.cierre} \nresistencia de liquido: {self.resistencia}")