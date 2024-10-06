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
