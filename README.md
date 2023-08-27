# Tailwind
A python UI module

## Usage

### Window
``tailwind.window``

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
    "anchor": `util.CenterAnchor().get_anchor()`
  }
}
```
Keep in mind you will have to import `tailwind.util` and `tailwind.widgets`

#### `def __call__(self, *args, **kwargs)`
Returns the `window._ctk` private attribute. This is only for the backend but you may use it for creating your own widgets with `tailwind.widget.Widget()`

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
`tailwind.graphing`
