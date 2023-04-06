import random

class Element:
    def __init__(self,atomicNum,symbol,name):
        self.atomicNum = atomicNum
        self.symbol = symbol
        self.name = name
        while True:
            self.color = self.__Color()
            if self.color != "#050505":
                break;

    def clone(self):
        newElement = Element(self.atomicNum,self.symbol,self.name)
        newElement.color = self.color
        return newElement

    def __Color(self):
        color = ['#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        color = str(color)
        color = color.replace("['",'')
        color = color.replace("']",'')
        return color

    def __Color(self):
        code = (self.name.lower() + " " * (12 - len(self.name))).encode('utf-8')[:12]
        r, g, b = code[0], code[1], code[2]
        r, g, b = r * 5, g * 7, b * 11
        luminicent = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
        if luminicent > 0:
            r, g, b = r * 0.8, g * 0.8, b * 0.8
        return "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))

    def __Color(self):
        return self.__obtener_color_accesible()

    def __obtener_color_accesible(self):
        """
        Esta función toma dos valores hexadecimales que representan los colores
        de fondo y de texto, y devuelve un color de fondo que cumpla con los
        estándares de accesibilidad web.
        """

        fondo = ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        texto = '000000'
        
        # Convertir los valores hexadecimales a valores RGB
        r_fondo, g_fondo, b_fondo = tuple(int(fondo[i:i+2], 16) for i in (0, 2, 4))
        r_texto, g_texto, b_texto = tuple(int(texto[i:i+2], 16) for i in (0, 2, 4))
        
        # Calcular la luminosidad relativa de cada color
        luminosidad_fondo = (r_fondo / 255) * 0.2126 + (g_fondo / 255) * 0.7152 + (b_fondo / 255) * 0.0722
        luminosidad_texto = (r_texto / 255) * 0.2126 + (g_texto / 255) * 0.7152 + (b_texto / 255) * 0.0722
        
        # Calcular el contraste entre los dos colores
        contraste = (max(luminosidad_fondo, luminosidad_texto) + 0.05) / (min(luminosidad_fondo, luminosidad_texto) + 0.05)
        
        # Si el contraste es suficiente, devolver el color de fondo original
        if contraste >= 4.5:
            return '#' + fondo
        
        # De lo contrario, buscar un color de fondo que cumpla con los estándares de accesibilidad web
        color_accesible = None
        luminosidad_ideal = (luminosidad_texto + 0.05) / 0.2126
        
        for i in range(1, 11):
            # Calcular la luminosidad relativa del nuevo color
            luminosidad_nuevo = (luminosidad_ideal + 0.05 * i) / (i + 1 - 0.05)
            
            # Si el nuevo color tiene una luminosidad relativa válida, calcular su valor RGB
            if luminosidad_nuevo <= 0.8:
                a = 0.055 if luminosidad_nuevo <= 0.03928 else 0.055 + 0.5 * (luminosidad_nuevo - 0.04052) / (0.9884 - 0.04052)
                b = (luminosidad_nuevo - a) / 12.92 if luminosidad_nuevo <= 0.03928 else ((luminosidad_nuevo + 0.055) / 1.055) ** 2.4
                
                # Convertir los valores RGB a hexadecimales y devolver el nuevo color de fondo
                color_accesible = "#{:02x}{:02x}{:02x}".format(round(b * 255), round(b * 255), round(b * 255))
                break
        
        # Si no se encontró un color de fondo adecuado, devolver el color de fondo original
        if color_accesible is None:
            return "#" + fondo

        return color_accesible