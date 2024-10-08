# SVG.py graph_server
from aiohttp import web
import math, enum
import XYGraph

HTML = '''<!DOCTYPE html>
 <html>
  <head>
    <meta charset="utf-8" />
    <title>SVG.py graph</title>
    <style>
     h1 {
       text-align:center;
       padding:15px;
       color:orangered;
     }
     #canvas {
       width:1000px;
       height:600px;
       margi-top:50px;
       margin-bottom:40px;
       margin-left:auto;
       margin-right:auto;
     }
     a:link, a:visited {
       color:red;
       text-decoration:none;
     }
     input[type="text"], select {
       border-radius:6px;
       height:30px;
       font-size:12pt;
     }
     #button1 {
       width:100px;
       height:36px;
       border:solid 2px dimgray;
       border-radius:6px;
       background-color:azure;
     }
     #info {
       padding:10px;
       text-align:center;
       color:blue;
       font-size:12pt;
     }
    </style>
    <script>
      function clear() {
         location = "/"
      }
    </script>
  </head>

  <body style="margin-left:10%;margin-right:10%;">
   <h1>graph_server.py</h1>
   <p><a href="https://triple-underscore.github.io/SVG11/index.html#minitoc" target="_blank">SVG 1.1 Specification</a>
    / <a href="https://docs.aiohttp.org/en/stable/index.html" target="_blank">aiohttp Document</a>
    / <a href="https://developer.mozilla.org/ja/docs/Web/SVG" target="_blank">MDN SVG</a>
    / <a href="/">Reset</a>
    </p>
   <form style="margin-top:50px;" method="POST" action="/draw">
    <div style="margin-bottom:10px;"><label>グラフ種別
     <select name="func" id="func" style="width:160px;">
      <option value="0"></option>
      <option value="1">(1) 折れ線グラフ</option>
      <option value="2">(2) 棒グラフ</option>
      <option value="3">(3) 散布図</option>
     </select>
    </label></div>
    <div style="margin-top:10px;">
     <button id="button1" type="submit">描画する</button>
    </div>
   </div>
   <p id="info">グラフ種別 {{number}}</p>
   <div id="canvas">{{svg}}</div>
   <p>&nbsp</p>
   <p>&nbsp</p>
  </body>
 </html>
'''

# 描画領域のサイズ
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800


# draw リクエストハンドラ
async def draw(request):
  # リクエストパラメータを得る。
  params = await request.post()
  number = int(params["func"])
  # XYGraph オブジェクトを得る。
  xyg = XYGraph.XYGraph(CANVAS_WIDTH, CANVAS_HEIGHT, offset=(400, 400), scale=(40, 40))
  # 枠とラベルを描画
  xyg.add_frame()
  xyg.add_numvalue([("-10",0,390), ("0",400,390), ("+10",760,390), ("+10",400,15), ("-10", 400, 785)])
  # グラフを描く
  match number:
    case 1: # XYGraph 折れ線グラフ
      xyg.title="XYGraph 折れ線グラフ"
      data = [(-5, 2), (-3, 5), (0, 0), (2, -1), (4, 7), (5, 6)]
      xyg.draw_graph(data, "stroke:blue;stroke-width:3;fill:transparent;")
    case 2: # XYGraph 棒グラフ
      xyg.title="XYGraph 棒グラフ"
      data = []
      for i in range(-10, 10):
        data.append((i, i * 0.5))
      xyg.draw_bars(data, 16, "stroke:blue;stroke-width:2;fill:azure;")
    case 3: # XYGraph 散布図
      xyg.title="XYGraph 散布図"
      data = [(0, 1), (1, 0), (-1, 0), (-1, -1), (2, 1), (-3, -2.5)]
      xyg.draw_scatters(data, 5, "stroke:blue;stroke-width:2;fill:teal;")
    case _:
      pass
  # graph を文字列化
  svg = str(xyg)
  print(svg)
  html = HTML.replace("{{svg}}", svg).replace("{{number}}", params["func"])
  return web.Response(content_type="text/html", body=html)



# / (index) リクエストハンドラ
async def index(request):
  html = HTML.replace("{{svg}}", "").replace("{{number}}", "--")
  return web.Response(body=html, content_type="text/html")



# Application オブジェクトを作成する。
app = web.Application()
# ルート (routes) に (パス, ハンドラ) を追加する。
app.add_routes([web.get('/', index), web.post('/draw', draw)])
 
# スタート port=8085
if __name__ == '__main__':
  print('aiohttp Web server starting .. http://localhost:8085/')
  web.run_app(app, port=8085)
