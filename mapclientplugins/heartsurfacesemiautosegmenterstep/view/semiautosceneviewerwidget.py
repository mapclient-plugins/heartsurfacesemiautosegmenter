"""
Created on Jul 27, 2015

@author: hsorby
"""
from cmlibs.widgets.sceneviewerwidget import SceneviewerWidget


class SemiAutoSceneviewerWidget(SceneviewerWidget):

    def __init__(self, parent=None):
        super(SemiAutoSceneviewerWidget, self).__init__(parent)
        self._model = None

    def setModel(self, model):
        self._model = model
