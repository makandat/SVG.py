# ComplexGraph.py
from PyPackage import SVG

# グラフ
class XYGraph(SVG.SVG):
  VERSION = "1.0.0"

  # コンストラクタ
  def __init__(self, width:int, height:int, title="XYGraph", *, offset:tuple, scale:tuple):
    super().__init__(width, height, title)
    self.__offset = offset
    self.__scale = scale
    return

  # 枠と座標軸を描画
  def add_frame(self):
    self.draw_frame()
    self.draw_hline(round(self.height / 2.0))
    self.draw_vline(round(self.width/ 2.0))
    return

  # 座標軸に文字列を追加
  #  texts は (x, y, text) のリスト
  def add_numvalue(self, texts:list[tuple]) -> None: 
    for p in texts:
      text = p[0]
      x = p[1]
      y = p[2]
      self.add_text(text, x, y)
    return

  # パスを追加 (折れ線グラフ)
  def draw_graph(self, data:list[tuple], style:str="") -> None:
    pathdata = ["M "]
    for t in data:
      x, y = self.translate_xy(t[0], t[1], self.scale_x, self.scale_y, self.offset_x, self.offset_y)
      pathdata.append(f'{x},{y} ')
    if style == "":
      self.add_path(pathdata)
    else:
      self.add_path(pathdata, style)
    return

  # 矩形を追加 (棒グラフ)
  def draw_bars(self, data:list[tuple], width:int, style:str="") -> None:
    for t in data:
      x, y = self.translate_xy(t[0], t[1], self.scale_x, self.scale_y, self.offset_x, self.offset_y)
      if y > 400:
        self.add_shape('rect', {"x":x, "y":self.offset_y, "width":width, "height":y-self.offset_y}, style)
      else:
        self.add_shape('rect', {"x":x, "y":y, "width":width, "height":self.offset_y-y}, style)
    return

  # 円を追加 (散布図)
  def draw_scatters(self, data:list[tuple], r:int, style:str="") -> None:
    for t in data:
      x, y = self.translate_xy(t[0], t[1], self.scale_x, self.scale_y, self.offset_x, self.offset_y)
      self.add_shape('circle', f'cx="{x}" cy="{y}" r="{r}"', style)
    return

  # X 軸方向のオフセット
  @property
  def offset_x(self):
    return float(self.__offset[0])

  # Y 軸方向のオフセット
  @property
  def offset_y(self):
    return float(self.__offset[1])

  # X 軸方向の倍率
  @property
  def scale_x(self):
    return float(self.__scale[0])

  # Y 軸方向の倍率
  @property
  def scale_y(self):
    return float(self.__scale[1])


# Test
if __name__ == '__main__':
  graph = XYGraph(800, 800, 'Test', offset=(400, 400), scale=(80, 80))
  print(graph.title)
  print(graph.width, graph.height)
  print(graph.offset_x, graph.offset_y)
  print(graph.scale_x, graph.scale_y)
  # 枠と座標軸を追加
  graph.add_frame()
  # データを追加
  graph.draw_graph([(0,0), (1,0.5), (2,-0.5), (3,0), (4,1)],XYGraph.shape_style("#c04040", 3, "transparent"))
  # SVG を表示
  print(graph)
  # ファイル保存
  graph.save('./graph.svg')