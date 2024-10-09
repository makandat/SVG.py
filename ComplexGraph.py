# ComplexGraph.py
from PyPackage import SVG

# 複素空間のグラフ
class ComplexGraph(SVG.SVG):
  VERSION = "1.0.0"

  # コンストラクタ
  def __init__(self, width:int, height:int, title="ComplexGraph", *, offset:tuple, scale:tuple):
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

  # パスを追加
  def draw_graph(self, data:list[complex], style:str="") -> None:
    pathdata = ["M "]
    for z in data:
      x, y = self.translate_complex(z, self.scale_x, self.scale_y, self.offset_x, self.offset_y)
      pathdata.append(f'{x},{y} ')
    if style == "":
      self.add_path(pathdata)
    else:
      self.add_path(pathdata, style)
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
  graph = ComplexGraph(800, 800, 'Test', offset=(400, 400), scale=(80, 80))
  print(graph.title)
  print(graph.width, graph.height)
  print(graph.offset_x, graph.offset_y)
  print(graph.scale_x, graph.scale_y)
  # 枠と座標軸を追加
  graph.add_frame()
  # データを追加
  graph.draw_graph([0+0j, 1+1j, 2+1.5j, 3+1.8j])
  # SVG を表示
  print(graph)
  # ファイル保存
  graph.save('./graph.svg')