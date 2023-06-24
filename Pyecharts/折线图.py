from pyecharts.charts import Line
from pyecharts.options import *

line = Line()
line.add_xaxis(['China', 'USA', 'Japan'])
line.add_yaxis('GDP', [20, 30, 10])

# 设置全局配置项set_global_opts
line.set_global_opts(
    title_opts=TitleOpts(title='GDP展示', pos_left='center', pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render('基础折线图.html')
