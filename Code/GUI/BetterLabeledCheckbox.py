
from panda3d.core import Vec3

from ..Util.DebugObject import DebugObject
from .BetterCheckbox import BetterCheckbox
from .BetterOnscreenText import BetterOnscreenText
import direct.gui.DirectGuiGlobals as DGG


class BetterLabeledCheckbox(DebugObject):

    """ This is a checkbox, combined with a label. The arguments are
    equal to the Checkbox and OnscreenText arguments. """

    def __init__(self, parent=None, x=0, y=0, chb_callback=None,
                 chb_args=None, chb_checked=True, text="", text_size=18,
                 radio=False, text_color=None, expand_width=100):
        DebugObject.__init__(self)
        if chb_args is None:
            chb_args = []

        if text_color is None:
            text_color = Vec3(1)

        self._checkbox = BetterCheckbox(
            parent=parent, x=x, y=y,
            callback=chb_callback, extra_args=chb_args,
            checked=chb_checked, radio=radio, expand_width=expand_width)
        self._text = BetterOnscreenText(x=x + 26, y=y + 10 + text_size // 4,
                                        text=text, align="left", parent=parent,
                                        size=text_size, color=text_color, may_change=True)

        self._checkbox._node.bind(DGG.WITHIN, self._on_node_enter)
        self._checkbox._node.bind(DGG.WITHOUT, self._on_node_leave)


    def _on_node_enter(self, *args):
        """ Internal callback when the node gets hovered """
        print("node enter")
        # self._checkbox._node["frameColor"] = (0, 0, 0, 1)
        self._text._node["fg"] = (0.5, 0.5, 0.5, 1.0)

    def _on_node_leave(self, *args):
        """ Internal callback when the node gets no longer hovered """
        print("node leave")
        # self._checkbox._node["frameColor"] = (0, 0, 0, 1)
        self._text._node["fg"] = (0.4, 0.4, 0.4, 1.0)

    def get_checkbox(self):
        """ Returns a handle to the checkbox """
        return self._checkbox

    def get_label(self):
        """ Returns a handle to the label """
        return self._text
