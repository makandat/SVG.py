# SVG.py

## Overview

SVG.py is a module for generating SVG, and can be used to generate SVG in Python. 

Therefore, graphs and other shapes that are difficult to create by hand can be created by script.

However, not all SVG functions are supported. Also, knowledge of SVG is required for programming.

When using the SVG class, import SVG is required.

## SVG class

### Constructor

**svg.SVG(width:int, height:int, title="")**

*    **width:int** Pixels of the SVG's width
*    **height:int** Pixels of the SVG's height
*    **title:str** Title of the SVG


## Properties
* **width:int** Pixels of the SVG's width (Read Only)
* **width:int** Pixels of the SVG's height (Read Only)
* **title:str** Title of the SVG (Read/Write)


## Instance methods
**svg.add_shape(name:str, data:Union[list, tuple, dict, str]="", style:str="stroke:gray;stroke-width:1;fill:transparent;") -> None**

Add a shape to the SVG.

*   **name**<br>
    Type of shape ('line', 'rect', 'circle', 'ellipse', 'polyline', 'polygon')
*   **data**<br>
    Attributes of the shape. The type must be list, dict or str.
    (ex1) 'x="0" y="0" width="120" height="50"'<br>
    (ex2) ['x="0"', 'y="0"', 'width="120"', 'height="50"']<br>
    (ex3) {"x":0, "y":0, "width":120, "height":50}<br>

*   **style**<br>
    Style of the shape.<br>
    (ex) "stroke:black;stroke-width:2;fill:lightyellow;fill-opacity:40%;"

**svg.add_path(data:Union[list, tuple, str]="", style:str="stroke:gray;stroke-width:1;fill:transparent;") -> None**

Add a Path to the SVG.

*   **data**<br>
    List of the commands and the points (list, tutple or str)<br>
    (ex1) ["M", "40,5", "45,18", "H 5", "19,3", "Z"]<br>
    (ex2) "M 40,5 45,18 50,18 19,3 Z"
*   **style**<br>
    Style of the shape. (ex) "stroke:gray;stroke-width:1;fill:transparent;"

**svg.add_text(text:str, x:int, y:int, style="font-size:1.5;stroke:gray;fill:gray;") -> None**

Add the string to the SVG.

*   **text:str**<br>
    Text to display.
*   **x:int**<br>
    X coordinate to display.
*   **y:int**<br>
    Y coordinate to display.
*   **style**<br>
    Style of the string. (ex) "font-size:1.5;stroke:gray;fill:gray;"

**svg.add_group(style:str) -> None**

Add the group to the SVG. To close the group, use close_group() method.

*   **style:str**
    Style to apply the group.

**svg.close_group()**

Close the group.

**str(svg)**

String expression of the SVG.

**svg.translate_xy(x:float, y:float, scale_x:float=1.0, scale_y:float=1.0, offset_x:float=0.0, offset_y:float=0.0) -> tuple[int, int]**

The point (x, y) of the XY coodinate convert to the SVG's coordinate.

*   **x:float**<br>
    X value of the point.
*   **y:float**<br>
    Y value of the point.
*   **scale_x:float**<br>
    X-axis magnification
*   **scale_y:float**<br>
    Y-axis magnification
*   **offset_x:float**<br>
    X-axis offset
*   **offset_y:float**<br>
    Y-axis offset

(ex) The point (0, 0) is at the center of a 1000x1000 drawing area, when the logical drawing area is 50x50.
```
svg.translate_xy(0, 0, 10.0, 10.0, 500, 500)
```

**svg.translate_complex(z:complex, scale_x:float=1.0, scale_y:float=1.0, offset_x=0.0, offset_y=0.0) -> tuple[int, int]**

Transform a complex space point (a complex number) into the SVG coordinate system.

*   **z:complex**<br>
    Complex number to convert.
*   **scale_x:float**<br>
    X-axis magnification
*   **scale_y:float**<br>
    Y-axis magnification
*   **offset_x:float**<br>
    X-axis offset
*   **offset_y:float**<br>
    Y-axis offset

(ex) The point (0+0i) is the center of a 1000x1000 drawing area, but the logical drawing area is 50x50.
```
svg.translate_complex(complex(0, 0), 10.0, 10.0, 500, 500)
```

**svg.translate_polar(r:float, arg:float, scale_x:float=1.0, scale_y:float=1.0, offset_x=0.0, offset_y=0.0, degree=False) -> tuple[int, int]**

Transforms the polar point (r, arg) into the SVG coordinate system.

*   **r:float**<br>
    Distance from the origin of the point to be transformed
*   **arg:float**<br>
    Argument of the point to be transformed
*   **scale_x:float**<br>
    X-axis magnification
*   **scale_y:float**
    Y-axis magnification
*   **offset_x:float**
    X-axis offset
*   **offset_y:float**
    Y-axis offset

(ex) The point (0,0) is at the center of a 1000x1000 drawing area, but the logical drawing area is 50x50.<br>
```
svg.translate_porlar(0, 0, 10.0, 10.0, 500, 500)
```

**svg.save(path:str) -> None**

Saves the SVG to a file with the path.

**svg.clear() -> None**

Clears the contents of the current SVG object.

**svg.draw_frame(color:str="gray", line_width:int=1) -> None**

Draws a frame on the current drawing area.

*   **color:str**<br>
    Border color
*   **line_width:int**<br>
    Border width

**svg.draw_vline(x:int, / , style="stroke:gainsboro;stroke-width:1") -> None**

Draws vertical lines for the axes on the current drawing area.

*   **x:int**<br>
    The x-coordinate of the vertical line
*   **style:str**<br>
    Style of the line.

**svg.draw_hline(y:int, / , style="stroke:gainsboro;stroke-width:1") -> None**

Draws horizontal axes lines on the current drawing area.

*   **y:int**<br>
    Y coordinate of the horizontal line
*   **style:str**<br>
    Style of the line.

## Static methods

**SVG.shape_style(color="black", line_width=2, bgcolor="transparent", opacity=1) -> str**

Constructs a style string to be used, for example, for the style parameter of the add_shape() method.

*   **color:str**<br>
    Border color
*   **line_width:int**<br>
    Border width
*   **bgcolor:str**<br>
    Background color
*   **opcity:float**<br>
    Background Transparency

**SVG.transform(rotate=None, moveto=None, scale=None) -> str**

Configure the transform attribute.

*   **rotate:float**<br>
    Rotation angle (degrees)
*   **moveto:tuple[int, int]**<br>
    Move the starting point.
*   **scale:float**<br>
    magnification

## Samples

### Draw various shapes
```
# テスト
if __name__ == "__main__":
  # v2.0
  #  初期化
  svgobj = SVG(320, 240, "Test")
  # 直線
  svgobj.add_shape('line', 'x1="10" y1="110" x2="200" y2="150"', SVG.shape_style(color="orange", line_width=5))
  # 矩形
  svgobj.add_shape('rect', 'x="5" y="5" width="80" height="50"', SVG.shape_style(color="black", line_width=2, bgcolor="lightblue"))
  # 文字列
  svgobj.add_text('ABCD098', x=10, y=80)
  # グループ開始
  svgobj.add_group(SVG.shape_style('red', 2, 'pink', 0.5))
  # 円
  svgobj.add_shape('circle', {"cx":280, "cy":200, "r":25})
  # 円
  svgobj.add_shape('circle', {"cx":240, "cy":200, "r":25})
  # 楕円
  svgobj.add_shape('ellipse', ('cx="180"', 'cy="200"', 'rx="40"', 'ry="25"'))
  # グループ終了
  svgobj.close_group()
  # 多角形
  svgobj.add_shape('polygon', ["150,30", "230,30", "200,80", "120,80"])
  # 折れ線
  svgobj.add_shape('polyline', "10,230 70,180 50,150 110,210", SVG.shape_style("deeppink", 4))
  # パス
  svgobj.add_path('M 10,95 80,30 100,50 120,150 180,50', SVG.shape_style("red", 3))
  # 傾いた矩形 (transform)
  tr = SVG.transform(rotate=-30, moveto=(10, 10), scale=(2, 1))
  svgobj.add_shape('rect', ('x="50"', 'y="190"', 'width="100"', 'height="50"', f'transform="{tr}"'), SVG.shape_style("black", 2, "silver"))
  # 結果を表示
  print(svgobj, "\n")
  # ファイル保存
  svgobj.save("./HTML/test.svg")
  # XY 座標変換メソッドの動作確認
  print("translate_xy")
  print(svgobj.translate_xy(0, 0, 10.0, 8.0, 160.0, 120))
  print(svgobj.translate_xy(1, 0, 10.0, 8.0, 160.0, 120))
  print(svgobj.translate_xy(0, 1, 10.0, 8.0, 160.0, 120))
  print(svgobj.translate_xy(1, 1, 10.0, 8.0, 160.0, 120))
  # 複素空間 座標変換メソッドの動作確認
  print("translate_complex")
  print(svgobj.translate_complex(complex(0, 0), 10.0, 8.0, 160.0, 120))
  print(svgobj.translate_complex(complex(1, 0), 10.0, 8.0, 160.0, 120))
  print(svgobj.translate_complex(1j, 10.0, 8.0, 160.0, 120))
  print(svgobj.translate_complex(1+1j, 10.0, 8.0, 160.0, 120))
  # 極座標変換メソッドの動作確認
  print("translate_polar")
  print(svgobj.translate_polar(0, 0, 10.0, 8.0, 160.0, 120))
  print(svgobj.translate_polar(1, 0, 10.0, 8.0, 160.0, 120))
  print(svgobj.translate_polar(1, 90.0, 10.0, 8.0, 160.0, 120, True))
  print(svgobj.translate_polar(1.414, 45, 10.0, 8.0, 160.0, 120, True))
```

### Graph
```
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
```

## Graph of complex space

```
# 複素空間
import os, cmath
import SVG

# 複素数関数を描画
def complexfunc(p1:complex, p2:complex) -> None:
  z = p1
  data = "M "
  while z.real < p2.real:
    w = cmath.exp(z * 0.05)
    x, y = svg.translate_complex(w, 4, 3, 400, 300)
    data += f'{x},{y} '
    z = z + (0.1+0.1j)
  return data

# 初期化
svg = SVG.SVG(800, 600, "Complex")
# 枠を描画
svg.draw_frame()
# 座標軸を描画
svg.draw_hline(300)
svg.draw_vline(400)
# 座標軸に値を表示
svg.add_text('100.0j', 400, 15)
svg.add_text('-100.0j', 400, 590)
svg.add_text('-100.0', 0, 290)
svg.add_text('100.0', 740, 290)
# 元の直線
svg.add_shape("line", {"x1":0, "y1":599, "x2":799, "y2":0}, "stroke:black;stroke-width:3")
# 変換後の曲線
path = complexfunc(complex(-100.0, -75.0), complex(100.0, 75.0))
svg.add_path(path, "stroke:royalblue;stroke-width:3;fill:transparent;")
# SVG を表示する。
print(svg)
# ファイル保存
svg.save("complexfunc.svg")
```

### Graph of poler coordinate system
```
# 極座標のグラフ
import SVG, math, os

# 極座標でグラフを描画する。
def polarfunc(svg):
  a = 0.0
  data = "M "
  while a <= 2.0 * math.pi:
    x, y = svg.translate_polar(200.0, a, 1.0, 1.0, 400, 400)
    data += f"{x},{y} "
    a += 0.1
  return data + " Z"

# 初期化
svg = SVG.SVG(800, 800, "Polar")
# 枠を描画
svg.draw_frame()
# 座標軸を描画
svg.draw_hline(400)
svg.draw_vline(400)
# 座標軸に値を表示
svg.add_text('100.0', 400, 15)
svg.add_text('-100.0', 400, 780)
svg.add_text('-100.0', 0, 400)
svg.add_text('100.0', 740, 400)
# グラフを描画
data = polarfunc(svg)
data = polarfunc(svg)
svg.add_path(data, "stroke:black;stroke-width:2;fill:lightcyan;fill-opacity:30%;")
# SVG を表示する。
print(svg)
# ファイル保存
svg.save("polarfunc.svg")
```
.<br>
.<br>
.<br>

