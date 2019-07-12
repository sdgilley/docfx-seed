# code snippets for the quickstart-create-workspace-with-python article
# <import>
import azureml.core
print(azureml.core.VERSION)
# </import>

# this is NOT a snippet.  If this code changes, go fix it in the article!
from azureml.core import Workspace
ws = Workspace.create(name='myworkspace',
                      subscription_id='<subscription-id>',
                      resource_group='myresourcegroup',
                      create_resource_group=True,
                      location='eastus2' # or other supported Azure region
                     )

# <getDetails>
ws.get_details()
# </getDetails>

# <writeConfig>
# Create the configuration file.
ws.write_config()

# Use this code to load the workspace from 
# other scripts and notebooks in this directory.
# ws = Workspace.from_config()
# </writeConfig>

# <useWs>
from azureml.core import Experiment

# Create a new experiment in your workspace.
exp = Experiment(workspace=ws, name='myexp')

# Start a run and start the logging service.
run = exp.start_logging()

# Log a single  number.
run.log('my magic number', 42)

# Log a list (Fibonacci numbers).
run.log_list('my list', [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) 

# Finish the run.
run.complete()
# </useWs>

# <viewLog>
print(run.get_portal_url())
# </viewLog>


# <delete>
ws.delete(delete_dependent_resources=True)
# </delete>