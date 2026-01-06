# -*- coding: mbcs -*-
# TPU (Ø18×14) vs Nylon (Ø78×35): Approach(1s) -> Load(1s) -> Spin(3s @ 145 rpm, dynamic)
# 30 N ramps during Approach and remains ON for Load + Spin.
# Spin uses Dynamic, implicit for real-time feel. Many small increments for smooth animation.

from abaqus import *
from abaqusConstants import *
import regionToolset, mesh, math

# -------- Settings --------
DENSITY_IN_G_PER_CM3 = True
job_name   = 'RigidCylinders_LoadSpin_2z4s_F5_mu0z50_dyn'
model_name = 'RigidCylinders_LoadSpin_2z4s_F5_mu0z50_dyn'
MU   = 0.50
RPM  = 145.0
OMEGA = RPM * 2.0*math.pi/60.0     # rad/s

# Geometry
tpu_r, tpu_h = 9.0, 14.0
nyl_r, nyl_h = 39.0, 35.0

# Materials (given)
tpu_density_in, tpu_E, tpu_nu = 1.20, 25.0, 0.49
nyl_density_in, nyl_E, nyl_nu = 1.15, 2500.0, 0.35

# Mesh sizes
tpu_seed, nyl_seed = 0.75, 1.2

# ---- Densities -> tonne/mm^3 ----
if DENSITY_IN_G_PER_CM3:
    tpu_rho = tpu_density_in * 1.0e-9
    nyl_rho = nyl_density_in * 1.0e-9
else:
    tpu_rho = tpu_density_in * 1.0e-12
    nyl_rho = nyl_density_in * 1.0e-12

# Fresh model
if model_name in mdb.models: del mdb.models[model_name]
M = mdb.Model(name=model_name)

# Materials & sections
mat_tpu = M.Material(name='TPU');   mat_tpu.Density(table=((tpu_rho,),));   mat_tpu.Elastic(table=((tpu_E, tpu_nu),))
mat_ny  = M.Material(name='Nylon'); mat_ny.Density(table=((nyl_rho,),));    mat_ny.Elastic(table=((nyl_E, nyl_nu),))
M.HomogeneousSolidSection(name='TPU_SEC',  material='TPU')
M.HomogeneousSolidSection(name='NYLON_SEC', material='Nylon')

# Parts
def make_cyl(model, name, r, h, sec):
    sk = model.ConstrainedSketch(name=name+'_SK', sheetSize=200.0)
    sk.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(r, 0.0))
    p = model.Part(name=name, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p.BaseSolidExtrude(sketch=sk, depth=h)
    p.Set(name=name+'_ALL', cells=p.cells)
    p.SectionAssignment(region=p.sets[name+'_ALL'], sectionName=sec)
    return p

p_tpu = make_cyl(M, 'TPU_Cyl',   tpu_r, tpu_h, 'TPU_SEC')
p_nyl = make_cyl(M, 'Nylon_Cyl', nyl_r, nyl_h, 'NYLON_SEC')

# RPs on PARTS
rp_tpu = p_tpu.ReferencePoint(point=(0.0, 0.0, tpu_h))
rp_nyl = p_nyl.ReferencePoint(point=(0.0, 0.0, nyl_h))
p_tpu.Set(name='TPU_RP',   referencePoints=(p_tpu.referencePoints[rp_tpu.id],))
p_nyl.Set(name='NYLON_RP', referencePoints=(p_nyl.referencePoints[rp_nyl.id],))

# Assembly & placement
a = M.rootAssembly; a.DatumCsysByDefault(CARTESIAN)
inst_nyl = a.Instance(name='Nylon_Cyl-1', part=p_nyl, dependent=ON)
inst_tpu = a.Instance(name='TPU_Cyl-1',   part=p_tpu, dependent=ON)

# Place TPU so bottom is 5 mm above Nylon top: Nylon top z=35 -> TPU bottom at z=40
a.translate(instanceList=('TPU_Cyl-1',),
            vector=(20.0, 0.0, (nyl_h + 5.0 + 0.5*tpu_h) - 0.5*tpu_h))

# Rigid bodies ON ASSEMBLY INSTANCES
rb_ref_tpu = regionToolset.Region(referencePoints=(inst_tpu.referencePoints[rp_tpu.id],))
rb_bdy_tpu = regionToolset.Region(cells=inst_tpu.cells)
rb_ref_nyl = regionToolset.Region(referencePoints=(inst_nyl.referencePoints[rp_nyl.id],))
rb_bdy_nyl = regionToolset.Region(cells=inst_nyl.cells)
M.RigidBody(name='RB_TPU',   refPointRegion=rb_ref_tpu,   bodyRegion=rb_bdy_tpu)
M.RigidBody(name='RB_NYLON', refPointRegion=rb_ref_nyl,   bodyRegion=rb_bdy_nyl)

# CONTACT: pick faces by assembly-space bounding boxes
eps = 1e-6
tpb = inst_tpu.faces.getByBoundingBox(20.0 - tpu_r - eps, -tpu_r - eps, 40.0 - eps,
                                      20.0 + tpu_r + eps,  tpu_r + eps, 40.0 + eps)
nyt = inst_nyl.faces.getByBoundingBox(-nyl_r - eps, -nyl_r - eps, 35.0 - eps,
                                       nyl_r + eps,  nyl_r + eps, 35.0 + eps)
if len(tpb)==0 or len(nyt)==0:
    raise RuntimeError('Contact faces not found. Check placement.')

secondaryRegion = regionToolset.Region(side1Faces=tpb)   # TPU bottom
mainRegion      = regionToolset.Region(side1Faces=nyt)   # Nylon top

prop = M.ContactProperty('TPU_NYLON_Fric')
prop.TangentialBehavior(formulation=PENALTY, directionality=ISOTROPIC,
                        maximumElasticSlip=FRACTION, fraction=0.01,
                        table=((MU,),))
prop.NormalBehavior(pressureOverclosure=HARD)

# API variant: main/secondary
M.SurfaceToSurfaceContactStd(name='INT_TPU_NYLON',
    createStepName='Initial',
    main=mainRegion, secondary=secondaryRegion,
    sliding=FINITE, thickness=ON,
    interactionProperty='TPU_NYLON_Fric',
    adjustMethod=NONE)

# -------- Steps (total = 2.4 s) --------
# Static steps with small increments for smooth motion
M.StaticStep(name='Approach', previous='Initial', timePeriod=0.5, nlgeom=ON,
             initialInc=0.08, minInc=1e-06, maxInc=0.2, maxNumInc=2000)
M.StaticStep(name='Load',     previous='Approach', timePeriod=0.5, nlgeom=ON,
             initialInc=0.1, minInc=1e-06, maxInc=0.5, maxNumInc=2000)

# Dynamic, implicit spin for real-time feel (1.4 s)
M.ImplicitDynamicsStep(name='Spin', previous='Load', timePeriod=1.4, nlgeom=ON,
                       application=QUASI_STATIC, initialInc=0.002, minInc=1e-06,
                       maxInc=0.01, maxNumInc=10000, alpha=0.0)

# Amplitudes
# 30 N ramps 0->30 N during the 0.5s Approach (TOTAL time), then holds
M.SmoothStepAmplitude(name='P_RAMP',    timeSpan=TOTAL, data=((0.0,0.0),(1.0,1.0)))
# Spin ramp within Spin step (0->1 over 1.4 s)
M.SmoothStepAmplitude(name='SPIN_RAMP', timeSpan=STEP,  data=((0.0,0.0),(1.0,1.0)))

# -------- BCs & Loads --------
M.DisplacementBC(name='BC_FIX_NYLON', createStepName='Initial',
                 region=inst_nyl.sets['NYLON_RP'], u1=0.0, u2=0.0, u3=0.0)  # rotations free
M.DisplacementBC(name='BC_HOLD_TPU_INIT', createStepName='Initial',
                 region=inst_tpu.sets['TPU_RP'], u1=0.0, u2=0.0, ur1=0.0, ur2=0.0, ur3=0.0)

# Approach: EXACT 5 mm down
M.DisplacementBC(name='BC_TPU_DOWN', createStepName='Approach',
                 region=inst_tpu.sets['TPU_RP'], u3=-5.0)

# 5 N starts in Approach with P_RAMP and persists automatically
M.ConcentratedForce(name='P_30N', createStepName='Approach',
                    region=inst_tpu.sets['TPU_RP'], cf3=-5.0, amplitude='P_RAMP')

# Spin: angular velocity about Z for 3.0 s (ramped over the Spin step)
M.VelocityBC(name='SPIN_NYLON', createStepName='Spin',
             region=inst_nyl.sets['NYLON_RP'], vr3=OMEGA, amplitude='SPIN_RAMP')

# -------- Mesh (free tet C3D4) --------
p_tpu.seedPart(size=tpu_seed, deviationFactor=0.1, minSizeFactor=0.1)
p_tpu.setElementType(regions=(p_tpu.cells,),
                     elemTypes=(mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD),))
p_tpu.generateMesh()
p_nyl.seedPart(size=nyl_seed, deviationFactor=0.1, minSizeFactor=0.1)
p_nyl.setElementType(regions=(p_nyl.cells,),
                     elemTypes=(mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD),))
p_nyl.generateMesh()
a.regenerate()

# -------- Output density (more frames) --------
# Bump default field output to give you smoother animation
for name in ('F_App', 'F_Load', 'F_Spin'):
    if name in M.fieldOutputRequests:
        del M.fieldOutputRequests[name]

# Approach: coarse (fast motion, few frames)
M.FieldOutputRequest(
    name='F_App',
    createStepName='Approach',
    variables=PRESELECT,
    numIntervals=20
)

# Load: medium
M.FieldOutputRequest(
    name='F_Load',
    createStepName='Load',
    variables=PRESELECT,
    numIntervals=20
)

# Spin: fine (smooth animation)
M.FieldOutputRequest(
    name='F_Spin',
    createStepName='Spin',
    variables=PRESELECT,
    numIntervals=200
)
# -------- Job (build only) --------
if job_name in mdb.jobs: del mdb.jobs[job_name]
mdb.Job(name=job_name, model=model_name)

print('Built. Total time = 5.0 s (Approach 1s, Load 1s, Spin 3s dynamic).')
print('Spin uses Dynamic, implicit with many small increments for real-time animation.')
print('Job "%s" created (not submitted). Submit from Job Manager.' % job_name)
