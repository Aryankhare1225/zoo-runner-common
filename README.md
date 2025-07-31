# zoo-runner-common

A shared utility library for ZOO-Project CWL runners – centralizing reusable components across runners like **Calrissian**, **Argo Workflows**, and **WES**.

---

## Overview

The `zoo-runner-common` repository provides core shared components used across multiple ZOO CWL runners. It avoids duplication by hosting:

- Common base classes (`BaseRunner`)
- Zoo-specific configuration handlers (`ZooConf`, `ZooInputs`, `ZooOutputs`)
- CWL workflow parsing and resource evaluation (`CWLWorkflow`)
- CWL wrapping utilities for stage-in, stage-out (`wrapper_utils`)
- Service stubs (`ZooStub`) to update job status

---

## Directory Structure

zoo-runner-common
- base_runner.py # Abstract BaseRunner used by all CWL runners
- zoostub.py # ZooStub class to communicate with ZOO kernel
- zoo_conf.py # ZooConf, ZooInputs, ZooOutputs, CWLWorkflow, ResourceRequirement
- wrapper_utils.py # Utilities to wrap CWL workflow with stage-in/out
- init.py # Optional for Python package recognition


---

## Setup

No external installation is needed. Just include the path in your `PYTHONPATH` or structure your runners to import directly:

```bash
export PYTHONPATH="$PYTHONPATH:/path/to/zoo-runner-common"
```

Or structure your project such that imports like the following work:

```python
from zoo_runner_common.base_runner import BaseRunner
from zoo_runner_common.zoo_conf import ZooConf, ZooInputs, ZooOutputs, CWLWorkflow
```
---

## Components
Module	Description
BaseRunner	Abstract runner blueprint all runners must extend
ZooConf	Parses conf.json, manages job ID, state
ZooInputs	Parses inputs.json, formats CWL-style parameters
ZooOutputs	Handles writing and setting output results
CWLWorkflow	Loads, parses, and analyzes CWL workflows
ResourceRequirement	Parses and evaluates CWL resource hints/requirements
wrapper_utils	Provides helper to build wrapped CWL pipeline
ZooStub	Interacts with ZOO's lenv for progress updates
---

## Used By
- zoo-wes-runner
- zoo-argowf-runner

zoo-calrissian-runner
