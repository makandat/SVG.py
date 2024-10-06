# 関数のグラフ
import SVG, os, math

def radian(degree:float) -> float:
  return degree / 180.0 * math.pi

svg = SVG.SVG(1000, 500, 'Graph')
svg.draw_frame()
svg.draw_vline(500)
svg.draw_hline(250)
svg.add_text('-360', x=0, y=245) 
svg.add_text('360', x=960, y=245) 
svg.add_text('1', x=500, y=15) 
svg.add_text('-1', x=500, y=495) 
scale_x = 500.0 / 360.0
scale_y = 250.0
offset_x = 500.0
offset_y = 250.0
x = -360.0
data = "M "
while x <= 360.0:
  y = math.cos(radian(x))
  x1, y1 = svg.translate_xy(x, y, scale_x, scale_y, offset_x, offset_y)
  data += f' {x1},{y1}'
  x += 1.0
svg.add_path(data, style="stroke:black;stroke-width:2;fill:transparent;")
svg.save("./xyfunc.svg")
print(svg)