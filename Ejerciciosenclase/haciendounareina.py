import graphics

if __name__ == '__main__':
    win = graphics.GraphWin("Reina", 100, 100)
    pol = graphics.Polygon(graphics.Point(10, 30), graphics.Point(30, 70),
                           graphics.Point(30, 80), graphics.Point(20, 90),
                           graphics.Point(70, 90), graphics.Point(80, 90),
                           graphics.Point(70, 80), graphics.Point(70, 70),
                           graphics.Point(90, 30), graphics.Point(60, 50),
                           graphics.Point(50, 10), graphics.Point(40, 50))
    pol.setFill("black")
    pol.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done
