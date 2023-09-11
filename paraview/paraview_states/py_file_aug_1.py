# state file generated using paraview version 5.11.1
from paraview.simple import *
import paraview

from topologytoolkit import (
    ttkMorseSmaleComplex,
    ttkPersistenceCurve,
    ttkPersistenceDiagram,
    ttkTopologicalSimplification,
)


paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [502, 174]
lineChartView1.LegendPosition = [560, 316]
lineChartView1.LeftAxisUseCustomRange = 1
lineChartView1.LeftAxisRangeMinimum = -2.4390244483947754
lineChartView1.LeftAxisRangeMaximum = 197.56097555160522
lineChartView1.BottomAxisUseCustomRange = 1
lineChartView1.BottomAxisRangeMinimum = -1.6595744639635086
lineChartView1.BottomAxisRangeMaximum = 88.34042553603649
lineChartView1.RightAxisUseCustomRange = 1
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisUseCustomRange = 1
lineChartView1.TopAxisRangeMaximum = 6.66

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [502, 173]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [92.23538970947266, 94.72978973388672, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [87.29932154148278, 86.26795858876125, 634.6895912170411]
renderView1.CameraFocalPoint = [87.29932154148278, 86.26795858876125, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 132.2161116425857
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.Visibility = 1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [502, 174]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [2.8439835, 3.342089999999999, 0.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [3.708583799166737, 3.3420899999999993, 104.57773001076086]
renderView2.CameraFocalPoint = [2.8439835, 3.3420899999999993, 0.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 27.06763323876265
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [502, 173]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.CenterOfRotation = [2.8439835, 3.342089999999999, 0.0]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [1.1148419959484839, 3.3420899999999993, 104.56700826522616]
renderView3.CameraFocalPoint = [2.8439835, 3.3420899999999993, 0.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 27.06763323876265
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView3.AxesGrid.Visibility = 1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.500000)
layout1.SplitVertical(1, 0.500000)
layout1.AssignView(3, lineChartView1)
layout1.AssignView(4, renderView1)
layout1.SplitVertical(2, 0.500000)
layout1.AssignView(5, renderView2)
layout1.AssignView(6, renderView3)
layout1.SetSize(1005, 348)

# ----------------------------------------------------------------
# restore active view
SetActiveView(lineChartView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
data_sorted_label_enc_outcsv = CSVReader(registrationName='data_sorted_label_enc_out.csv', FileName=['G:\\My Drive\\UALR\\GA\\GA\\Repository\\paraview\\umap\\data_sorted_label_enc_out.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(registrationName='TableToPoints1', Input=data_sorted_label_enc_outcsv)
tableToPoints1.XColumn = 'UMAP-0'
tableToPoints1.YColumn = 'UMAP-1'
tableToPoints1.ZColumn = 'UMAP-1'
tableToPoints1.a2DPoints = 1
tableToPoints1.KeepAllDataArrays = 1

# create a new 'Gaussian Resampling'
gaussianResampling3 = GaussianResampling(registrationName='GaussianResampling3', Input=tableToPoints1)
gaussianResampling3.ResampleField = ['POINTS', 'ignore arrays']
gaussianResampling3.ResamplingGrid = [300, 300, 3]
gaussianResampling3.GaussianSplatRadius = 0.05
gaussianResampling3.SplatAccumulationMode = 'Sum'

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(registrationName='TTKPersistenceCurve1', Input=gaussianResampling3)
tTKPersistenceCurve1.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceCurve1.InputOffsetField = ['POINTS', 'SplatterValues']

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=gaussianResampling3)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'SplatterValues']

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'Persistence']
threshold1.LowerThreshold = 3.6948504433272196
threshold1.UpperThreshold = 378.91915610416487

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(registrationName='TTKTopologicalSimplification1', Domain=gaussianResampling3,
    Constraints=threshold1)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification1.InputOffsetField = ['POINTS', 'SplatterValues']
tTKTopologicalSimplification1.VertexIdentifierField = ['POINTS', 'CriticalType']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1.Descending1Separatrices = 0

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# find source
tTKPersistenceCurve1_1 = FindSource('TTKPersistenceCurve1')

# show data from tTKPersistenceCurve1_1
tTKPersistenceCurve1_1Display = Show(OutputPort(tTKPersistenceCurve1_1, 3), lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
tTKPersistenceCurve1_1Display.AttributeType = 'Row Data'
tTKPersistenceCurve1_1Display.XArrayName = 'Number Of Pairs (all pairs)'
tTKPersistenceCurve1_1Display.SeriesVisibility = ['Number Of Pairs (all pairs)', 'Persistence (all pairs)']
tTKPersistenceCurve1_1Display.SeriesLabel = ['Number Of Pairs (all pairs)', 'Number Of Pairs (all pairs)', 'Persistence (all pairs)', 'Persistence (all pairs)']
tTKPersistenceCurve1_1Display.SeriesColor = ['Number Of Pairs (all pairs)', '0', '0', '0', 'Persistence (all pairs)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
tTKPersistenceCurve1_1Display.SeriesOpacity = ['Number Of Pairs (all pairs)', '1', 'Persistence (all pairs)', '1']
tTKPersistenceCurve1_1Display.SeriesPlotCorner = ['Number Of Pairs (all pairs)', '0', 'Persistence (all pairs)', '0']
tTKPersistenceCurve1_1Display.SeriesLabelPrefix = ''
tTKPersistenceCurve1_1Display.SeriesLineStyle = ['Number Of Pairs (all pairs)', '1', 'Persistence (all pairs)', '1']
tTKPersistenceCurve1_1Display.SeriesLineThickness = ['Number Of Pairs (all pairs)', '2', 'Persistence (all pairs)', '2']
tTKPersistenceCurve1_1Display.SeriesMarkerStyle = ['Number Of Pairs (all pairs)', '0', 'Persistence (all pairs)', '0']
tTKPersistenceCurve1_1Display.SeriesMarkerSize = ['Number Of Pairs (all pairs)', '4', 'Persistence (all pairs)', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from threshold1
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'Persistence'
persistenceTF2D = GetTransferFunction2D('Persistence')

# get color transfer function/color map for 'Persistence'
persistenceLUT = GetColorTransferFunction('Persistence')
persistenceLUT.TransferFunction2D = persistenceTF2D
persistenceLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 189.45957805208243, 0.865003, 0.865003, 0.865003, 378.91915610416487, 0.705882, 0.0156863, 0.14902]
persistenceLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Persistence'
persistencePWF = GetOpacityTransferFunction('Persistence')
persistencePWF.Points = [0.0, 0.0, 0.5, 0.0, 378.91915610416487, 1.0, 0.5, 0.0]
persistencePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['CELLS', 'Persistence']
threshold1Display.LookupTable = persistenceLUT
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleArray = 'Coordinates'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'Coordinates'
threshold1Display.ScaleFactor = 18.945957946777344
threshold1Display.SelectScaleArray = 'Coordinates'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'Coordinates'
threshold1Display.GaussianRadius = 0.9472978973388672
threshold1Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'Coordinates']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = persistencePWF
threshold1Display.ScalarOpacityUnitDistance = 37.77603189788163
threshold1Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold1Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [-16.322965621948242, 0.0, 0.5, 0.0, 21.882722854614258, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [-16.322965621948242, 0.0, 0.5, 0.0, 21.882722854614258, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for persistenceLUT in view renderView1
persistenceLUTColorBar = GetScalarBar(persistenceLUT, renderView1)
persistenceLUTColorBar.Title = 'Persistence'
persistenceLUTColorBar.ComponentTitle = ''

# set color bar visibility
persistenceLUTColorBar.Visibility = 1

# show color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from gaussianResampling3
gaussianResampling3Display = Show(gaussianResampling3, renderView2, 'UniformGridRepresentation')

# get 2D transfer function for 'Separate_278193_SplatterValues'
separate_278193_SplatterValuesTF2D = GetTransferFunction2D('Separate_278193_SplatterValues')
separate_278193_SplatterValuesTF2D.ScalarRangeInitialized = 1
separate_278193_SplatterValuesTF2D.Range = [0.0, 189.45957805208243, 0.0, 1.0]

# get separate color transfer function/color map for 'SplatterValues'
separate_gaussianResampling3Display_SplatterValuesLUT = GetColorTransferFunction('SplatterValues', gaussianResampling3Display, separate=True)
separate_gaussianResampling3Display_SplatterValuesLUT.TransferFunction2D = separate_278193_SplatterValuesTF2D
separate_gaussianResampling3Display_SplatterValuesLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 94.72978902604122, 0.865003, 0.865003, 0.865003, 189.45957805208243, 0.705882, 0.0156863, 0.14902]
separate_gaussianResampling3Display_SplatterValuesLUT.ScalarRangeInitialized = 1.0

# get separate opacity transfer function/opacity map for 'SplatterValues'
separate_gaussianResampling3Display_SplatterValuesPWF = GetOpacityTransferFunction('SplatterValues', gaussianResampling3Display, separate=True)
separate_gaussianResampling3Display_SplatterValuesPWF.Points = [0.0, 0.0, 0.5, 0.0, 189.45957805208243, 1.0, 0.5, 0.0]
separate_gaussianResampling3Display_SplatterValuesPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
gaussianResampling3Display.Representation = 'Slice'
gaussianResampling3Display.ColorArrayName = ['POINTS', 'SplatterValues']
gaussianResampling3Display.LookupTable = separate_gaussianResampling3Display_SplatterValuesLUT
gaussianResampling3Display.SelectTCoordArray = 'None'
gaussianResampling3Display.SelectNormalArray = 'None'
gaussianResampling3Display.SelectTangentArray = 'None'
gaussianResampling3Display.OSPRayScaleArray = 'SplatterValues'
gaussianResampling3Display.OSPRayScaleFunction = 'PiecewiseFunction'
gaussianResampling3Display.SelectOrientationVectors = 'None'
gaussianResampling3Display.ScaleFactor = 4.18187964
gaussianResampling3Display.SelectScaleArray = 'SplatterValues'
gaussianResampling3Display.GlyphType = 'Arrow'
gaussianResampling3Display.GlyphTableIndexArray = 'SplatterValues'
gaussianResampling3Display.GaussianRadius = 0.20909398199999998
gaussianResampling3Display.SetScaleArray = ['POINTS', 'SplatterValues']
gaussianResampling3Display.ScaleTransferFunction = 'PiecewiseFunction'
gaussianResampling3Display.OpacityArray = ['POINTS', 'SplatterValues']
gaussianResampling3Display.OpacityTransferFunction = 'PiecewiseFunction'
gaussianResampling3Display.DataAxesGrid = 'GridAxesRepresentation'
gaussianResampling3Display.PolarAxes = 'PolarAxesRepresentation'
gaussianResampling3Display.ScalarOpacityUnitDistance = 1.2137442395384574
gaussianResampling3Display.ScalarOpacityFunction = separate_gaussianResampling3Display_SplatterValuesPWF
gaussianResampling3Display.TransferFunction2D = separate_278193_SplatterValuesTF2D
gaussianResampling3Display.OpacityArrayName = ['POINTS', 'SplatterValues']
gaussianResampling3Display.ColorArray2Name = ['POINTS', 'SplatterValues']
gaussianResampling3Display.IsosurfaceValues = [1.4931196064547703]
gaussianResampling3Display.SliceFunction = 'Plane'
gaussianResampling3Display.Slice = 1
gaussianResampling3Display.SelectInputVectors = [None, '']
gaussianResampling3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
gaussianResampling3Display.ScaleTransferFunction.Points = [-0.006803636153742871, 0.0, 0.5, 0.0, 2.993042849063283, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
gaussianResampling3Display.OpacityTransferFunction.Points = [-0.006803636153742871, 0.0, 0.5, 0.0, 2.993042849063283, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
gaussianResampling3Display.SliceFunction.Origin = [2.8439835, 3.342089999999999, 0.0]

# set separate color map
gaussianResampling3Display.UseSeparateColorMap = True

# setup the color legend parameters for each legend in this view

# get color legend/bar for separate_gaussianResampling3Display_SplatterValuesLUT in view renderView2
separate_gaussianResampling3Display_SplatterValuesLUTColorBar = GetScalarBar(separate_gaussianResampling3Display_SplatterValuesLUT, renderView2)
separate_gaussianResampling3Display_SplatterValuesLUTColorBar.Title = 'SplatterValues'
separate_gaussianResampling3Display_SplatterValuesLUTColorBar.ComponentTitle = ''

# set color bar visibility
separate_gaussianResampling3Display_SplatterValuesLUTColorBar.Visibility = 1

# show color legend
gaussianResampling3Display.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_1
tTKMorseSmaleComplex1_1Display = Show(OutputPort(tTKMorseSmaleComplex1_1, 3), renderView3, 'UniformGridRepresentation')

# get 2D transfer function for 'AscendingManifold'
ascendingManifoldTF2D = GetTransferFunction2D('AscendingManifold')
ascendingManifoldTF2D.ScalarRangeInitialized = 1
ascendingManifoldTF2D.Range = [-1.0, 6.0, 0.0, 1.0]

# get color transfer function/color map for 'AscendingManifold'
ascendingManifoldLUT = GetColorTransferFunction('AscendingManifold')
ascendingManifoldLUT.TransferFunction2D = ascendingManifoldTF2D
ascendingManifoldLUT.RGBPoints = [-1.0, 0.231373, 0.298039, 0.752941, 6.0, 0.865003, 0.865003, 0.865003, 13.0, 0.705882, 0.0156863, 0.14902]
ascendingManifoldLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'AscendingManifold'
ascendingManifoldPWF = GetOpacityTransferFunction('AscendingManifold')
ascendingManifoldPWF.Points = [-1.0, 0.0, 0.5, 0.0, 13.0, 1.0, 0.5, 0.0]
ascendingManifoldPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKMorseSmaleComplex1_1Display.Representation = 'Slice'
tTKMorseSmaleComplex1_1Display.ColorArrayName = ['POINTS', 'AscendingManifold']
tTKMorseSmaleComplex1_1Display.LookupTable = ascendingManifoldLUT
tTKMorseSmaleComplex1_1Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1_1Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1_1Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1_1Display.OSPRayScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1_1Display.ScaleFactor = 3.83338967
tTKMorseSmaleComplex1_1Display.SelectScaleArray = 'SplatterValues'
tTKMorseSmaleComplex1_1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1_1Display.GlyphTableIndexArray = 'SplatterValues'
tTKMorseSmaleComplex1_1Display.GaussianRadius = 0.1916694835
tTKMorseSmaleComplex1_1Display.SetScaleArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_1Display.OpacityArray = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1_1Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1_1Display.ScalarOpacityUnitDistance = 0.9629139699042034
tTKMorseSmaleComplex1_1Display.ScalarOpacityFunction = ascendingManifoldPWF
tTKMorseSmaleComplex1_1Display.TransferFunction2D = ascendingManifoldTF2D
tTKMorseSmaleComplex1_1Display.OpacityArrayName = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1_1Display.ColorArray2Name = ['POINTS', 'SplatterValues']
tTKMorseSmaleComplex1_1Display.IsosurfaceValues = [94.72978902604122]
tTKMorseSmaleComplex1_1Display.SliceFunction = 'Plane'
tTKMorseSmaleComplex1_1Display.Slice = 1
tTKMorseSmaleComplex1_1Display.SelectInputVectors = [None, '']
tTKMorseSmaleComplex1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 189.45957805208243, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 189.45957805208243, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
tTKMorseSmaleComplex1_1Display.SliceFunction.Origin = [2.8439835, 3.342089999999999, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for ascendingManifoldLUT in view renderView3
ascendingManifoldLUTColorBar = GetScalarBar(ascendingManifoldLUT, renderView3)
ascendingManifoldLUTColorBar.Title = 'AscendingManifold'
ascendingManifoldLUTColorBar.ComponentTitle = ''

# set color bar visibility
ascendingManifoldLUTColorBar.Visibility = 1

# show color legend
tTKMorseSmaleComplex1_1Display.SetScalarBarVisibility(renderView3, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')

import pandas as pd
import numpy as np

data = pd.read_csv(r"G:\My Drive\UALR\GA\GA\Repository\paraview\umap\data_sorted_label_enc_out.csv")

data

c = 0
d = 299
a = -14.0995
b = 24.0164

u_0_trx = c+(((d-c)/(b-a))*(data['UMAP-0']-a))

data['u_0_trx'] = u_0_trx

c = 0
d = 299
a = -14.8735
b = 23.5025

u_1_trx = c+(((d-c)/(b-a))*(data['UMAP-1']-a))
u_1_trx

data['u_1_trx'] = u_1_trx
data

morse_smalle_df = pd.read_csv(r"G:\My Drive\UALR\GA\GA\Repository\paraview\paraview_states\morse_smale-complex.csv")



data['u_0_trx'] = data['u_0_trx'].apply(np.floor)

data['u_1_trx'] = data['u_1_trx'].apply(np.floor)

result = pd.DataFrame(columns=['Point ID',	'Structured Coordinates:0',	'Structured Coordinates:1','Structured Coordinates:2',	'AscendingManifold',	'DescendingManifold',	'MorseSmaleManifold',	'SplatterValues',	'SplatterValues_Order'])
for row in data.itertuples():
   column1_value = row.u_0_trx
   column2_value = row.u_1_trx
   result = result.append(morse_smalle_df[(morse_smalle_df['Structured Coordinates:0'] == column1_value) & (morse_smalle_df['Structured Coordinates:1'] == column2_value) & (morse_smalle_df['Structured Coordinates:2'] == 1)],ignore_index=True)
# result.to_csv('filename.CSV', index=False)
  #  result.append(morse_smalle_df[(morse_smalle_df['Structured Coordinates:0'] == column1_value) & (morse_smalle_df['Structured Coordinates:1'] == column2_value)],ignore_index=True)
print(result)

data['AscendingManifold'] = result['AscendingManifold']
data['MorseSmaleManifold'] = result['MorseSmaleManifold']
