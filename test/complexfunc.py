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