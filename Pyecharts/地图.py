from pyecharts.charts import Map
from pyecharts.options import *

Map = Map()
data = [
    ('北京', 99),
    ('上海', 199),
    ('江西', 2),
    ('广东', 89),
    ('广西', 29)
]

Map.add('测试地图', data, 'china')

Map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 1, 'max': 9, 'label': '1-9', 'color': 'blue'},
            {'min': 10, 'max': 49, 'label': '10-49', 'color': 'orange'},
            {'min': 50, 'max': 999, 'label': '50-999', 'color': 'red'},
        ]
    )
)
Map.render('基础地图.html')
