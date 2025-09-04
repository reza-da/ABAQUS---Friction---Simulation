# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.Model(name='Spin_Approach_2mm')
mdb.models['Spin_Approach_2mm'].ConstrainedSketch(name='__big__', sheetSize=
    0.2)
mdb.models['Spin_Approach_2mm'].sketches['__big__'].ConstructionLine(point1=(
    0.0, -0.1), point2=(0.0, 0.1))
mdb.models['Spin_Approach_2mm'].sketches['__big__'].CircleByCenterPerimeter(
    center=(0.0, 0.0), point1=(0.039, 0.0))
mdb.models['Spin_Approach_2mm'].Part(dimensionality=THREE_D, name='BigCylinder'
    , type=DEFORMABLE_BODY)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].BaseSolidExtrude(depth=
    0.035, sketch=mdb.models['Spin_Approach_2mm'].sketches['__big__'])
del mdb.models['Spin_Approach_2mm'].sketches['__big__']
mdb.models['Spin_Approach_2mm'].ConstrainedSketch(name='__small__', sheetSize=
    0.2)
mdb.models['Spin_Approach_2mm'].sketches['__small__'].ConstructionLine(point1=(
    0.0, -0.1), point2=(0.0, 0.1))
mdb.models['Spin_Approach_2mm'].sketches['__small__'].CircleByCenterPerimeter(
    center=(0.0, 0.0), point1=(0.009, 0.0))
mdb.models['Spin_Approach_2mm'].Part(dimensionality=THREE_D, name=
    'SmallCylinder', type=DEFORMABLE_BODY)
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].BaseSolidExtrude(depth=
    0.014, sketch=mdb.models['Spin_Approach_2mm'].sketches['__small__'])
del mdb.models['Spin_Approach_2mm'].sketches['__small__']
mdb.models['Spin_Approach_2mm'].Material(name='Nylon')
mdb.models['Spin_Approach_2mm'].materials['Nylon'].Density(table=((1150.0, ), 
    ))
mdb.models['Spin_Approach_2mm'].materials['Nylon'].Elastic(table=((
    2800000000.0, 0.39), ))
mdb.models['Spin_Approach_2mm'].Material(name='TPU')
mdb.models['Spin_Approach_2mm'].materials['TPU'].Density(table=((1200.0, ), ))
mdb.models['Spin_Approach_2mm'].materials['TPU'].Elastic(table=((30000000.0, 
    0.45), ))
mdb.models['Spin_Approach_2mm'].HomogeneousSolidSection(material='Nylon', name=
    'NylonSection')
mdb.models['Spin_Approach_2mm'].HomogeneousSolidSection(material='TPU', name=
    'TPUSection')
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].SectionAssignment(region=
    Region(
    cells=mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].cells.getSequenceFromMask(
    mask=('[#1 ]', ), )), sectionName='NylonSection')
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].SectionAssignment(
    region=Region(
    cells=mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].cells.getSequenceFromMask(
    mask=('[#1 ]', ), )), sectionName='TPUSection')
mdb.models['Spin_Approach_2mm'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Spin_Approach_2mm'].rootAssembly.Instance(dependent=ON, name=
    'BigCylinder-1', part=mdb.models['Spin_Approach_2mm'].parts['BigCylinder'])
mdb.models['Spin_Approach_2mm'].rootAssembly.Instance(dependent=ON, name=
    'SmallCylinder-1', part=
    mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'])
mdb.models['Spin_Approach_2mm'].rootAssembly.translate(instanceList=(
    'SmallCylinder-1', ), vector=(0.02, 0.0, 0.037))
mdb.models['Spin_Approach_2mm'].rootAssembly.ReferencePoint(point=(0.0, 0.0, 
    0.0175))
mdb.models['Spin_Approach_2mm'].RigidBody(bodyRegion=Region(
    cells=mdb.models['Spin_Approach_2mm'].rootAssembly.instances['BigCylinder-1'].cells.getSequenceFromMask(
    mask=('[#1 ]', ), )), name='RB-Nylon', refPointRegion=Region(
    referencePoints=(
    mdb.models['Spin_Approach_2mm'].rootAssembly.referencePoints[6], )))
mdb.models['Spin_Approach_2mm'].ImplicitDynamicsStep(initialInc=0.01, 
    maxNumInc=1000, name='Approach', nlgeom=ON, previous='Initial', timePeriod=
    0.2)
mdb.models['Spin_Approach_2mm'].ImplicitDynamicsStep(initialInc=0.01, 
    maxNumInc=1000, name='SpinStep', nlgeom=ON, previous='Initial', timePeriod=
    1.0)
mdb.models['Spin_Approach_2mm'].VelocityBC(createStepName='Initial', name=
    'FixRP', region=Region(referencePoints=(
    mdb.models['Spin_Approach_2mm'].rootAssembly.referencePoints[6], )), v1=0.0
    , v2=0.0, v3=0.0, vr1=0.0, vr2=0.0, vr3=UNSET)
mdb.models['Spin_Approach_2mm'].VelocityBC(createStepName='SpinStep', name=
    'Spin', region=Region(referencePoints=(
    mdb.models['Spin_Approach_2mm'].rootAssembly.referencePoints[6], )), v1=0.0
    , v2=0.0, v3=0.0, vr1=0.0, vr2=0.0, vr3=-15.1843644923507)
mdb.models['Spin_Approach_2mm'].rootAssembly.Surface(name='TPU_Top_Surf', 
    side1Faces=
    mdb.models['Spin_Approach_2mm'].rootAssembly.instances['SmallCylinder-1'].faces.getSequenceFromMask(
    mask=('[#2 ]', ), ))
mdb.models['Spin_Approach_2mm'].rootAssembly.ReferencePoint(point=(0.02, 0.0, 
    0.051))
mdb.models['Spin_Approach_2mm'].Coupling(controlPoint=Region(referencePoints=(
    mdb.models['Spin_Approach_2mm'].rootAssembly.referencePoints[12], )), 
    couplingType=DISTRIBUTING, influenceRadius=WHOLE_SURFACE, name=
    'TPU_Top_Coupling', surface=
    mdb.models['Spin_Approach_2mm'].rootAssembly.surfaces['TPU_Top_Surf'], u1=
    ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, weightingMethod=UNIFORM)
mdb.models['Spin_Approach_2mm'].DisplacementBC(createStepName='Initial', name=
    'BC_TPU_Fix_XY_Rots', region=Region(referencePoints=(
    mdb.models['Spin_Approach_2mm'].rootAssembly.referencePoints[12], )), u1=
    0.0, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0)
mdb.models['Spin_Approach_2mm'].DisplacementBC(createStepName='Approach', name=
    'BC_TPU_MoveDown', region=Region(referencePoints=(
    mdb.models['Spin_Approach_2mm'].rootAssembly.referencePoints[12], )), u1=
    UNSET, u2=UNSET, u3=-0.002, ur1=UNSET, ur2=UNSET, ur3=UNSET)
mdb.models['Spin_Approach_2mm'].boundaryConditions['BC_TPU_MoveDown'].deactivate(
    'SpinStep')
mdb.models['Spin_Approach_2mm'].ContactProperty('Friction_mu015')
mdb.models['Spin_Approach_2mm'].interactionProperties['Friction_mu015'].TangentialBehavior(
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, table=((
    0.15, ), ))
mdb.models['Spin_Approach_2mm'].interactionProperties['Friction_mu015'].NormalBehavior(
    allowSeparation=ON, pressureOverclosure=HARD)
mdb.models['Spin_Approach_2mm'].ContactStd(createStepName='Initial', name='GC')
mdb.models['Spin_Approach_2mm'].interactions['GC'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models['Spin_Approach_2mm'].interactions['GC'].contactPropertyAssignments.appendInStep(
    assignments=((GLOBAL, SELF, 'Friction_mu015'), ), stepName='Initial')
mdb.models['Spin_Approach_2mm'].ConcentratedForce(cf3=-5.0, createStepName=
    'SpinStep', name='CF_5N', region=Region(referencePoints=(
    mdb.models['Spin_Approach_2mm'].rootAssembly.referencePoints[12], )))
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.00583333333333333)
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].seedPart(
    deviationFactor=0.1, minSizeFactor=0.1, size=0.00225)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].setElementType(elemTypes=(
    ElemType(elemCode=C3D8R, elemLibrary=STANDARD), ), regions=(
    mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].cells, ))
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].setElementType(
    elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=STANDARD), ), regions=(
    mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].cells, ))
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].HistoryOutputRequest(createStepName='SpinStep', 
    name='H_RP_Torque', region=Region(referencePoints=(
    mdb.models['Spin_Approach_2mm'].rootAssembly.referencePoints[6], )), 
    variables=('RM', ))
del mdb.models['Spin_Approach_2mm'].fieldOutputRequests['F-Output-1']
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='Approach', 
    name='F_Approach_Default', variables=PRESELECT)
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='SpinStep', 
    name='F_Spin_Default', variables=PRESELECT)
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='Approach', 
    name='__tmp__', numIntervals=1, variables=('CPRESS', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='Approach', 
    name='__tmp__', numIntervals=1, variables=('CSHEAR1', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='Approach', 
    name='__tmp__', numIntervals=1, variables=('CSHEAR2', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='Approach', 
    name='__tmp__', numIntervals=1, variables=('COPEN', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='Approach', 
    name='__tmp__', numIntervals=1, variables=('CSLIP1', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='Approach', 
    name='__tmp__', numIntervals=1, variables=('CSLIP2', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='Approach', 
    name='__tmp__', numIntervals=1, variables=('CSTATUS', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='SpinStep', 
    name='__tmp__', numIntervals=1, variables=('CPRESS', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='SpinStep', 
    name='__tmp__', numIntervals=1, variables=('CSHEAR1', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='SpinStep', 
    name='__tmp__', numIntervals=1, variables=('CSHEAR2', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='SpinStep', 
    name='__tmp__', numIntervals=1, variables=('COPEN', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='SpinStep', 
    name='__tmp__', numIntervals=1, variables=('CSLIP1', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='SpinStep', 
    name='__tmp__', numIntervals=1, variables=('CSLIP2', ))
#* AbaqusNameError: invalid name
mdb.models['Spin_Approach_2mm'].FieldOutputRequest(createStepName='SpinStep', 
    name='__tmp__', numIntervals=1, variables=('CSTATUS', ))
#* AbaqusNameError: invalid name
mdb.Job(model='Spin_Approach_2mm', name='SpinJob')
mdb.jobs['SpinJob'].submit(consistencyChecking=OFF)
mdb.jobs['SpinJob']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'jobName': 'SpinJob', 'clientHost': 'LE-WSC101-11', 'handle': 0})
mdb.jobs['SpinJob']._Message(WARNING, {
    'message': 'A 3D DISTRIBUTED COUPLING DEFINITION WITH ROTATIONAL COUPLING=STRUCTURAL WILL IGNORE THE STRUCTURAL ROTATIONAL COUPLING AS ALL OF NODES IN THE CLOUD ARE FROM ELEMENTS WHICH DO NOT HAVE ALL ROTATIONAL DEGREES OF FREEDOM ACTIVE', 
    'phase': BATCHPRE_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FILE, {'file': 'C:\\temp\\SpinJob.odb', 
    'phase': BATCHPRE_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(COMPLETED, {'message': 'Analysis phase complete', 
    'phase': BATCHPRE_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob', 'clientHost': 'LE-WSC101-11', 'handle': 12652})
mdb.jobs['SpinJob']._Message(STEP, {'stepId': 1, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 0, 'frame': 0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(WARNING, {
    'message': 'THERE ARE 2 UNCONNECTED REGIONS IN THE MODEL.', 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(MEMORY_ESTIMATE, {'memory': 32.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(PHYSICAL_MEMORY, {'physical_memory': 65375.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(MINIMUM_MEMORY, {'minimum_memory': 21.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(WARNING, {
    'message': 'There is zero MOMENT everywhere in the model based on the default criterion. please check the value of the average MOMENT during the current iteration to verify that the MOMENT is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero MOMENT.', 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(WARNING, {
    'message': 'There is zero MOMENT everywhere in the model based on the default criterion. please check the value of the average MOMENT during the current iteration to verify that the MOMENT is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero MOMENT.', 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 1, 'attempts': 1, 
    'severe': 1, 'equilibrium': 5, 'iterations': 6, 'totalTime': 0.01, 
    'stepTime': 0.01, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 2, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.02, 
    'stepTime': 0.02, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 3, 'attempts': 1, 
    'severe': 0, 'equilibrium': 5, 'iterations': 5, 'totalTime': 0.03, 
    'stepTime': 0.03, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 4, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.04, 
    'stepTime': 0.04, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 5, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.05, 
    'stepTime': 0.05, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 6, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.065, 
    'stepTime': 0.065, 'timeIncrement': 0.015, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 7, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.0875, 
    'stepTime': 0.0875, 'timeIncrement': 0.0225, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 8, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.12125, 
    'stepTime': 0.12125, 'timeIncrement': 0.03375, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 9, 'attempts': 1, 
    'severe': 0, 'equilibrium': 5, 'iterations': 5, 'totalTime': 0.171875, 
    'stepTime': 0.171875, 'timeIncrement': 0.050625, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 0, 'frame': 1, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 10, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.2225, 'stepTime': 0.2225, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 11, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.273125, 'stepTime': 0.273125, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 12, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.32375, 'stepTime': 0.32375, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 13, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.374375, 'stepTime': 0.374375, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 14, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.425, 'stepTime': 0.425, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 15, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.475625, 'stepTime': 0.475625, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 16, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.52625, 'stepTime': 0.52625, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 17, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.576875, 'stepTime': 0.576875, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 18, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.6275, 'stepTime': 0.6275, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 19, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.678125, 'stepTime': 0.678125, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 0, 'frame': 2, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 20, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.72875, 'stepTime': 0.72875, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 21, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.779375, 'stepTime': 0.779375, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 22, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.83, 'stepTime': 0.83, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 23, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.880625, 'stepTime': 0.880625, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 24, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.93125, 'stepTime': 0.93125, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 25, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.981875, 'stepTime': 0.981875, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 0, 'frame': 3, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 26, 
    'attempts': 1, 'severe': 0, 'equilibrium': 4, 'iterations': 4, 
    'totalTime': 1.0, 'stepTime': 1.0, 'timeIncrement': 0.0181249999999996, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(END_STEP, {'stepId': 1, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STEP, {'stepId': 2, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 1, 'frame': 0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(MEMORY_ESTIMATE, {'memory': 33.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(PHYSICAL_MEMORY, {'physical_memory': 65375.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(MINIMUM_MEMORY, {'minimum_memory': 20.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 1, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.01, 
    'stepTime': 0.01, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 2, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.02, 
    'stepTime': 0.02, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 3, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.035, 
    'stepTime': 0.035, 'timeIncrement': 0.015, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 4, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.055, 
    'stepTime': 0.055, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 5, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.075, 
    'stepTime': 0.075, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 6, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.095, 
    'stepTime': 0.095, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 7, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.115, 
    'stepTime': 0.115, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 8, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.135, 
    'stepTime': 0.135, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 9, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.155, 
    'stepTime': 0.155, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 1, 'frame': 1, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 10, 
    'attempts': 1, 'severe': 0, 'equilibrium': 4, 'iterations': 4, 
    'totalTime': 1.175, 'stepTime': 0.175, 'timeIncrement': 0.02, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 11, 
    'attempts': 1, 'severe': 0, 'equilibrium': 3, 'iterations': 3, 
    'totalTime': 1.195, 'stepTime': 0.195, 'timeIncrement': 0.02, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 1, 'frame': 2, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 12, 
    'attempts': 1, 'severe': 2, 'equilibrium': 2, 'iterations': 4, 
    'totalTime': 1.2, 'stepTime': 0.2, 'timeIncrement': 0.00499999999999995, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(END_STEP, {'stepId': 2, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(COMPLETED, {'message': 'Analysis phase complete', 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(JOB_COMPLETED, {
    'time': 'Wed Sep  3 13:59:20 2025', 'jobName': 'SpinJob'})
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
del mdb.models['Model-1'].sketches['__profile__']
# Save by rdanesha on 2025_09_03-14.57.16; build 2025 2024_09_20-09.00.46 RELr427 198590
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].deleteMesh()
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.0001)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.009)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.0005)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].deleteMesh()
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].seedPart(
    deviationFactor=0.1, minSizeFactor=0.1, size=0.0005)
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].rootAssembly.regenerate()
mdb.jobs['SpinJob'].submit(consistencyChecking=OFF)
mdb.jobs['SpinJob']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'jobName': 'SpinJob', 'clientHost': 'LE-WSC101-11', 'handle': 0})
mdb.jobs['SpinJob']._Message(ERROR, {
    'message': 'Academic Teaching license is limited to 250000 nodes.', 
    'phase': BATCHPRE_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ERROR, {
    'message': 'ERROR DURING PART, INSTANCE AND ASSEMBLY PROCESSING', 
    'phase': BATCHPRE_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ABORTED, {
    'message': 'Analysis phase failed due to errors', 'phase': BATCHPRE_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error - Please see the  SpinJob.dat file for possible error messages if the file exists.', 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error - Please see the  SpinJob.dat file for possible error messages if the file exists.', 
    'jobName': 'SpinJob'})
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].deleteMesh()
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.001)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].deleteMesh()
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.01)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.009)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.0009)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.001)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.005)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].seedPart(deviationFactor=
    0.1, minSizeFactor=0.1, size=0.003)
mdb.models['Spin_Approach_2mm'].parts['BigCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].deleteMesh()
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].seedPart(
    deviationFactor=0.1, minSizeFactor=0.1, size=0.001)
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].seedPart(
    deviationFactor=0.1, minSizeFactor=0.1, size=0.0008)
mdb.models['Spin_Approach_2mm'].parts['SmallCylinder'].generateMesh()
mdb.models['Spin_Approach_2mm'].rootAssembly.regenerate()
mdb.jobs['SpinJob'].submit(consistencyChecking=OFF)
mdb.jobs['SpinJob']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'jobName': 'SpinJob', 'clientHost': 'LE-WSC101-11', 'handle': 0})
mdb.jobs['SpinJob']._Message(WARNING, {
    'message': 'A 3D DISTRIBUTED COUPLING DEFINITION WITH ROTATIONAL COUPLING=STRUCTURAL WILL IGNORE THE STRUCTURAL ROTATIONAL COUPLING AS ALL OF NODES IN THE CLOUD ARE FROM ELEMENTS WHICH DO NOT HAVE ALL ROTATIONAL DEGREES OF FREEDOM ACTIVE', 
    'phase': BATCHPRE_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FILE, {'file': 'C:\\temp\\SpinJob.odb', 
    'phase': BATCHPRE_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(COMPLETED, {'message': 'Analysis phase complete', 
    'phase': BATCHPRE_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob', 'clientHost': 'LE-WSC101-11', 'handle': 4008})
mdb.jobs['SpinJob']._Message(STEP, {'stepId': 1, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 0, 'frame': 0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(WARNING, {
    'message': 'THERE ARE 2 UNCONNECTED REGIONS IN THE MODEL.', 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(MEMORY_ESTIMATE, {'memory': 296.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(PHYSICAL_MEMORY, {'physical_memory': 65375.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(MINIMUM_MEMORY, {'minimum_memory': 54.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(WARNING, {
    'message': 'There is zero MOMENT everywhere in the model based on the default criterion. please check the value of the average MOMENT during the current iteration to verify that the MOMENT is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero MOMENT.', 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 1, 'attempts': 1, 
    'severe': 2, 'equilibrium': 5, 'iterations': 7, 'totalTime': 0.01, 
    'stepTime': 0.01, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 2, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.02, 
    'stepTime': 0.02, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 3, 'attempts': 1, 
    'severe': 0, 'equilibrium': 5, 'iterations': 5, 'totalTime': 0.03, 
    'stepTime': 0.03, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 4, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.04, 
    'stepTime': 0.04, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 5, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.05, 
    'stepTime': 0.05, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 6, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.065, 
    'stepTime': 0.065, 'timeIncrement': 0.015, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 7, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.0875, 
    'stepTime': 0.0875, 'timeIncrement': 0.0225, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 8, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 0.12125, 
    'stepTime': 0.12125, 'timeIncrement': 0.03375, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 9, 'attempts': 1, 
    'severe': 0, 'equilibrium': 5, 'iterations': 5, 'totalTime': 0.171875, 
    'stepTime': 0.171875, 'timeIncrement': 0.050625, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 0, 'frame': 1, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 10, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.2225, 'stepTime': 0.2225, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 11, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.273125, 'stepTime': 0.273125, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 12, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.32375, 'stepTime': 0.32375, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 13, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.374375, 'stepTime': 0.374375, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 14, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.425, 'stepTime': 0.425, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 15, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.475625, 'stepTime': 0.475625, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 16, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.52625, 'stepTime': 0.52625, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 17, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.576875, 'stepTime': 0.576875, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 18, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.6275, 'stepTime': 0.6275, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 19, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.678125, 'stepTime': 0.678125, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 0, 'frame': 2, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 20, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.72875, 'stepTime': 0.72875, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 21, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.779375, 'stepTime': 0.779375, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 22, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.83, 'stepTime': 0.83, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 23, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.880625, 'stepTime': 0.880625, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 24, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.93125, 'stepTime': 0.93125, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 25, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 0.981875, 'stepTime': 0.981875, 'timeIncrement': 0.050625, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 0, 'frame': 3, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 1, 'increment': 26, 
    'attempts': 1, 'severe': 0, 'equilibrium': 5, 'iterations': 5, 
    'totalTime': 1.0, 'stepTime': 1.0, 'timeIncrement': 0.0181249999999996, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(END_STEP, {'stepId': 1, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STEP, {'stepId': 2, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 1, 'frame': 0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(MEMORY_ESTIMATE, {'memory': 321.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(PHYSICAL_MEMORY, {'physical_memory': 65375.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(MINIMUM_MEMORY, {'minimum_memory': 57.0, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 1, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.01, 
    'stepTime': 0.01, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 2, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.02, 
    'stepTime': 0.02, 'timeIncrement': 0.01, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 3, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.035, 
    'stepTime': 0.035, 'timeIncrement': 0.015, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 4, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.055, 
    'stepTime': 0.055, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 5, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.075, 
    'stepTime': 0.075, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 6, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.095, 
    'stepTime': 0.095, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 7, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.115, 
    'stepTime': 0.115, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 8, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.135, 
    'stepTime': 0.135, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 9, 'attempts': 1, 
    'severe': 0, 'equilibrium': 4, 'iterations': 4, 'totalTime': 1.155, 
    'stepTime': 0.155, 'timeIncrement': 0.02, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 1, 'frame': 1, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 10, 
    'attempts': 1, 'severe': 0, 'equilibrium': 4, 'iterations': 4, 
    'totalTime': 1.175, 'stepTime': 0.175, 'timeIncrement': 0.02, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 11, 
    'attempts': 1, 'severe': 0, 'equilibrium': 3, 'iterations': 3, 
    'totalTime': 1.195, 'stepTime': 0.195, 'timeIncrement': 0.02, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(ODB_FRAME, {'step': 1, 'frame': 2, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(STATUS, {'step': 2, 'increment': 12, 
    'attempts': 1, 'severe': 2, 'equilibrium': 2, 'iterations': 4, 
    'totalTime': 1.2, 'stepTime': 0.2, 'timeIncrement': 0.00499999999999995, 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(END_STEP, {'stepId': 2, 'phase': STANDARD_PHASE, 
    'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(COMPLETED, {'message': 'Analysis phase complete', 
    'phase': STANDARD_PHASE, 'jobName': 'SpinJob'})
mdb.jobs['SpinJob']._Message(JOB_COMPLETED, {
    'time': 'Wed Sep  3 15:41:18 2025', 'jobName': 'SpinJob'})
# Save by rdanesha on 2025_09_03-16.45.29; build 2025 2024_09_20-09.00.46 RELr427 198590
