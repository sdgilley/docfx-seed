Testing a code snippet
=====================

This one should work now
---------------------
Here is a code snippet from a Python file.  

[!code-python[](codefiles/create-workspace.py?name=writeConfig)]

This one is what we are adding
---------------------

Here is that same snippet from a Jupyter notebook.

[!notebook-python[](codefiles/create-workspace.ipynb?name=writeConfig)]

Results
--------

Both sections should display  code that looks like this:

```python
# Create the configuration file.
ws.write_config()

# Use this code to load the workspace from 
# other scripts and notebooks in this directory.
# ws = Workspace.from_config()
```
