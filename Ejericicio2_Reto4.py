from typing import List
import math

class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
	
    def compute_distance(self, point: "Point"):
        distance = ((point._x - self._x)**2 + (point._y - self._y)**2)**0.5
        return distance 

    def __repr__(self):
        return f"(x: {self._x}, y: {self._y})"

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, new_x: float):
        self._x = new_x

    def set_y(self, new_y: float):
        self._y = new_y


class Line:
    def __init__(self, start_point: Point, end_point : Point):
        self.start_point = start_point 
        self.end_point = end_point
        self.length = start_point.compute_distance(end_point)




class Shape:
    
    def __init__(self, vertices: List):
        self._vertices: List = vertices
        if len(vertices) < 3:
            self._edges: List = []
            self.inner_angles: List = []
            self.__is_regular: bool = False
        else:
            self._edges: List = self.set_edges()
            self.inner_angles: List = self.compute_inner_angles(vertices)
            self.__is_regular: bool = self.set_is_regular()

        


    def get_is_regular(self):
        return self.__is_regular
    
    def get_vertices(self):
        return self._vertices
    
    def set_edges(self):
        list_edges = []
        if not self._vertices:
            return list_edges
        for i in range(len(self._vertices)):
            edge = Line(self._vertices[i], self._vertices[(i + 1) % len(self._vertices)])
            list_edges.append(edge)
        return list_edges

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

        if n < 3:
            return angles

        for i in range(n):
            p_prev = vertices[(i - 1) % n]
            p = vertices[i]
            p_next = vertices[(i + 1) % n]

            ux = p_prev._x - p._x
            uy = p_prev._y - p._y
            vx = p_next._x - p._x
            vy = p_next._y - p._y

            dot = ux * vx + uy * vy

            norm_u = math.hypot(ux, uy)
            norm_v = math.hypot(vx, vy)
            if norm_u == 0 or norm_v == 0:
                angles.append(0.0)
                continue

            cos_theta = dot / (norm_u * norm_v)
            cos_theta = max(-1.0, min(1.0, cos_theta))
            angles.append(math.degrees(math.acos(cos_theta)))

        return angles
       



class Rectangle(Shape):
    def __init__(self, vertices: List):
        super().__init__(vertices)
        self.longer_length = max(edge.length for edge in self._edges)
        self.smaller_length = min(edge.length for edge in self._edges)
 
    def compute_area(self):
        area = self.longer_length * self.smaller_length 
        return area  

    def compute_perimeter(self):
        perimeter = 2*(self.smaller_length + self.longer_length)
        return perimeter



 

class Square(Rectangle):
    def __init__(self, vertices: List):
        super().__init__(vertices)

    def compute_area(self):
        area = self._edges[0].length ** 2
        return area
 
    def compute_perimeter(self):
        perimeter = 4 * self._edges[0].length
        return perimeter


class Triangle(Shape):
    def __init__(self, vertices: List):
        super().__init__(vertices)

    def set_vertices(self, new: List[Point]):
        
        if len(self._vertices) != 3:
            print("El triangulo solamente debe poseer 3 ángulos")
            
        else:
            super().set_vertices(new)
	
    def compute_area(self):
        a = self._edges[0].length
        b = self._edges[1].length
        c = self._edges[2].length
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

class Isosceles(Triangle):
    def __init__(self, vertices: List):
        super().__init__(vertices)



class Equilateral(Triangle):
    def __init__(self, vertices: List):
        super().__init__(vertices)

class Scalene(Triangle):
    def __init__(self, vertices: List):
        super().__init__(vertices)

class TriRectangle(Triangle):
    def __init__(self, vertices: List):
        super().__init__(vertices)


def main():
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)

    triangle = Triangle([p1, p2, p3])
    print("Area del triángulo:", triangle.compute_area())
    print("Perímetro del triángulo:", triangle.compute_perimeter())
    print("Ángulos internos del triángulo:", triangle.inner_angles)
    print("¿Es el triángulo regular?", triangle.get_is_regular())

    rectangle = Rectangle([p1, p2, p3, p4])
    print("\nÁrea del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())
    print("Ángulos internos del rectángulo:", rectangle.inner_angles)
    print("¿Es el rectángulo regular?", rectangle.get_is_regular())

    
if __name__ == "__main__":
    main()
