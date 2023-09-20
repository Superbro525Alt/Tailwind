<div align="center">
<img width="455" height="122" src="tailwind_logo.png" title="Tailwind" alt="Tailwind" style="color: white;font-size: 61px;line-height: 122px;text-align: cen
ter;background-color: transparent;">
</div>
<div align="center">

![Status Badge](https://github.com/Superbro525Alt/Tailwind/actions/workflows/python-app.yml/badge.svg)
![Status Badge](https://github.com/Superbro525Alt/Tailwind/actions/workflows/package-deploy.yml/badge.svg)

</div>

```console
pip install tailwindall
```

> [!IMPORTANT]
> A python all in one package for doing everything, including:
> - Graphing
> - UI
> - Website development
> - Statistics
> - Maths
>   - Shape identification
>   - Angle calculation
> - And more!


> [!NOTE] 
> ## Future Updates
> - [ ] Add widgets
>   - [ ] For web development
>   - [ ] For UI development
> - [ ] Add different types of graphs
> - [ ] Add more statistics functions
> - [ ] Add more math functions
> - [ ] Add more util functions
> - [ ] Improve syntax of tw script
> - [ ] Improve networking library
> - [ ] Add embedded pygame/turtle windows for graphics
>   - [x] Add multiple windows rendering at once

> [!WARNING]
> Math/Web module is not finished yet

## Usage

### Window
``tailwindall.window``

```python
class Window:
    
    def __init__(self, style, name, options={}):

    def main_loop(self):

    def add_widget(self, widget: any, options={}):
        
    def __call__(self, *args, **kwargs):
        
    def quit(self):

    def add_on_exit_function(self, func):

    def remove_on_exit_function(self, func):

    def add_garbage_collect_path(self, path):

    def remove_garbage_collect_path(self, path):
```

#### `def __init__(style, name, options)`
You pass in a style (can be file or a string)
If you choose to pass in a file use `style = "path/to/file"`

The file and string must be in the format 
```css
.class-name {key:value;key2:value2;}
tag {key:value;key2:value2;}
```
#### `def main_loop()`
Runs the main loop. Any code after this will not be executed. Use `add_on_exit_function(func)` to add a function to be called when the window is closed.

#### `def add_widget(widget: any, options={})`
Use the function to add a widget to the window, a base options file will be as follows:
```json
{
  "place": {
    "relx": 0,
    "rely": 0,
    "anchor": util.CenterAnchor().get_anchor()
  }
}
```
Keep in mind you will have to import `tailwindall.util` and `tailwindall.widgets`

#### `def __call__(self, *args, **kwargs)`
Returns the `window._ctk` private attribute. This is only for the backend but you may use it for creating your own widgets with `tailwindall.widget.Widget()`

#### `def quit(self)`
Does garbage collection of files created when graphs are rendered. Add your own files to this list using `add_garbage_collect_path(self, path)`to add a path to the garbage collection

#### `def add_on_exit_function(self, func)`
Adds an on exit function to the list, this function will be called on the closing of the window.

#### `def remove_on_exit_function(self, func)`
Removes an on exit function from the list <ins>NOT RECOMMENDED</ins>

#### `def add_garbage_collect_path(self, path)`
Add your own garbage collection path to be deleted on window close

#### `def remove_garbage_collect_path(self, path)`
Remove garbage collect path <ins>NOT RECOMMENDED</ins>

### Graphing
`tailwindall.graphing`

These are the acceptable types of graphs to be put in the ```GraphOptions.type``` parameter.
#### Graph Options
```python
class GraphOptions:
    def __init__(self, xLabel, yLabel, title, size: util.ImageScale, type: str):
```
Graph options take in:
- `xLabel` (a label for the x axis)
- `yLabel` (a label for the y axis)
- `title` a title for the graph
- `size` a `util.ImageScale` object
- `type` a string containing the type of graph. Must be in `GRAPH_TYPES`

##### `def display(self)`
The display function creates a graph and returns an `widgets.Image` object that can be directly added to a `tailwindall.window.Window` using `window.add_widget(widget)`

#### Line Graph
`tailwindall.graphing.LineGraph`

```python
class LineGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
    def display(self):
```

Used to create line graphs. `display()` returns a widget to render on the screen

#### Bar Graph
`tailwindall.graphing.BarGraph`

```python
class BarGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
    def display(self):
```

Used to create bar graphs. `display()` returns a widget to render on the screen

#### Pie Graph
`tailwindall.graphing.PieGraph`

```python
class PieGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
    def display(self):
```

Used to create pie graphs. `display()` returns a widget to render on the screen

#### Scatter Graph
`tailwindall.graphing.ScatterGraph`

```python
class ScatterGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
    def display(self):
```

Used to create scatter graphs. `display()` returns a widget to render on the screen

#### Histogram Graph
`tailwindall.graphing.HistogramGraph`

```python
class HistogramGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
    def display(self):
```

Used to create histogram graphs. `display()` returns a widget to render on the screen

#### Box Plot Graph
`tailwindall.graphing.BoxPlotGraph`

```python
class BoxPlotGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
    def display(self):
```

Used to create box plot graphs. `display()` returns a widget to render on the screen

#### Area Graph
`tailwindall.graphing.AreaGraph`

```python
class AreaGraph(Graph):
    def __init__(self, xData, yData, options: GraphOptions, window):
    def display(self):
```

Used to create area graphs. `display()` returns a widget to render on the screen

## Statistics
`tailwindall.statistics_lib.statistics`

### Mean
`tailwindall.statistics_lib.statistics.mean(data)`

Returns the mean of the data

### Median
`tailwindall.statistics_lib.statistics.median(data)`

Returns the median of the data

### Mode
`tailwindall.statistics_lib.statistics.mode(data)`

Returns the mode of the data

### Range
`tailwindall.statistics_lib.statistics.range(data)`

Returns the range of the data

### Standard Deviation
`tailwindall.statistics_lib.statistics.standard_deviation(data)`

Returns the standard deviation of the data

### Variance
`tailwindall.statistics_lib.statistics.variance(data)`

Returns the variance of the data

### Quartiles
`tailwindall.statistics_lib.statistics.quartiles(data)`

Returns the quartiles of the data

### Interquartile Range
`tailwindall.statistics_lib.statistics.interquartile_range(data)`

Returns the interquartile range of the data

### Z-Score
`tailwindall.statistics_lib.statistics.z_score(data)`

Returns the z-score of the data

### Z-Scores
`tailwindall.statistics_lib.statistics.z_scores(data)`

Returns the z-scores of the data

### Percentile
`tailwindall.statistics_lib.statistics.percentile(data, percentile)`

Returns the percentile of the data

### Outliers
`tailwindall.statistics_lib.statistics.outliers(data)`

Returns the outliers of the data

### Remove Outliers
`tailwindall.statistics_lib.statistics.remove_outliers(data)`

Returns the data with the outliers removed

### Covariance
`tailwindall.statistics_lib.statistics.covariance(data1, data2)`

Returns the covariance of the data

### Correlation
`tailwindall.statistics_lib.statistics.correlation(data1, data2)`

Returns the correlation of the data

### Least Squares Regression
`tailwindall.statistics_lib.statistics.least_squares_regression(data1, data2)`

Returns the least squares regression of the data

### Least Squares Regression Line
`tailwindall.statistics_lib.statistics.least_squares_regression_line(data1, data2)`

Returns the least squares regression line of the data

## Util
`tailwindall.util`

### Constants
```python
NULL = None
null = NULL
```
These are used to create a more diverse usage of null types.

### Type Utilities
`tailwindall.util.Types`


#### `def are_list_items_same(cls, this: list, other: list):`
<ins>`@classmethod`</ins>

Can be called using `tailwindall.util.Types.are_list_items_same(this, other)` depending on how you import it. You pass in two lists and the function will return a list telling you if the item in the same index in each list are the same type.

#### `def is_class_same(cls, this: object, other: object):`
<ins>`@classmethod`</ins>

Can be called using `tailwindall.util.Types.is_class_same`. It takes in two objects and outputs wheather each attribute in each object is the same and if it is not in the other object it outputs `None`. The return value is a dictionary containing all the attribute names from each object as keys and if the are the same between objects as the value. 

#### `def is_type(cls, this, other):`
<ins>`@classmethod`</ins>

Can be called using `tailwindall.util.Types.is_type`. Takes in two arguments `this` and `other`and returns weather they are the same object type.

### File Utilities
`tailwindall.util`

`def read_file(file, options={}):`

Reads a file and returns contents. `options` allow for the user to input `{"strip": True}` to strip the lines before returning and `{"lines": True}`to return the value of readlines.

The only other argument is `file` which is the path to the file that you are trying to read.

### Anchor Points
`tailwindall.util`

#### General

To access the anchor for use with placing widgets use `anchor_class.get_anchor()`. `get_anchor()` is a class method allowing it to be called without it's respective object needing to be instantiated.

#### Current Types
The current anchors are as follows:

- `EmptyAnchor`
- `CenterAnchor`
- `NorthAnchor`
- `NorthEastAnchor`
- `EastAnchor`
- `SouthEastAnchor`
- `SouthAnchor`
- `WestAnchor`
- `NorthWestAnchor`

### Image Scale
`tailwindall.util.ImageScale(width, height)`

Takes in a width and a height and returns it when called (`image_scale()`)

### Other

#### Execute List
`tailwindall.util.exec_list(functions, final=None):`

Takes in a list of functions and a final function to be called (_not required_)

It executes each function in the list before finishing with the final function.


## Widgets
`tailwindall.widgets`

### Button
`tailwindall.widgets.Button`

`def __init__(self, window, style={}, properties={}, binds={}, **kwargs)`

Takes in the arguments `window` which is a `tailwindall.window.Window`, an object that contains the styles that will be applied to the object. The keys are the property and the values are the new value. Properties work the same and binds take in the event as the key and the function that is called as the value. If text is a property it will be set as the text in the button.

Returns a button that can be rendered onto the screen using `window.add_widget(widget)`

### Label
`tailwindall.widgets.Label`

`def __init__(self, window, style={}, properties={}, binds={}, **kwargs):`

Takes in the arguments `window` which is a `tailwindall.window.Window`, an object that contains the styles that will be applied to the object. The keys are the property and the values are the new value. Properties work the same and binds take in the event as the key and the function that is called as the value. If text is a property it will be set as the text in the label.

Returns a label that can be rendered onto the screen using `window.add_widget(widget)`

### Entry
`tailwindall.widgets.Entry`

`def __init__(self, window, style={}, properties={}, binds={}, **kwargs):`

Takes in the arguments `window` which is a `tailwindall.window.Window`, an object that contains the styles that will be applied to the object. The keys are the property and the values are the new value. Properties work the same and binds take in the event as the key and the function that is called as the value. If text is a property it will be set as the text in the entry.

Returns an entry that can be rendered onto the screen using `window.add_widget(widget)`

### Frame
`tailwindall.widgets.Frame`

`def __init__(self, window, style={}, properties={}, binds={}, **kwargs):`

Takes in the arguments `window` which is a `tailwindall.window.Window`, an object that contains the styles that will be applied to the object. The keys are the property and the values are the new value. Properties work the same and binds take in the event as the key and the function that is called as the value. 

Returns a frame that can be rendered onto the screen using `window.add_widget(widget)`

### Canvas
`tailwindall.widgets.Canvas`

`def __init__(self, window, style={}, properties={}, binds={}, **kwargs):`

Takes in the arguments `window` which is a `tailwindall.window.Window`, an object that contains the styles that will be applied to the object. The keys are the property and the values are the new value. Properties work the same and binds take in the event as the key and the function that is called as the value. 

Returns a canvas that can be rendered onto the screen using `window.add_widget(widget)`

### Scrollbar
`tailwindall.widgets.Scrollbar`

`def __init__(self, window, style={}, properties={}, binds={}, **kwargs):`

Takes in the arguments `window` which is a `tailwindall.window.Window`, an object that contains the styles that will be applied to the object. The keys are the property and the values are the new value. Properties work the same and binds take in the event as the key and the function that is called as the value.

Returns a scrollbar that can be rendered onto the screen using `window.add_widget(widget)`

### Scrollview
`tailwindall.widgets.Scrollview`

`def __init__(self, window, style={}, properties={}, binds={}, **kwargs):`

Takes in the arguments `window` which is a `tailwindall.window.Window`, an object that contains the styles that will be applied to the object. The keys are the property and the values are the new value. Properties work the same and binds take in the event as the key and the function that is called as the value. 

Returns a scrollview that can be rendered onto the screen using `window.add_widget(widget)`
'
### Image
`tailwindall.widgets.Image`

`def __init__(self, window, image, style={}, properties={}, binds={}, **kwargs):`

Takes in the arguments `window` which is a `tailwindall.window.Window`, an object that contains the styles that will be applied to the object. The keys are the property and the values are the new value. Properties work the same and binds take in the event as the key and the function that is called as the value. `Image` is the path to the image to be rendered.

Returns an image that can be rendered onto the screen using `window.add_widget(widget)`

# Developer

## Widget
`tailwindall.widget.Widget`

`def __init__(self, style, properties, binds, _ctk):`

Takes in `style`, `properties`, `binds` and a `_ctk`(an object that can actually be rendered onto the screen with styles).
It has no public methods other then `reload_styles()`, `reload_properties()` and `reload_binds()`. These are all called on creation so they should generally have no reason to be called again.

## Styles
`tailwindall.styles.Styles`

`def parse(cls, style: str, file=False)`

<ins>`@classmethod`</ins>

Parses a css (style) string or file into an object containing classnames, ids and tags each containing the respective properties.

## Graphing

### Graph Class
```python
class Graph:
    def __init__(self):
    def display(self):
```

Create a figure under the property of `self.graph` and inherit from this class for creating new graphs
