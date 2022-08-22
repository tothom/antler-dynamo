# Enable Python support and load DesignScript library
import clr

# Import RevitAPI
clr.AddReference("RevitAPI")
from Autodesk.Revit import DB

# Import ToDSType(bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)


# Import DocumentManager and TransactionManager
clr.AddReference ("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument


#The inputs to this node will be stored as a list in the IN variable.
elements = IN[0]

def valid_solid_filter(geometry_object):
	if isinstance(geometry_object, DB.Solid) and\
		geometry_object.Faces.Size > 0 and\
		geometry_object.Edges.Size > 0 and\
		geometry_object.Volume > 0:
		return True
	else:
		return False



def get_solids(element):
	solids = []

	options = DB.Options()

	geometry_element = element.get_Geometry(options)

	for geometry_object in geometry_element:
		geometry_instance = clr.Convert(geometry_object, DB.GeometryInstance)

		if geometry_instance:
			instance_geometry = geometry_instance.GetInstanceGeometry()

			for geometry in instance_geometry:

			    if valid_solid_filter(geometry):
			    	solids.append(solid)

	return solids


"""
class sub_transaction():
	def __init__(self, doc):
		self.doc = doc
		self._st = DB.SubTransaction(self.doc)
"""
# Start Transaction
#TransactionManager.Instance.EnsureInTransaction(doc)

# Transaction

# End Transaction
#TransactionManager.Instance.TransactionTaskDone()

def function(element):
	#st = DB.SubTransaction(doc)

	try:
		#st.Start()
		element = UnwrapElement(element)

		solids = get_solids(element)

	except:
		pass
	else:
		return solids
	finally:
		#st.RollBack()
		#st.Dispose()



def process(item):
	if isinstance(item, (list, tuple)):
		return [process(a) for a in item]
	else:
		return function(item)

OUT = process(elements)
