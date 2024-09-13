from graphics import Window, Point, Line

def main():
    
    window = Window(800, 600)
    l = Line(Point(50,50), Point(400, 400))
    window.draw_line(l, "black")
    window.wait_for_close()
    


main()