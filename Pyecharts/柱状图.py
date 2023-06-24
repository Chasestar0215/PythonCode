from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(['中国', '美国', '日本'])
bar1.add_yaxis('GDP', [30, 35, 25], label_opts=LabelOpts(position='right'))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['中国', '美国', '日本'])
bar2.add_yaxis('GDP', [35, 39, 29], label_opts=LabelOpts(position='right'))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(['中国', '美国', '日本'])
bar3.add_yaxis('GDP', [37, 42, 31], label_opts=LabelOpts(position='right'))
bar3.reversal_axis()

timeline = Timeline({'theme': ThemeType.LIGHT})

timeline.add(bar1, '2020')
timeline.add(bar2, '2021')
timeline.add(bar3, '2022')

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render('基础时间线柱状图.html')
