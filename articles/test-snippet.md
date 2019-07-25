Testing a code snippet
=====================

This one already works
---------------------
Here is a code snippet from a Python file, which is supported today:

[!code-python[](codefiles/create-workspace.py?name=writeConfig)]

Here's our hack
---------------------

Here is that same snippet from a Jupyter notebook, which we added in our hack.  Note the syntax: `[!notebook-<language>[](<codepath>?name={tagname})]]`

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
