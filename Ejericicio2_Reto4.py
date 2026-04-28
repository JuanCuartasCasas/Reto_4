from typing import List
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
	
    def compute_distance(self, point: "Point"):
        distance = ((point.x - self.x)**2 + (point.y - self.y)**2)**0.5
        return distance 

    def __repr__(self):
        return f"(x: {self.x}, y: {self.y})"

class Line:
    def __init__(self, start_point: Point, end_point : Point):
        self.start_point = start_point 
        self.end_point = end_point
        self.length = start_point.compute_distance(end_point)




class Shape:
    
    def __init__(self, vertices: List):
        self._vertices: List = vertices
        self._edges: List = self.set_edges()
        self.inner_angles: List = self.compute_inner_angles(vertices)
        self.__is_regular: bool = self.set_is_regular()



    def get_is_regular(self):
        return self.__is_regular
    
    def get_vertices(self):
        return self._vertices
    
    def set_edges(self):

        for i in range(len(self._vertices)):
            edge = Line(self._vertices[i], self._vertices[i+1])
            self._edges.append(edge)

    def set_vertices(self, new_vertices: List[Point]):
	    
        self.__init__(new_vertices)
    
    
    def set_is_regular(self):
        if len(self._vertices) < 3:
            self.__is_regular = False
            return self.__is_regular

        side_lengths = [edge.length for edge in self._edges]
        first_length = side_lengths[0]
        sides_equal = all(abs(length - first_length) < 1e-9 for length in side_lengths)

        angles = self.inner_angles
        first_angle = angles[0]
        angles_equal = all(abs(angle - first_angle) < 1e-9 for angle in angles)

        self.__is_regular = sides_equal and angles_equal
        return self.__is_regular

    def compute_area(self):
        raise NotImplementedError("Debe implementarse un método 'compute_area()' a cáda subclase específica")

    def compute_perimeter(self):
        raise NotImplementedError("Debe implementarse un método 'compute_perimeter()' a cáda subclase específica")

    def compute_inner_angles(self, vertices):
        n = len(vertices)
        angles = []

        for i in range(n):
            p_prev = vertices[(i - 1) % n]
            p = vertices[i]
            p_next = vertices[(i + 1) % n]

            ux = p_prev.x - p.x
            uy = p_prev.y - p.y
            vx = p_next.x - p.x
            vy = p_next.y - p.y

            cross = ux * vy - uy * vx
            dot = ux * vx + uy * vy

            theta = math.atan2(cross, dot)
            interior = (math.pi - theta) % (2 * math.pi)

            angles.append(math.degrees(interior))

        return angles
       



class Rectangle(Shape):
    def __init__(self, vertices: List):
        super().__init__(vertices)
 
    def calculate_area(self):
        area = self.longer_length * self.smaller_length 
        return area  

    def calculate_perimeter(self):
        perimeter = 2*(self.smaller_length + self.longer_length)
        return perimeter



 

class Square(Rectangle):
    def __init__(self, ):
        super().__init__()


class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def set_vertices(self, new: Point):
        
        if len(self.vertices) != 3:
            print("El triangulo solamente debe poseer 3 ángulos")
            
        else:
            self.vertices.append(new)
	

class Isosceles(Triangle):
    def __init__(self):
        super().__init__()

class Equilateral(Triangle):
    def __init__(self):
        super().__init__()

class Scalene(Triangle):
    def __init__(self):
        super().__init__()

class TriRectangle(Triangle):
    def __init__(self):
        super().__init__()





























def main():
    punto1 = Point(4,3)
    punto2 = Point(2,2)
    linea1 = Line(punto1, punto2)
	
    print(linea1.length)



if __name__ == "__main__":
    main()
