from Color import RGB
from Pos import Pos
class SVG:
    encoding:str = 'Shift-JIS'
    unit:str = 'mm'
    draw_width = 1
    draw_color:RGB = RGB(255, 255, 255) # 'white'
    fill_color:RGB = RGB(255, 255, 255) # 'white'
    # canvas = [Pos(0, 0), Pos(100, 100)]
    # viewBox = [Pos(0, 0), Pos(100, 100)]
    def __init__(self, file_name):
        try:
            self.fp = open(file_name, mode='w')
        except FileNotFoundError: # 権限などのエラーは含まれない？
            print('ファイル', file_name, 'を開けませんでした。')
    def __del__(self):
        self.fp.close()

    def start(self, canvas=[Pos(0, 0), Pos(100, 100)], viewBox=[Pos(0, 0), Pos(100, 100)]):
        self.fp.write(f"<?xml version=\"{1.0}\" encoding=\"{self.encoding}\"?>\n")
        self.fp.write("<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n"
                      "  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n")
        self.fp.write(f"<svg version=\"1.1\" "
                      f"width=\"{canvas[1].x - canvas[0].x}{self.unit}\" "
                      f"height=\"{canvas[1].y - canvas[0].y}{self.unit}\" "
                      f"viewBox=\"{viewBox[0].x} {viewBox[0].y} {viewBox[1].x} {viewBox[1].y}\" "
                      f"preserveAspectRatio=\"xMidYMid\" "
                      f"fill-rule=\"evenodd\" "
                      f"xmlns=\"http://www.w3.org/2000/svg\" "
                      f"xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n")
    def finish(self):
        self.fp.write('</svg>\n')

    def set_unit(self, unit:str):
        if unit == 'mm' or unit == 'px':
            self.unit = unit
        else:
            raise ValueError('the unit unavailable!')
    def set_width(self, draw_width):
        self.draw_width = draw_width
    def set_fill_color(self, color:RGB):
        self.fill_color = color
    def set_draw_color(self, color:RGB):
        self.draw_color = color

    def line(self, left_top:Pos, right_bottom:Pos, color:RGB=draw_color, width=draw_width):
        self.fp.write(f"<line x1=\"{left_top.x}\" y1=\"{left_top.y}\" "
                      f"x2=\"{right_bottom.x}\" y2=\"{right_bottom.y}\" "
                      f"stroke=\"{color}\" stroke-width=\"{width}\" "
                      f"stroke-opacity=\"{1}\" stroke-linecap=\"{'round'}\" />\n")
    def rect():
        pass
    def circle():
        pass
    def text():
        pass
