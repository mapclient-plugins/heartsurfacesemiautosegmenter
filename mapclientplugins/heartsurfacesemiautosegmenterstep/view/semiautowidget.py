'''
Created on Jul 27, 2015

@author: hsorby
'''
from PySide2 import QtWidgets

from mapclientplugins.heartsurfacesemiautosegmenterstep.view.ui_semiautowidget import Ui_SemiAutoWidget

class SemiAutoWidget(QtWidgets.QWidget):
    '''
    classdocs
    '''


    def __init__(self, model, parent=None):
        '''
        Constructor
        '''
        super(SemiAutoWidget, self).__init__(parent)
        self._ui = Ui_SemiAutoWidget()
        self._ui.setupUi(self)
        self._ui.widgetZinc.setContext(model.getContext())
        self._ui.widgetZinc.setModel(model)
        self._model = model
        self._callback = None
        self._makeConnections()
        
    def _makeConnections(self):
        self._ui.pushButtonContinue.clicked.connect(self._continueButtonClicked)
        self._ui.widgetZinc.graphicsInitialized.connect(self._graphicsInitialized)
        
    def _continueButtonClicked(self):
        self._callback()
        
    def _graphicsInitialized(self):
        sceneviewer = self._ui.widgetZinc.getSceneviewer()
        if sceneviewer is not None:
            scene = self._model.getRegion().getScene()
            sceneviewer.setScene(scene)
            sceneviewer.viewAll()
            
    def clear(self):
        self._model.clear()
        
    def initialize(self):
        self._model.initialize()
        
    def setImageData(self, image_data):
        self._model.setImageData(image_data)
        
    def getPointCloud(self):
        return self._model.getPointCloud()
    
    def registerDoneExecution(self, callback):
        self._callback = callback
        
        
            
    
        
