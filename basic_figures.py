class Vertex:
    def __init__(self, name, coordinates=None):
        self.name = name
        self.coordinates = coordinates
        

class Triangle(Vertex):
    def __init__(self, name, coordinates=None):
        super().__init__(name, coordinates)
        self.vertices = [x for x in name]

    def get_vertices(self):
        return self.vertices
        
    def get_sides(self):
        sides = []
        for i in range(len(self.vertices)):
            side = self.vertices[i] + self.vertices[(i+1)%3]
            sides.append(side)
        return sides

class Square(Vertex):
    def __init__(self, name, coordinates=None):
        super().__init__(name, coordinates)
        self.vertices = [x for x in name]
    
    def get_vertices(self):
        return self.vertices

    def get_sides(self):
        sides = []
        for i in range(len(self.vertices)):
            side = self.vertices[i] + self.vertices[(i+1)%4]
            sides.append(side)
        return sides

class Pentagon(Vertex):
    def __init__(self, name, coordinates=None):
        super().__init__(name, coordinates)
        self.vertices = [x for x in name]
        
    def get_vertices(self):
        return self.vertices
    
    def get_sides(self):
        sides = []
        for i in range(len(self.vertices)):
            side = self.vertices[i] + self.vertices[(i+1)%5]
            sides.append(side)
        return sides

#example
# triangle = Triangle("ABC", coordinates=[(1,1), (2,3), (3,1)])
# print(triangle.get_vertices())
# print(triangle.get_sides())
# print(triangle.coordinates)

# square = Square("ABCD", coordinates=[(0,0), (0,1), (1,1), (1,0)])
# print(square.get_vertices())
# print(square.get_sides())
# print(square.coordinates)

# pentagon = Pentagon("ABCDE", coordinates=[(0,0), (0,1), (1,2), (2,2), (2,0)])
# print(pentagon.get_vertices())
# print(pentagon.get_sides())
# print(pentagon.coordinates)


#get outer angles(꼭짓점 말고 다른 점 있는지 확인하기)
#대각선 선분 구하기, 개수 세기, 개수 공식

#삼각형의 세 내각의 합은 180도이다 이용하기

#n각형의 내각의 크기의 합; 삼각형의 개수 이용해서 구하기


class circle():
    #중심과 반지름
    pass

class circle_extend(circle):
    #호
    #현
    #활꼴
    pass

class circular_sector(circle):
    pass