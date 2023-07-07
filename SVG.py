from .Color import RGB
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

    def start(self, viewBox_min_x=0, viewBox_min_y=0, viewBox_width=600, viewBox_height=400, width=600, height=400):
        self.fp.write(f"<?xml version=\"{1.0}\" encoding=\"{self.encoding}\"?>\n")
        self.fp.write("<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n"
                      "  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n")
        self.fp.write(f"<svg version=\"1.1\" "
                      f"width=\"{width}{self.unit}\" "
                      f"height=\"{height}{self.unit}\" "
                      f"viewBox=\"{viewBox_min_x} {viewBox_min_y} {viewBox_width} {viewBox_height}\" "
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

    def line(self, x1:float, y1:float, x2:float, y2:float, color:RGB=draw_color, width=draw_width):
        self.fp.write(f"<line x1=\"{x1}\" y1=\"{y1}\" "
                      f"x2=\"{x2}\" y2=\"{y2}\" "
                      f"stroke=\"{color}\" stroke-width=\"{width}\" "
                      f"stroke-opacity=\"{1}\" stroke-linecap=\"{'round'}\" />\n")
    def rect(self, x:float=0, y:float=0, fill_color=fill_color, width='auto', height='auto'):
        self.fp.write(f"<rect x=\"{x}\" y=\"{y}\" "
                      f"width=\"{width}\" height=\"{height}\" "
                      f"fill=\"{fill_color}\" />\n")
    def circle():
        pass
    def text():
        pass
