More tests
=====================

## Imports
----------

[!code-ipynb[](codefiles/train-hyperparameter.ipynb?name=importCore)]

Should be same as:
```python
# Check core SDK version number
import azureml.core

print("SDK version:", azureml.core.VERSION)
```

Diagnostics
--------
[!code-ipynb[](codefiles/train-hyperparameter.ipynb?name=diagnostics)]

Should be same as:
```# Check core SDK version number
import azureml.core

print("SDK version:", azureml.core.VERSION)
```

Initialize
------------
[!code-ipynb[](codefiles/train-hyperparameter.ipynb?name=initialize)]

Should be same as:
```python
from azureml.core.workspace import Workspace

ws = Workspace.from_config()
print('Workspace name: ' + ws.name, 
      'Azure region: ' + ws.location, 
      'Subscription id: ' + ws.subscription_id, 
      'Resource group: ' + ws.resource_group, sep = '\n')
```

Create compute
------------

[!code-ipynb[](codefiles/train-hyperparameter.ipynb?name=create_compute)]

Should be same as:
```python
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

# choose a name for your cluster
cluster_name = "gpu-cluster"

try:
    compute_target = ComputeTarget(workspace=ws, name=cluster_name)
    print('Found existing compute target.')
except ComputeTargetException:
    print('Creating a new compute target...')
    compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_NC6', 
                                                           max_nodes=4)

    # create the cluster
    compute_target = ComputeTarget.create(ws, cluster_name, compute_config)

    compute_target.wait_for_completion(show_output=True)

# use get_status() to get a detailed status for the current cluster. 
print(compute_target.get_status().serialize())
```

Duplicate name
------------

[!code-ipynb[](codefiles/train-hyperparameter.ipynb?name=duplicate)]

> [!IMPORTANT]
> Should give an error, the name is not unique in the notebook file.

Name not found
-----

[!code-ipynb[](codefiles/train-hyperparameter.ipynb?name=blah)]

> [!IMPORTANT]
> Should give an error, the name is not present in the notebook file.