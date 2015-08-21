'''
Created on Jul 27, 2015

@author: hsorby
'''
from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget

class SemiAutoSceneviewerWidget(SceneviewerWidget):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(SemiAutoSceneviewerWidget, self).__init__(parent)
        self._model = None
        
    def setModel(self, model):
        self._model = model
        
