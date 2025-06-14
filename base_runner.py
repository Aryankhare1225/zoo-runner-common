from abc import ABC, abstractmethod
import logging
import types
import sys
import os

# Shared ZooStub import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from zoostub import ZooStub

zoo = ZooStub()
logger = logging.getLogger()

class BaseRunner(ABC):
    def __init__(self, inputs, conf, outputs, handler=None):
        self.inputs = inputs
        self.conf = conf
        self.outputs = outputs
        self.handler = handler
        self.zoo_conf = types.SimpleNamespace(conf=self.conf)

    def update_status(self, progress: int, message: str = ""):
        if "lenv" in self.conf:
            self.conf["lenv"]["message"] = message
        zoo.update_status(self.conf, progress)

    def log_output(self, output):
        logger.info("[BaseRunner] Output: %s", output)

    def validate_inputs(self):
        logger.info("[BaseRunner] Validating inputs...")
        return True

    def prepare(self):
        """Shared pre-execution logic."""
        logger.info("execution started")
        self.update_status(progress=2, message="starting execution")
        logger.info("wrap CWL workflow with stage-in/out steps")

        processing_parameters = {
            **self.get_processing_parameters(),
            **(self.handler.get_additional_parameters() if self.handler else {})
        }

        return types.SimpleNamespace(
            cwl=self.wrap(), params=processing_parameters
        )

    @abstractmethod
    def execute(self):
        raise NotImplementedError
