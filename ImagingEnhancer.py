#!/usr/bin/env python

__author__ = "MKozuch"

import sys
import os
from PyQt4 import QtCore, QtGui
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from ImagingEnhancerUI import Ui_Form
import vtk
import itk
from vtk.util import numpy_support
import matplotlib.pyplot as plt
import numpy as np

STARTINGPATH = 'F:\\Dropbox\\Studia\\Sprawozdania (1)\\SODMProjekt\\dicom_images'
FILENAME = 'brain_012.dcm'
FILENAME = 'CT-MONO2-16-ankle.dcm'

class MIEnhancer(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.reader = vtk.vtkDICOMImageReader()

        #self.viewerL = vtk.vtkImageViewer2()
        #self.viewerR = vtk.vtkImageViewer2()

        self.renL = vtk.vtkRenderer()
        self.ui.leftVtk.GetRenderWindow().AddRenderer(self.renL)
        self.renR = vtk.vtkRenderer()
        self.ui.rightVtk.GetRenderWindow().AddRenderer(self.renR)

        self.mapperL = vtk.vtkImageMapper()
        self.mapperL.SetInputConnection(self.reader.GetOutputPort())
        self.mapperR = vtk.vtkImageMapper()

        self.actorL = vtk.vtkActor2D()
        self.actorL.SetMapper(self.mapperL)
        self.actorR = vtk.vtkActor2D()
        self.actorR.SetMapper(self.mapperR)

        self.renL.AddActor2D(self.actorL)
        self.renR.AddActor2D(self.actorR)

        self.importer = vtk.vtkImageImport()
        self.mapperR.SetInputConnection(self.importer.GetOutputPort())

        self.loadImage(os.path.join(STARTINGPATH, FILENAME))
        self.setWindowingAlg()

    def loadImage(self, imagePath):
        self.reader.SetFileName(imagePath)
        self.reader.SetUpdateExtentToWholeExtent()
        self.reader.Update()

        _extent = self.reader.GetDataExtent()
        ConstPixelDims = [_extent[1]-_extent[0]+1, _extent[3]-_extent[2]+1, _extent[5]-_extent[4]+1]

        imageData = self.reader.GetOutput()
        pointData = imageData.GetPointData()
        arrayData = pointData.GetArray(0)
        dataType = arrayData.GetDataType()

        NumPy_data = numpy_support.vtk_to_numpy(arrayData)

        NumPy_data = NumPy_data.reshape(ConstPixelDims, order='C')
        NumPy_data = NumPy_data.astype('short')

        NumPy_data_shape = NumPy_data.shape
        VTK_data = numpy_support.numpy_to_vtk(num_array=NumPy_data.ravel(), deep=True, array_type=dataType)

        self.importer.CopyImportVoidPointer(VTK_data, NumPy_data.nbytes)
        self.importer.SetWholeExtent(_extent[0], _extent[1], _extent[2], _extent[3], _extent[4], _extent[5])
        self.importer.SetDataExtentToWholeExtent()
        self.importer.SetDataScalarType(dataType)

        tabI = self.ui.tabWidget.currentIndex()
        self.on_tabWidget_currentChanged(tabI)

        self.ui.leftVtk.GetRenderWindow().Render()
        self.ui.rightVtk.GetRenderWindow().Render()


    def setWindowingAlg(self):
        print('win set')
        pass


    def setCannyAlg(self):
        print('canny set')
        imageCast = vtk.vtkImageCast()
        imageCast.SetOutputScalarTypeToFloat()
        imageCast.SetInputData(self.reader.GetOutput())
        imageCast.Update()

        cannyImgType = itk.Image[itk.F, 2]
        vtk2itk = itk.VTKImageToImageFilter[cannyImgType].New(imageCast.GetOutput())

        canny = itk.CannyEdgeDetectionImageFilter[cannyImgType, cannyImgType].New(vtk2itk)

        outImgType = itk.Image[itk.SS, 2]
        rescaler = itk.RescaleIntensityImageFilter[cannyImgType, outImgType].New(canny)

        itk2vtk = itk.ImageToVTKImageFilter[outImgType].New(rescaler)
        itk2vtk.Update()

        self.mapperR.SetInputData(itk2vtk.GetOutput())
        self.ui.leftVtk.GetRenderWindow().Render()
        self.ui.rightVtk.GetRenderWindow().Render()


    def algoUpdate(self):
        pass

    @QtCore.pyqtSlot(int)
    def on_tabWidget_currentChanged(self, tabIndex):
        algs = [self.setWindowingAlg, self.setCannyAlg]
        algs[tabIndex]()

    @QtCore.pyqtSlot()
    def on_loadImage_clicked(self):
            imagePath = QtGui.QFileDialog.getOpenFileName(None, 'Wybierz obraz:', STARTINGPATH, str("Image Files (*.dcm)"))
            imagePath = str(imagePath)
            if imagePath:
                self.loadImage(imagePath)
            else:
                pass


if __name__ == "__main__":

    logWin = vtk.vtkWin32OutputWindow()
    logWin.SendToStdErrOn()
   # logWin.SetGlobalWarningDisplay(0)

    app = QtGui.QApplication(sys.argv)
    window = MIEnhancer()
    window.show()
    exit_code = app.exec_()
    del window
    sys.exit(exit_code)

#QtGui.QApplication.quit()