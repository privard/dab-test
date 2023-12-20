# Databricks Asset Bundles Test

Trying to make DAB work with a monorepo with shared libraries.

## Setup

1. `pip install -r requirements-pip.txt`
2. `pip install -r requirements-dev.txt`
3. `cd libs/shared_lib && pip install -e .`

## Issues

### Notebook Task

In `bundles/workflow_notebook` you will find a bundle that defines a notebook task. The notebook task uses `shared_lib.my_module`. This works locally, but `databricks bundle deploy` fails because the artifact declared in the bundle's databricks.yml file is outside the bundle root.

(bundles/workflow_notebook/databricks.yml)
```yaml
artifacts:
  shared_lib:
    type: whl
    path: ../../libs/shared_lib/
```

### Wheel Task

In `bundles/workflow_whl` you will find a bundle that defines a "python_wheel_task" task. The wheel's entrypoint uses `shared_lib.my_module`. This works locally, but `databricks bundle deploy` fails because one of the libraries declared in the bundle's resource (resources/task_whl.yml) is outside the bundle root.

(bundles/workflow_whl/resources/task_whl.yml)
```yaml
 libraries:
      - whl: ../dist/*.whl
      # Adding the below as suggested in the docs
      # https://docs.databricks.com/en/dev-tools/bundles/library-dependencies.html
      # fails because the whl path is outside the bundle root
      - whl: ../../libs/shared_lib/dist/*.whl
```