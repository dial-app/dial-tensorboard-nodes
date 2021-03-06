## vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

from typing import TYPE_CHECKING, List

import dependency_injector.providers as providers
from dial_core.node_editor import Node
from tensorflow.keras.callbacks import Callback

from .tb_instance_widget import TensorboardInstanceWidgetFactory

if TYPE_CHECKING:
    from .tensorboard_instance_widget import TensorboardInstanceWidget


class TensorboardInstanceNode(Node):
    def __init__(
        self, tensorboard_instance_widget: "TensorboardInstanceWidget",
    ):
        super().__init__(
            title="Tensorboard Instance", inner_widget=tensorboard_instance_widget,
        )

        self.add_output_port("Keras Callbacks", port_type=List[Callback])

        self.outputs["Keras Callbacks"].set_generator_function(
            self.inner_widget.get_callbacks
        )

    def __reduce__(self):
        return (TensorboardInstanceNode, (self.inner_widget,), super().__getstate__())


TensorboardInstanceNodeFactory = providers.Factory(
    TensorboardInstanceNode,
    tensorboard_instance_widget=TensorboardInstanceWidgetFactory,
)
