'''
Created on Jul 27, 2015

@author: hsorby
'''
from opencmiss.zinc.context import Context


class SemiAutoModel(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._context = Context('heartsurface')
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()
        material_module = self._context.getMaterialmodule()
        material_module.defineStandardMaterials()
        self.clear()

    def clear(self):
        self._region = None
        self._image_data = None

    def initialize(self):
        self._region = self._context.createRegion()

    def getRegion(self):
        return self._region

    def getContext(self):
        return self._context

    def getPointCloud(self):
        return []

    def setImageData(self, image_data):
        self._image_data = image_data
