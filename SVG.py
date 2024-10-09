# SVG.py
#   https://triple-underscore.github.io/SVG11/index.html
import os, math
from typing import Union

# SVG クラス
class SVG:
  VERSION = "2.2.0"

  # コンストラクタ
  #   width: 描画領域の幅 (ドット数)
  #   height: 描画領域の高さ (ドット数)
  #   title: SVG のタイトル。 "" の場合は使用されない。
  def __init__(self, width:int, height:int, title=""):
    self.__width = width # 描画領域の幅
    self.__height = height # 描画領域の高さ
    self.__title = title  # 図形のタイトル
    self.__shapes = []  # 図形のコレクション
    self.__group = []   # グループ要素のコレクション
    return

  # 現在はグループ内か？
  def _is_group(self):
    return len(self.__group) > 0

  # data がリストまたはタプルなら要素を連結する。
  def _tos(self, data:Union[list, tuple, dict, str]):
    if type(data) is str:
      return data
    if type(data) is dict:
      sdata = ""
      for key, val in data.items():
        if not (type(val) is str and val.startswith('"')):
          val = f'"{val}"'
        sdata += f'{key}={val} '
      sdata = sdata.rstrip()
    else:
      sdata = " ".join(data)
    return sdata

  # 図形を追加
  #   name: 図形の名前 ('line', 'rect', 'circle', 'ellipse', 'polygon', 'polyline')
  #   data: 図形の属性・データ (x, y, width, height など)
  #   style: style="..." の ... 部分。
  def add_shape(self, name:str, data:Union[list, tuple, dict, str]="", style:str="stroke:gray;stroke-width:1;fill:transparent;") -> None:
    sdata = self._tos(data)
    if name == "polygon" or name == "polyline":
      sdata = f'points="{sdata}"'
    if self._is_group():
      self.__group.append(f'<{name} {sdata} />')
    else:
      self.__shapes.append(f'<{name} {sdata} style="{style}" />')
    return

  # パスを追加
  def add_path(self, data:Union[list, tuple, str]="", style:str="stroke:gray;stroke-width:1;fill:transparent;") -> None:
    sdata = self._tos(data)
    if self._is_group():
      self.__group.append(f'<path d="{sdata}" style="{style}" />')
    else:
      self.__shapes.append(f'<path d="{sdata}" style="{style}" />')
    return

  # 文字列を追加
  #   text: 文字列
  #   x: 表示位置の X 座標
  #   y: 表示位置の Y 座標
  #   style: スタイル
  def add_text(self, text:str, x:int, y:int, style="font-size:1.5;stroke:gray;fill:gray;") -> None:
    if self._is_group():
      self.__group.append(f'<text x="{x}" y="{y}" style="{style}"></text>')
    else:
      self.__shapes.append(f'<text x="{x}" y="{y}" style="{style}">{text}</text>')
    return

  # グループを追加 (新しいグループを開始)
  #   style: スタイル
  def add_group(self, style:str) -> None:
    self.__group.clear()
    self.__group.append(f'<g style="{style}">')
    return 

  # グループを終了
  def close_group(self) -> None:
    # self.__group の内容を self.__shapes へコピー
    self.__shapes += self.__group
    self.__shapes.append("</g>")
    self.__group.clear()
    return

  # 文字列表現
  #   str(obj) が返す文字列
  def __str__(self) -> str:
    svg = f'<svg width="{self.width}" height="{self.height}" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'
    if self.title != "":
      svg += f'<title>{self.title}</title>\n'
    svg += "\n".join(self.__shapes)
    svg += "\n</svg>\n"
    return svg

  # 座標変換 (XY座標を SVG 座標に変換する)
  #  x, y: 点の座標
  #  scale_x: 横軸方向の倍率
  #  scale_y: 縦軸方向の倍率
  #  offset_x: 横軸方向のオフセット
  #  offset_y: 縦軸方向のオフセット
  #  戻り値: 変換後の点の座標 (整数)
  def translate_xy(self, x:float, y:float, scale_x:float=1.0, scale_y:float=1.0, offset_x:float=0.0, offset_y:float=0.0) -> tuple[int, int]:
    new_x = round(x * scale_x + offset_x)
    new_y = self.height - round(y * scale_y + offset_y)
    return (new_x, new_y)

  # 座標変換 (複素数を SVG 座標に変換する)
  #  z: 複素数
  #  scale_x: 横軸方向の倍率
  #  scale_y: 縦軸方向の倍率
  #  戻り値: 変換後の点の座標 (整数)
  def translate_complex(self, z:complex, scale_x:float=1.0, scale_y:float=1.0, offset_x=0.0, offset_y=0.0) -> tuple[int, int]:
    x = z.real
    y = z.imag
    return self.translate_xy(x, y, scale_x, scale_y, offset_x, offset_y)

  # 座標変換 (極座標を SVG 座標に変換する)
  #  r: 原点からの距離
  #  arg: 偏角 (radian)
  #  scale_x: 横軸方向の倍率
  #  scale_y: 縦軸方向の倍率
  #  degree: arg の単位を度とみなす。
  #  戻り値: 変換後の点の座標 (整数)
  def translate_polar(self, r:float, arg:float, scale_x:float=1.0, scale_y:float=1.0, offset_x=0.0, offset_y=0.0, degree=False) -> tuple[int, int]:
    if degree:
      arg = math.pi * arg / 180.0
    x = r * math.cos(arg)
    y = r * math.sin(arg)
    return self.translate_xy(x, y, scale_x, scale_y, offset_x, offset_y)

  # 図形のスタイル生成
  #   color: 境界線の色
  #   line_width: 線の幅
  #   bgcolor: 背景色
  #   opacity: 背景の透過率
  @staticmethod
  def shape_style(color="black", line_width=2, bgcolor="transparent", opacity=1) -> str:
    style = f'stroke:{color};stroke-width:{line_width};fill:{bgcolor};fill-opacity:{opacity};'
    return style

  # Transform 属性文字列を得る。
  #   rotate: 回転角
  #   moveto: 移動先の座標
  #   scale: 倍率
  @staticmethod
  def transform(rotate=None, moveto=None, scale=None) -> str:
    tr = ''
    if rotate != None:
      tr += f'rotate({rotate}) '
    if moveto != None:
      tr += f'translate({moveto[0]} {moveto[1]}) '
    if scale != None:
      tr += f'scale({scale[0]} {scale[1]})'
    return tr

  # ファイル保存
  #   path: 保存先のファイル名（フルパス）
  def save(self, path:str) -> None:
    with open(path, "wt", encoding="utf-8") as f:
      s = f'<?xml version="1.0"?>\n{self}'
      f.write(s)
    return

  # 内容をクリア
  def clear(self) -> None:
    self.__shapes.clear()
    self.__group.clear()
    return

  # 描画領域に枠を表示
  def draw_frame(self, color="gray", line_width=1) -> None:
    self.add_shape('rect', ['x="0"', 'y="0"', f'width="{self.width-1}"', f'height="{self.height-1}"'], f"stroke:{color};stroke-width:{line_width};fill:transparent;")
    return

  # 描画領域両端を結ぶ垂直直線を表示 (座標軸などで利用)
  def draw_vline(self, x:int, / , style="stroke:gainsboro;stroke-width:1") -> None:
    data = f'x1="{x}" y1="{0}" x2="{x}" y2="{self.height}"'
    self.add_shape('line', data, style)
    return

  # 描画領域両端を結ぶ水平直線を表示 (座標軸などで利用)
  def draw_hline(self, y:int, / , style="stroke:gainsboro;stroke-width:1") -> None:
    data = f'x1="0" y1="{y}" x2="{self.width}" y2="{y}"'
    self.add_shape('line', data, style)
    return

  # 描画領域の幅
  @property
  def width(self) -> int:
    return self.__width

  # 描画領域の高さ
  @property
  def height(self) -> int:
    return self.__height

  # SVG のタイトル
  @property
  def title(self) -> int:
    return self.__title
  @title.setter
  def title(self, value) -> None:
    self.__title = value
    return




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
