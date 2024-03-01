class Equipo:
    def __init__(self, nom, i1, i2, i3, slogan):
        self.nom = nom
        self.int1 = i1
        self.int2 = i2
        self.int3 = i3
        self.slogan = slogan
    
    def __str__(self):
        integrantes = f"""
        Integrante 1: {self.int1}
        Integrante 2: {self.int2}
        Integrante 3: {self.int3}
        Slogan: {self.slogan}
        """
        return integrantes

class FS3:
    def __init__(self, equipos):
        self.equipos = equipos
    
    def __str__(self):
        equipos_str = ""
        for idx, equipo in enumerate(self.equipos, start=1):
            equipos_str += f"Equipo {idx}: {equipo.nom}\n{str(equipo)}\n{'-' * 20}\n"
        return equipos_str

# Crear instancias de Equipo
e1 = Equipo("Los =^UwU^=", "Leonardo Alberto Gonzáles Carmona - 19550747", "Norma Graciela Mendoza Ruiz - C16550498", "Jonathan Durán Mendoza - 20550401", "Respiración de Programación, Pose de HTML, Codificar")
e2 = Equipo("Toyota legacy", "Israel Chacon Rojo - 21550250", "Dilan Mauricio Garcia Hernandez - 21550132", "Jesus Elias Sierra Ruiz - 21550135", "Transformamos líneas de código en experiencias excepcionales")
e3 = Equipo("Pingüinos Galácticos", "Yahir Antonio Monje Ochoa - 20550740", "Yesica Cristina Rodriguez Renteria - 20550739", "", "SIC•PARVIS•MAGNA")
e4 = Equipo("Los 3 Mosqueteros", "Dania Denisse Benavides Figueroa - 20550402", "Erick Lozano Duarte - 20550353", "Ana Cristina Valenzuela Ruiz - 20550380", "Todos para uno, uno para todos")
e5 = Equipo("WebHeros", "Jesus Manuel Arellano Merendon - 21550158", "Axel Felipe Reyes Valadez - 21550156", "Luis Daniel Delgado Enriquez - 21550145", "La verdad solo se puede encontrar en un lugar: El codigo")
e6 = Equipo("Los Polystation", "Erick Fernando Siqueiros Zúñiga - 21550138", "Paulina Ixchel Arreguin Ruiz - 20550417", "", "Conectando el futuro, hoy")

equipos_fs3 = FS3([e1, e2, e3, e4, e5, e6])

print(equipos_fs3)
