from SVG import SVG
from Color import RGB
from Pos import Pos

file_name = 'test.svg'

svg = SVG(file_name)
svg.set_unit('px') # startより先にしなければならない…
svg.start(canvas=[Pos(0, 0), Pos(1920, 1080)], viewBox=[Pos(0, 0), Pos(1920, 1080)])
svg.line(Pos(10.0, 0), Pos(50, 50), RGB(100, 100, 255), 3)
svg.line(Pos(30.5, 20.0025), Pos(10, 80), RGB(255, 0, 100), 8)
svg.line(Pos(30, 0), Pos(30, 80), RGB(10, 6, 255), 1)
svg.finish()
