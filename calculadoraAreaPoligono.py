
class Rectangle():
    def __init__(self):
        self.width = 0
        self.heigth = 0

    def set_width(self, width):
        self.width = width
        return True
    
    def set_height(self, heigth):
        self.heigth = heigth
        return True
        
    
    def get_area(self):
        return self.width * self.heigth
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.heigth)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        altura = self.width
        ancho = self.heigth

        if altura < 51 and ancho < 51:
            for i in range(1 , ancho+1):
                for i in range(1, altura+1):
                    print('*', end='')
                print(' ')
  
    def get_amount_inside(self, forma, formaAIntroducir):
        altura = self.heigth
        ancho = self.width
        
        formaAIntroducir == altura
                    
        multi = altura * ancho 
        contador = 0
        
        multiIntroducir = formaAIntroducir * formaAIntroducir
        
        
        formaAIntroducir = 0
        while formaAIntroducir < multi:
            formaAIntroducir = formaAIntroducir + multiIntroducir
            contador = contador + 1
            print('cabe ', contador, 'Veces')
            
            
        # print(multi)
        
        
        
        # cantidad = 0
        # altuta = formaAIntroducir
        # if forma == 'rectangulo':
            
        #     while cantidad <= formaAIntroducir:
                
        #         if formaAIntroducir > self.width:
        #             return print('es mas ancho')
                
        #         if formaAIntroducir > self.heigth:
        #             return print('es mas alto')

        #         print('si cabe')
        #         altuta = altuta * 2
        #         cantidad = cantidad + 1
        #         print(cantidad)
            
        # elif forma == 'cuadrado':
        #     pass
        
        # return cantidad



class Square(Rectangle):
    
    def __init__(self, side):    
        self.side = side
        
    def set_side(self):
        print(f"Soy {self.width}")
        
    
    
    

rectangulo = Rectangle()
rectangulo.set_width(4)
rectangulo.set_height(8)

# rectangulo.get_picture()
rectangulo.get_amount_inside('rectangulo', 4)

cuadrado = Square(side=9)
cuadrado.set_width(4)
cuadrado.set_height(8)
cuadrado.set_side()

