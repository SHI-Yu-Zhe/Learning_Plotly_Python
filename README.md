# Learning Plotly Python

## 简介

Plotly Python 是一个构建在plotly.js上的开源库，cufflinks是一个plotly的包装容器，而plotly正是构建在世界公认最好的可视化核——d3.js上的。这几个库的堆叠顺序是——cufflinks->plotly python->plotly.js->d3.js。相比于构建于javascript上的d3.js，构建于python上的plotly有着更明显的优势——兼具了python的良好编程效率和d3的图形化能力。之前通过对d3.js的学习，我们已经掌握了数据可视化的基础逻辑和一些基本元素的实现方法，这有助于我们学习plotly。

## 安装

在终端输入一下命令安装plotly和cufflinks这两个包：

```
sudo pip install plotly cufflinks
```

### 使用在线库

这需要创建账号密码。对于使用Jupyter Notebook的开发者来说是比较方便的。

```python
plotly.tools.set_credentials_file(username='YourUsernameHere', api_key='YourAPIkeyHere')
```

### 使用离线库

我的学习环境是Ubuntu的PyCharm，因此我使用的是离线库。离线库通过此方式调用plot。

```python
plotly.offline.plot()
```

## 配置本地开发环境

由于plotly是基于python2的库，而默认下PyCharm解释器是python3，需要通过额外配置修改，否则编译器会报错。

![1565660798550](/home/shi/.config/Typora/typora-user-images/1565660798550.png)

如图，我们应该在选择文件路径时就将默认的虚拟环境改成python2.7，这样能使系统自动复制python2.7到实验文件夹中，这样随后python运行生成的HTML文件也会出现在同一路径下。

若一开始没有修改虚拟环境，只能点击File->Settings->选定需要修改python版本的项目->Project Interpreter->选择Python 2.7。可以看到，这里面就含有plotly包。点击Apply，返回编程界面，发现不再报错。

![1565657355776](/home/shi/.config/Typora/typora-user-images/1565657355776.png)

下面用这段代码测试安装成功与否，并考察版本。

```python
import plotly as pl
print(pl.__version__)
```

![1565657717497](/home/shi/.config/Typora/typora-user-images/1565657717497.png)

## 第一个简单图

制作一个最简单的折线图。

```python
import plotly as pl
from plotly.graph_objs import Scatter,Layout
# import required modules and packages from plotly
pl.offline.plot({ # use offline call
    "data":[Scatter(x=[1,2,3,4],y=[4,3,2,1])],
    # attribute data is a scatter set
    "layout":Layout(title="a simple line chart")
    # attribute layout is a title
})# make an object with attributes as parameter
```

![1565658019435](/home/shi/.config/Typora/typora-user-images/1565658019435.png)

分析这段代码。第一行我们引进了plotly包，而第二行我们从plotly下的`graph_objts`模块下引进了`Scatter() `和` Layout()`这两个方法。显然地，`Scatter()`作用是将数据坐标以散点形式打印在二维坐标系中，其参数为一个拥有两个存储着横纵坐标值数组的二维数组，对应下标组成散点。`Layout()`作用是在图像上打印文本，这里参数中title规定了文本打印的位置，而对其赋值的字符串规定了文本内容。

观察URL栏不难得知，程序运行时启动默认浏览器，通过本地文件传输协议(file://)访问了一个名为`temp-plot.html`的HTML文件，而这个文件显然是程序执行过程中由plotly中的某些方法自动生成的，它的路径也是默认的，并不是.py文件存储的路径，这种问题正是由于一开始没有将项目解释器设置为python2.7，导致随后修改时仅仅添加了引用路径，并没有将python2.7复制到当前文件夹。

值得注意的是，`temp-plot.html`文件大小为3,245,365 bytes，也就是3.2MB。这也说明实际使用中，并不必要引入完整`plotly`包，只需根据需要引入相应模块即可。

进一步观察，我们发现可以通过对图象的拖拽截取一部分，例如：

![1565659223856](/home/shi/.config/Typora/typora-user-images/1565659223856.png)

这样的特性极大方便了数据研究者对复杂图象细微处的探究。而双击页面就会使图象恢复原样。通过这个测试，我们发现plotly可能拥有非常人性化的交互设计。

## 绘图基础

### 使用渲染框架绘图

与上一个例子不同，渲染框架首先调用图像对象的`Figure()`方法，通过自定义参数设置图像属性，再调用图像对象的`show()`方法将其打印。与之前的`plot()`方法不同，这种方法的操作对象是图像而不是图象。图象是确定的坐标与数据，而图像是一张印好了坐标轴与数据的图片。值得注意的是，`data`赋值永远是数组，不论它的维度是多少。

```python
import plotly.graph_objects as go
fig = go.Figure(
    data = [go.Bar(y=[2,5,3,1,7,3])],
    layout_title_text = "show figure"
)
fig.show()

```

![1565662337606](/home/shi/.config/Typora/typora-user-images/1565662337606.png)

与`plot()`方法不同，`Figure()`传入的参数是若干数组类型变量，而`plot()`传入的参数是一个对象类型变量，其余则大同小异，对象的属性对应着这些参数变量。最后一行代码中，`show()`方法可以被省略，可以直接通过fig 让其显示其自身。

### 设置默认渲染器

在终端控制台中输入以下命令查看渲染器：

```python
import plotly.io as pio
pio.renderers
```

![1565663356816](/home/shi/.config/Typora/typora-user-images/1565663356816.png)

下面尝试更改默认渲染器为svg,由前两行代码实现。

```python
import plotly.io as pio
pio.renderers.default = "browser"
import plotly.graph_objects as go
fig = go.Figure(
    data = [go.Bar(y=[2,5,3,1,7,3])],
    layout_title_text = "show figure"
)
fig.show(renderer="svg")

```

![1565665528610](/home/shi/.config/Typora/typora-user-images/1565665528610.png "如图，svg元素已经生成")

类似地，我们可以更改默认渲染器为pdf,json,png以及notebook,notebook_collected,colab,kaggle和azure等。

### 构造图像字典

下面完全使用字典嵌套来实现一个柱状图，这与之前例子中使用图像对象初始化方式完全不同。

```python
import plotly.io as pio

fig = {
    "data":[{
        # nested dictionary
        "type":"bar",
        "x":[2011,2012,2013,2014],
        "y":[32,54,21,42]
    }],
    "layout":{"title":{"text":"bar chart"}}
}

pio.show(fig)

```

![1565668192272](/home/shi/.config/Typora/typora-user-images/1565668192272.png)

分析代码：为`data`键赋值的二级字典第一个键`type`的值决定了图表类型，包括`bar,scatter,contour`等；`x,y`确定了横纵轴的赋值；一级字典中的`layout`键的值决定了图像上打印的文本，下面嵌套的二级字典中`title`的值为题目内容，而下面嵌套的三级字典中`text`的值则是题目中文本内容（题目当然可以有非文本内容）。

### 构造图像对象与plotly.graph_objects模块

与图像字典相比，图像对象有如下四个好处：
１．能在输入错误属性是抛出异常；
２．内含python文档字符串，方便查资料；
３．既可以通过类风格调用对象属性，如`fig.data`，也可以通过字典风格调用对象属性，如`fig["layout"]`
４．可以链式调用方法，如`title = go.layout.Title(text = "hahaha")`

欲将这两者结合，我们可以选择初始化图像对象时给构造函数传入一个字典作为参数。

```python
import plotly.graph_objects as go
fig = go.Figure({
    "data":{
        "type":"scatter",
        "x":[2,5,4,7,3],
        "y":[1,7,4,3,6]
    },
    "layout":{"title":{"text":"test"},}
})
fig.show()

```

既然可以完全通过字典方式构造图像，那么也可以完全使用对象方法构造图像对象。下面的代码充满了*functional programming*的风格。

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[1,2,3],y=[4,2,5])],
    layout=dict(title=dict(text="bar chart"))
)
fig.show()

```

### plotly.express模块

这是一个高级抽象的模块，其中的方法用于可视化数据分析。

下面的例子中，我们使用`plotly.express`自带的示例数据集——鸢尾花聚类学习的结果，使用散点图来可视化聚类结果。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species"
)
fig.show()

```

![1565670831600](/home/shi/.config/Typora/typora-user-images/1565670831600.png)

分析代码，第一行引入模块；第二行加载数据，从模块自带的鸢尾花方法中加载数据；第三步初始化图像对象，调用模块的散点图方法传入四个参数，第一个是加载好的数据，第二、三个分别是横纵轴名称，第四个是颜色的意义，这里不同颜色代表了不同种类鸢尾花，还为我们自动生成了图例。与d3.js对比，语法可谓非常简洁，毕竟在d3中，仅仅使纵轴注释文字旋转成与轴平行就要如此大动干戈：`attr("transform","rotation(-90)")`

下面的代码利用散点图上方和右方的剩余空间陈列了直方图和地毯式投影图。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_x="histogram",
    marginal_y="rug"
)
fig.show()

```

![1565756257986](/home/shi/.config/Typora/typora-user-images/1565756257986.png)

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_x="box",
    marginal_y="violin"
)
fig.show()

```

![1565756521614](/home/shi/.config/Typora/typora-user-images/1565756521614.png)

类似地，上面的代码利用上方和右侧剩余空间陈列了盒子图和提琴图。将鼠标移动到提琴图上，了解virginica种鸢尾花的萼片最大、最小值、中位数等指标。

下面的代码则是利用数据值大小形象地表现萼片宽度来绘制图像，宽度越大，萼片尖端与花梗距离越远。对萼片宽度除以１００的操作是为了使结果看起来更清楚。

```python
import plotly.express as px
iris = px.data.iris()
iris["e"]=iris["sepal_width"]/100
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    error_x="e",
    error_y="e"
)
fig.show()

```

![1565757203214](/home/shi/.config/Typora/typora-user-images/1565757203214.png)

```python
import plotly.express as px
tips = px.data.tips()
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    facet_col="day",
    facet_row="time",
    color="smoker",
    category_orders={
        "day":["Thur","Fri","Sat","Sun"],
        "time":["Lunch","Dinner"]
    }
)
fig.show()

```

![1565762348486](/home/shi/.config/Typora/typora-user-images/1565762348486.png)

上面的代码使用`tips`数据集，与之前按类别分列分图的鸢尾花例子类似，这里的分图为二维形式，分行标准为午餐晚餐，分列标准为日子。

下面回到鸢尾花数据集，看看拥有４＊４维度的散点矩阵。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter_matrix(
    iris,
    color="species",
    dimensions=["sepal_width","sepal_length","petal_width","petal_length"]
)
fig.show()
```

![1565762812132](/home/shi/.config/Typora/typora-user-images/1565762812132.png)

下面是数据可视化领域非常常用的平行轴坐标视图，本例中是五维向量，每一维度的分数用折线连接。分析代码，我们可以看到平形轴构造函数的参数中，首次出现了物种编码而非物种本身作为颜色编码。而`labels`构造了一个字典，其键值对就是维度和对应标签名称。接下来是颜色连续映射，这就是右侧的颜色条，其赋值为选定的色系。最后的参数是颜色条的中值。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.parallel_coordinates(
    iris,
    color="species_id",
    labels={
        "species_id":"species",
        "sepal_width":"Sepal Width",
        "sepal_length":"Sepal Length",
        "petal_width":"Petal Width",
        "petal_length":"Petal Length"
    },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2
)
fig.show()

```

![1565763485171](/home/shi/.config/Typora/typora-user-images/1565763485171.png)

来看另一种色系的平行轴视图。

```python
import plotly.express as px
tips = px.data.tips()
fig = px.parallel_coordinates(
    tips,
    color="size",
    color_continuous_scale=px.colors.sequential.Inferno
)
fig.show()

```

![1565764357655](/home/shi/.config/Typora/typora-user-images/1565764357655.png)

我们的散点图同样可以添加连续的颜色轴。

```python
import plotly.express as px
tips = px.data.tips()
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    facet_col="sex",
    color_continuous_scale=px.colors.sequential.Viridis,
    color="size",
    render_mode="webg1"
)
fig.show()

```

![1565764635244](/home/shi/.config/Typora/typora-user-images/1565764635244.png)

接下来是比散点图多一个数据维度的图——气泡图。对气泡图而言，数据本身某种属性可以通过气泡半径大小直观地反映出来。本例中气泡半径与人口成正比。

```python
import plotly.express as px
gapminder = px.data.gapminder()
g_2007 = gapminder.query("year==2007")
fig = px.scatter(
    g_2007,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60
)
fig.show()

```

![1565765436666](/home/shi/.config/Typora/typora-user-images/1565765436666.png)

下面让时间的齿轮转起来。运动帧是年，而运动单位是国家。

```python
import plotly.express as px
gapminder = px.data.gapminder()
fig = px.scatter(
    gapminder,
    animation_frame="year",
    animation_group="country",
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    facet_col="continent",
    log_x=True,
    size_max=45,
    range_x=[100,100000],
    range_y=[25,90]
)
fig.show()

```

![1565767550663](/home/shi/.config/Typora/typora-user-images/1565767550663.png)

接下来把时间轴换为横轴，探究预期寿命。

```python
import plotly.express as px
gapminder = px.data.gapminder()
fig = px.line(
    gapminder,
    x="year",
    y="lifeExp",
    color="continent",
    line_group="country",
    hover_name="country",
    line_shape="spline",
    render_mode="svg"
)
fig.show()

```

![1565766711112](/home/shi/.config/Typora/typora-user-images/1565766711112.png)

人口也可以以曲线围成面积大小来可视化。

```python
import plotly.express as px
gapminder = px.data.gapminder()
fig = px.area(
    gapminder,
    x="year",
    y="pop",
    color="continent",
    line_group="country",
    hover_name="country"
)
fig.show()

```

![1565767409323](/home/shi/.config/Typora/typora-user-images/1565767409323.png)

绘制分布密度轮廓梯度图。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.density_contour(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_x="histogram",
    marginal_y="rug"
)
fig.show()

```

![1565767824048](/home/shi/.config/Typora/typora-user-images/1565767824048.png)

绘制次数统计分布热图。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.density_heatmap(
    iris,
    x="sepal_width",
    y="sepal_length",
    marginal_x="histogram",
    marginal_y="violin"
)
fig.show()
```

![1565768122302](/home/shi/.config/Typora/typora-user-images/1565768122302.png)

绘制传统型分布直方图。

```python
import plotly.express as px
tips = px.data.tips()
fig = px.histogram(
    tips,
    x="total_bill",
    y="tip",
    color="sex",
    marginal="box",
    hover_data=tips.columns
)
fig.show()

```

![1565768699785](/home/shi/.config/Typora/typora-user-images/1565768699785.png)

下面观察条带状散点图。

```python
import plotly.express as px
tips = px.data.tips()
fig = px.strip(
    tips,
    x="total_bill",
    y="time",
    orientation="v",
    color="smoker"
)
fig.show()

```

![1565828981811](/home/shi/.config/Typora/typora-user-images/1565828981811.png)

 下面观察二维三元坐标系(ternary coordinates)

```python
import plotly.express as px
ele = px.data.election()
fig = px.scatter_ternary(
    ele,
    a="Joly",
    b="Coderre",
    c="Bergeron",
    color="winner",
    size="total",
    hover_name="district",
    color_discrete_map={
        "Joly":"blue",
        "Bergeron":"green",
        "Coderre":"red",
    },
    size_max=15
)
fig.show()

```

![1565829450603](/home/shi/.config/Typora/typora-user-images/1565829450603.png)

下面观察三维散点坐标系。

```python
import plotly.express as px
ele = px.data.election()
fig = px.scatter_3d(
    ele,
    x="Joly",
    y="Coderre",
    z="Bergeron",
    color="winner",
    size="total",
    color_discrete_map={
        "Joly":"blue",
        "Bergeron":"green",
        "Coderre":"red"
    },
    hover_name="district",
    symbol="result"
)
fig.show()

```

![1565829751564](/home/shi/.config/Typora/typora-user-images/1565829751564.png)

下面，我们暂时告别笛卡尔坐标系，看看极坐标系下的图像。分析代码，可以发现极坐标参数是r-theta体系，与笛卡尔坐标系中对坐标轴命名不同。与上个例子不同散点符号由候选人输赢确定类似，这里不同散点符号由风力大小确定。

```python
import plotly.express as px
wind = px.data.wind()
fig = px.scatter_polar(
    wind,
    r="frequency",
    theta="direction",
    symbol="strength",
    color="strength",
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1]
)
fig.show()

```

![1565830245933](/home/shi/.config/Typora/typora-user-images/1565830245933.png)

类似地，极坐标下还有折线图和柱状图，这些图像也非常直观。在风场例子中，甚至比散点图效果要好。

```python
import plotly.express as px
wind = px.data.wind()
fig = px.line_polar(
    wind,
    r="frequency",
    theta="direction",
    line_close=True,
    color="strength",
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1]
)
fig.show()

```

![1565830878060](/home/shi/.config/Typora/typora-user-images/1565830878060.png)

```python
import plotly.express as px
wind = px.data.wind()
fig = px.bar_polar(
    wind,
    r="frequency",
    theta="direction",
    color="strength",
    template="plotly_dark",
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1]
)
fig.show()

```

![1565831276195](/home/shi/.config/Typora/typora-user-images/1565831276195.png)

### figure_factory模块

这个模块适用于特殊的域，能生成图像对象图片。下面的例子制造了一个展示二维波动向量流图的二维图。

```python
import numpy as np
import plotly.figure_factory as ff
x1,y1 = np.meshgrid(np.arange(0,2,.2),np.arange(0,2,.2))
u1 = np.cos(x1)*y1
v1 = np.sin(x1)*y1

fig = ff.create_quiver(x1,y1,u1,v1)
fig.show()
```

![1565676282610](/home/shi/.config/Typora/typora-user-images/1565676282610.png)

分析代码，`x1,y1 = np.meshgrid(np.arange(0,2,.2),np.arange(0,2,.2))`的作用是定义了啮合框，其横纵轴定义域均为０到２且离散间隔为０．２；随后定义了我们的波动函数，分别用x的正弦和余弦与y相乘；接下来调用`create_quiver`方法，传递四个参数分别是对啮合框的长宽和两个波动函数值。

### 制造分图

`plotly.subplots`模块能为我们制造分图，相关方法能预配置一些图表框方便我们添加分图。

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
fig = make_subplots(rows=1,cols=2)
fig.add_trace(go.Scatter(y=[1,5,2],x＝[1,2,3],mode="lines"),row=1,col=1)
fig.add_trace(go.Bar(y=[1,2,4],x=[1,2,3]),row=1,col=2)
fig.show()
```

![1565677628514](/home/shi/.config/Typora/typora-user-images/1565677628514.png)

分析代码，第三行调用`make_subplots()`函数制造分图，参数规定其为一行两列，共两个图。四、五行调用`fig`对象的`add_trace`方法，在由后两个参数确定插入图片的预留位置，而第一个参数决定插入图表的各种属性。

### 更新图

​	`add_trace`方法本质上就是为图对象添加实例，而这些对象本身是空的。正如上一个例子，创建的`subplots`本质上就是两个空图。这与在创建图像对象时立即对其进行初始化完全不同，似乎比那种方式灵活。
考察下面的代码：

```python
fig = go.Figure()
fig.add_trace(go.Bar(x=[1,2,3],y=[2,5,3],mode="line"))
fig.show()
```

其效果等价于：

```python
fig = go.Figure(data=[go.Bar(x=[1,2,3],y=[2,5,3])],mode="line")
fig.show()
```

只是前者在创建对象实例时调用了无参数的默认构造函数。
看下面的例子,仍然是用我们的鸢尾花数据集：

```python
import plotly.express as px
import plotly.graph_objs as go
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species"
)
fig.add_trace(
    go.Scatter(
        x=[2,4],
        y=[4,8],
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=False
    )
)
fig.show()

```

![1565679252428](/home/shi/.config/Typora/typora-user-images/1565679252428.png)

分析代码，前半部分加载鸢尾花数据集以及使用`px.scatter()`方法绘制散点图与之前的程序一致，而后面`add_trace()`方法调用的结果证明了当没有空对象可供赋值是，就将新图覆盖在原图上。

下面我们用另一种方法制造分图：通过某个标准对图中元素进行分类。

```python
import plotly.graph_objs as go
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    facet_col="species"
)
reference_line = go.Scatter(
    x=[2,4],
    y=[4,8],
    mode="lines",
    line=go.scatter.Line(color="gray"),
    showlegend=False
)
for i in range(1,4):
    fig.add_trace(reference_line,row=1,col=i)
fig.show()

```

![1565680569206](/home/shi/.config/Typora/typora-user-images/1565680569206.png)

分析代码，注意`facet_col="species"`，这个参数确定了按列分图的标准：不同种类的鸢尾花；第一个函数执行完毕，实际上三个分图的“预留位置”（虽然这听起来很不专业）就已经生成。第二个函数定义了一条分界线，`showlegend=Boolean`是决定是否单独为三条直线创建图例的参数。最后，使用循环为三个“预留位置”赋值图片实例，可以理解为抽象对象实例化。

### 背景元素自定义

这里给出更改某些元素属性的方法。有一点是毋庸置疑的：任何的属性都是键值对，因此最直接的方法是使用`dict()`方法生成键值对字典，再赋值给相应属性。

```python
import plotly.graph_objs as go
fig = go.Figure(
    data=[go.Scatter(y=[1,3,2],x=[1,2,3],line=dict(color="crimson"))],
    layout=dict(title=dict(text="chart"))
)
fig.show()

```

![1565689339022](/home/shi/.config/Typora/typora-user-images/1565689339022.png)

在magic underscore notation体系下，我们可以使用一些特殊的变量替换这些繁琐的充满functional programming风格的代码：`line=dict(color="crimson")`替换为`line_color="crimson"`  ；`layout=dict(title=dict(text="chart"))`替换为`layout_title_text="chart"`。总之，就是`A=dict(B=...)`替换为`A_B=...`。

下面的代码更改了字体大小，并使用了简洁的magic underscore notation。

```python
fig = go.Figure(data=go.Bar(y=[1,3,2]))
fig.update_layout(
    title_text="chart",
    title_font_size=30
)
fig.show()
```

![1565690197534](/home/shi/.config/Typora/typora-user-images/1565690197534.png)

### 更新元素

之前我们使用`add_trace`方法添加新图，而`add_{scatter,bar,et al}`可以任意添加新元素。

```python
from plotly.subplots import make_subplots
fig = make_subplots(rows=1,cols=2)

fig.add_scatter(y=[4,2,3.5],mode="markers",
                marker=dict(size=20,color="LightSeaGreen"),
                name="a",
                row=1,col=1)

fig.add_bar(y=[2,1,3],
            marker_color="MediumPurple",
            name="b",
            row=1,col=1)

fig.add_scatter(y=[2,3.5,4],mode="markers",
                marker=dict(size=20,color="MediumPurple"),
                name="c",
                row=1,col=2
                )

fig.add_bar(y=[1,3,2],
            marker_color="LightSeaGreen",
            name="d",
            row=1,col=2)

fig.show()


```

![1565746322961](/home/shi/.config/Typora/typora-user-images/1565746322961.png)

分析这段代码，首先使用`make_subplots()`方法制造一行两个分图，接下来通过添加数据属性，给每个图都分别添加了柱形图和散点图属性，对其尺寸、颜色等属性进行赋值；方法的最后两个参数决定了将新元素添加到哪个图中。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    facet_col="species",
    trendline="ols"
)
fig.update_traces(
    line=dict(dash="dot",width=4),
    selector=dict(type="scatter",mode="lines")
)
fig.show()

```

以上代码使用了`selector `  和　`update_traces`　，前者用于选定所有的符合参数条件的元素，类似d3 `d3.selectAll(),d3.select()`　的作用；后者对所有图进行更新，与`add_traces`不同，后者可以以相同方式更新多个图。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species"
)
fig.for_each_trace(
    lambda trace:trace.update(name=trace.name.replace("=",":"))
)
fig.show()

```

![1565750227071](/home/shi/.config/Typora/typora-user-images/1565750227071.png)

　前面的`update_traces()`仅仅能对多个图进行更新操作，而下面的`for_each_trace()`能对多个图对象进行自定义更新操作，如进行的更新依赖于某个属性值，这里就是使用`replace()`方法将“＝”替换为“；”。Lambda函数作为其第一个参数，就是执行自定义的更新操作；而后面的可选择参数当然包括`select,row,col`等。

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    facet_col="species"
)
fig.update_xaxes(showgrid=False)
fig.show()

```

![1565750452548](/home/shi/.config/Typora/typora-user-images/1565750452548.png)

上面的代码使用`update_xaxes()`方法对轴进行自定义更新。

### 链式调用

plotly拥有与d3类似的链式调用编程风格，前面的鸢尾花例子可以写成如下形式：

```python
import plotly.express as px
iris = px.data.iris()
(px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    facet_col="species",
    title="Iris Dataset"
).update_layout(title_font_size=32)
 .update_yaxes(showgrid=False)
 .update_traces(
    line=dict(dash="dot",width=4),
    selector=dict(type="scatter",mode="lines")
)).show()
```

![1565750914798](/home/shi/.config/Typora/typora-user-images/1565750914798.png)

这其中原本的图像对象以匿名对象方式创建，由于这些方法的返回值均为图像对象，因此支持链式调用。

自然，之前无论是通过函数式编程、字典参数还是magic underscore方式更改的属性值，也可以通过链式调用实现。

于是就有了下面几组等价的代码：

```python
layout=dict(title=dict(text="chart"))
layout:{title:{text:"chart"}}
layout_title_text="chart"
fig.layout.title.text="chart" # chain method
```

下面的例子更新了柱状图的边框：

```python
import plotly.graph_objs as go
fig = go.Figure(data=go.Bar(x=[1,2,3],y=[2,5,3]))
fig.data[0].marker.line.width=4
fig.data[0].marker.line.color="black"
fig.show()
```

![1565751445080](/home/shi/.config/Typora/typora-user-images/1565751445080.png)

### 主题

```python
import plotly.io as pio
pio.templates
```

通过这段命令检查模板。

![1565751891701](/home/shi/.config/Typora/typora-user-images/1565751891701.png)

```python
import plotly.express as px
gapminder=px.data.gapminder()
gapminder_2007=gapminder.query("year==2007")

for template in ["plotly_dark","xgridoff","presentation","ggplot2"]:
    fig = px.scatter(
        gapminder_2007,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=template,
        title="Gapminder 2007:'%s' theme" % template
    )
    fig.show()


```

![1565752824060](/home/shi/.config/Typora/typora-user-images/1565752824060.png)

![1565752841304](/home/shi/.config/Typora/typora-user-images/1565752841304.png)

![1565752854786](/home/shi/.config/Typora/typora-user-images/1565752854786.png)

![1565752925673](/home/shi/.config/Typora/typora-user-images/1565752925673.png)

对比这几个主题，可以明显看出presentation模板的字体最大，这是为了在展示是方便观众读图的。

分析代码，我们加载了gapminder这个数据集并从中查询了２００７年数据，下面构造了四种模板名称的列表循环遍历，每次循环就创建一个相应模板的图对象。这个对象是散点图，`size=pop` 意味着散点数据大小由气泡大小形式表示； `log_x=True`表示x轴不是线性的，而是经过了对数映射。

```python
import plotly.graph_objs as go
import pandas as pd
z_data = pd.read_csv("mt_bruno_elevation.csv")
fig = go.Figure(
    data=go.Surface(z=z_data.values),
    layout=go.Layout(
        title="Mt Bruno Elevation",
        width=500,
        height=500
    )
)
for template in ["plotly","plotly_dark","ggplot2","seaborn"]:
    fig.update_layout(
        template=template,
        title="Mt Bruno Elevation:'%s' theme" % template
    )
    fig.show()

```

以上代码引入了`pandas`模块，为了加载`.csv`文件。`go.Surface()`方法的作用就是绘制类似二元函数的图像，即三维空间中一个曲面。与上个例子相同，我们也使用了四种模板，由for循环遍历列表得到。

![1565754956056](/home/shi/.config/Typora/typora-user-images/1565754956056.png)

![1565754982512](/home/shi/.config/Typora/typora-user-images/1565754982512.png)

![1565754999913](/home/shi/.config/Typora/typora-user-images/1565754999913.png)

![1565755016235](/home/shi/.config/Typora/typora-user-images/1565755016235.png)

### 图片文件写入

```python
import os
if not os.path.exists("images"):
	os.mkdir("images")
fig.write_image("images/template.{png,jpeg,webp,svg,pdf,eps}")
```

os包（操作系统包）中包括了文件读写、与操作系统交互的方法。第２行代码检查当前目录下的目标目录是否存在，若不存在则在当前目录下创建新目标目录。随后调用图像对象的方法`write_image`写图片文件。

### 调整图片大小

我们可以对图片大小以及空余位置尺寸等外观进行配置。在`update_{}()`方法中，可以对多余空间进行配置。对于轴的配置，还可以在`update_{}()` 方法中传入参数`automargin=True`　。

```python
import plotly.express as px
tips = px.data.tips()
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    facet_col="sex",
    width=1000,
    height=500
    # adjust the size of figure
)
fig.update_layout(
    margin=dict(l=20,r=20,t=20,b=20),
    # set margin of left,right,top,bottom
    paper_bgcolor="LightSteelBlue"
)
fig.show()

```

![1565921630366](/home/shi/.config/Typora/typora-user-images/1565921630366.png)

### fig.show()自定义配置

`fig.show()`方法可以输入参数使图片在鼠标放置其上时随滚轮转动改变大小。

```python
fig.show(config=dict(scrollZoom=True))
```

使图像标题和x,y轴呈现可编辑形式。

```python
fig.show(config=dict(editable=True))
```

### 坐标轴配置

在`layout()`方法中，可以通过传递额外配置坐标轴。

```python
xaxes=dict(showgrid=False,zeroline=False)
```

这段代码配置了x轴，使图像没有垂直方向的网格线，没有画出的直角坐标轴。类似地，使用更新方法也可以达到相同的效果。

```python
fig.update_xaxes(showgird=False,zeroline=False,ticks="inside")
```

这段代码还使坐标轴刻度位于图像内。

```python
fig.update_yaxes(showticklabels=False)
```

这段代码是坐标轴刻度隐藏。

```python
fig.update_yaxes(nticks=20)
```

这段代码规定了y轴上必须有２０个刻度，不论值域是什么。

```python
fig.update_yaxes(tickvals=[2,3,6,7])
```

这段代码使y轴的标注刻度不均匀，用于突出某些特定值。

```python
fig.update_yaxes(tick0=0.25,dtick=0.5)
```

这段代码规定零刻度从0.25开始，且步进为0.5。

```python
fig.update_xaxes(tickangle=45,tickfont={
	"family":'Rockwell',
	"color":'crimson',
	"size":14
})
```

这段代码规定刻度旋转４５度，规定了字体、颜色、大小。

下面的例子展示了分级目录作为轴的标签，实际结构是多维数组。

```python
import plotly.graph_objs as go
fig = go.Figure()
fig.add_trace(go.Box(
    x=[2,3,1,5],
    y=[
        ['First','First','First','First'],
        ["A","A","A","A"]
    ],
    name="A",
    orientation="h"
))
fig.add_trace(go.Box(
    x=[8,3,6,5],
    y=[
        ['First','First','First','First'],
        ["B","B","B","B"]
    ],
    name="B",
    orientation="h"
))
fig.add_trace(go.Box(
    x=[2,3,2,5],
    y=[
        ['Second','Second','Second','Second'],
        ["C","C","C","C"]
    ],
    name="C",
    orientation="h"
))
fig.add_trace(go.Box(
    x=[7.5,3,6,4],
    y=[
        ['Second','Second','Second','Second'],
        ["D","D","D","D"]
    ],
    name="D",
    orientation="h"
))
fig.update_layout(title="Multi-category axis")
fig.show()

```

![1565927632732](/home/shi/.config/Typora/typora-user-images/1565927632732.png)

```python
fig.update_xaxes(range=[1,3])
```

这段代码是人为规定坐标轴的域。若没有规定具体域，可以通过`rangemode`参数确定方式，包括`nonegative,tozero,normal` 。顾名思义，第一个值域非负，第二个值域是包括零的一侧，第三个值域是从数据集的最小值到最大值。

```python
fig.update_xaxes(showgrid=True,gridwidth=1,gridcolor='LightPink')
```

这段代码生成粉红色网格线，显得非常美观。

```python
fig.update_yaxes(type="log")
```

这段代码将y轴重新进行对数映射。

### 图例

图例的一般逻辑是，在只有一种图象时默认隐藏`showlegend==False`，在有超过一种图象时默认展开`showlegend==True`。图例名称默认与图象名称一致。

```python
fig.update_layout(legend_orientation="h")
```

图例默认是垂直排列`legend_orientation=="v"`。这段代码把图例改为水平排列。

下面的例子是多重图例。

```python
import plotly.graph_objs as go
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1,2,3],
    y=[2,1,3],
    legendgroup="group1",
    name="first legend group",
    mode="markers",
    marker=dict(color="crimson",size=15)
))
fig.add_trace(go.Scatter(
    x=[1,2,3],
    y=[1,1,1],
    legendgroup="group1",
    name="first legend group",
    mode="lines",
    line=dict(color="crimson")
))
fig.add_trace(go.Scatter(
    x=[1,2,3],
    y=[4,7,5],
    legendgroup="group2",
    name="second legend group",
    mode="markers",
    marker=dict(color="MediumPurple",size=15)
))
fig.add_trace(go.Scatter(
    x=[1,2,3],
    y=[6,6,6],
    legendgroup="group2",
    name="second legend group",
    mode="lines",
    line=dict(color="MediumPurple")
))
fig.show()

```

![1566135286264](/home/shi/.config/Typora/typora-user-images/1566135286264.png)

