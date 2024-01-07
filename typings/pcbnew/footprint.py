from typing import Any, Mapping

from .kiid import KIID_PATH
from .box2i import BOX2I
from .board_item_container import BOARD_ITEM_CONTAINER


# TODO
class FOOTPRINT(BOARD_ITEM_CONTAINER):

	def GetPrivateLayers(self) -> Any:
		...

	def SetPrivateLayers(self, aLayers) -> Any:
		...

	def ClearAllNets(self) -> Any:
		...

	def FixUuids(self) -> Any:
		...

	def GetFpPadsLocalBbox(self) -> Any:
		...

	def GetBoundingHull(self) -> Any:
		...

	def GetBoundingBox(self, *args) -> BOX2I:
		...

	def Pads(self, *args) -> Any:
		...

	def GraphicalItems(self, *args) -> Any:
		...

	def Zones(self, *args) -> Any:
		...

	def Groups(self, *args) -> Any:
		...

	def HasThroughHolePads(self) -> Any:
		...

	def Models(self, *args) -> Any:
		...

	def SetOrientation(self, aNewAngle) -> Any:
		...

	def GetOrientation(self) -> Any:
		...

	def SetLayerAndFlip(self, aLayer) -> Any:
		...

	def SetOrientationDegrees(self, aOrientation) -> Any:
		...

	def GetOrientationDegrees(self) -> Any:
		...

	def GetFPID(self) -> Any:
		...

	def SetFPID(self, aFPID) -> Any:
		...

	def GetFPIDAsString(self) -> str:
		...

	def SetFPIDAsString(self, aFPID) -> Any:
		...

	def GetDescription(self) -> Any:
		...

	def SetDescription(self, aDoc) -> Any:
		...

	def GetKeywords(self) -> Any:
		...

	def SetKeywords(self, aKeywords) -> Any:
		...

	def GetPath(self) -> KIID_PATH:
		...

	def SetPath(self, aPath) -> Any:
		...

	def GetLocalSolderMaskMargin(self) -> Any:
		...

	def SetLocalSolderMaskMargin(self, aMargin) -> Any:
		...

	def SetLocalClearance(self, aClearance) -> Any:
		...

	def GetLocalClearance(self, *args) -> Any:
		...

	def GetLocalSolderPasteMargin(self) -> Any:
		...

	def SetLocalSolderPasteMargin(self, aMargin) -> Any:
		...

	def GetLocalSolderPasteMarginRatio(self) -> Any:
		...

	def SetLocalSolderPasteMarginRatio(self, aRatio) -> Any:
		...

	def SetZoneConnection(self, aType) -> Any:
		...

	def GetZoneConnection(self) -> Any:
		...

	def GetAttributes(self) -> Any:
		...

	def SetAttributes(self, aAttributes) -> Any:
		...

	def SetFlag(self, aFlag) -> Any:
		...

	def IncrementFlag(self) -> Any:
		...

	def GetFlag(self) -> Any:
		...

	def IsNetTie(self) -> bool:
		...

	def GetNetTiePadGroups(self) -> Any:
		...

	def ClearNetTiePadGroups(self) -> Any:
		...

	def AddNetTiePadGroup(self, aGroup) -> Any:
		...

	def MapPadNumbersToNetTieGroups(self) -> Any:
		...

	def GetNetTiePads(self, aPad) -> Any:
		...

	def GetLikelyAttribute(self) -> Any:
		...

	def MoveAnchorPosition(self, aMoveVector) -> Any:
		...

	def IsFlipped(self) -> bool:
		...

	def IsConflicting(self) -> bool:
		...

	def IsPlaced(self) -> bool:
		...

	def SetIsPlaced(self, isPlaced) -> Any:
		...

	def NeedsPlaced(self) -> Any:
		...

	def SetNeedsPlaced(self, needsPlaced) -> Any:
		...

	def LegacyPadsLocked(self) -> Any:
		...

	def CheckFootprintAttributes(self, aErrorHandler) -> Any:
		...

	def CheckPads(self, aErrorHandler) -> Any:
		...

	def CheckShortingPads(self, aErrorHandler) -> Any:
		...

	def CheckNetTies(self, aErrorHandler) -> Any:
		...

	def CheckNetTiePadGroups(self, aErrorHandler) -> Any:
		...

	def TransformPadsToPolySet(self, aBuffer, aLayer, aClearance, aMaxError, aErrorLoc, aSkipNPTHPadsWihNoCopper=False, aSkipPlatedPads=False, aSkipNonPlatedPads=False) -> Any:
		...

	def TransformFPShapesToPolySet(self, aBuffer, aLayer, aClearance, aError, aErrorLoc, aIncludeText=True, aIncludeShapes=True, aIncludePrivateItems=False) -> Any:
		...

	def TransformFPTextToPolySet(self, aBuffer, aLayer, aClearance, aError, aErrorLoc) -> Any:
		...

	def GetContextualTextVars(self, aVars) -> Any:
		...

	def ResolveTextVar(self, token, aDepth=0) -> Any:
		...

	def HitTestAccurate(self, aPosition, aAccuracy=0) -> Any:
		...

	def HitTest(self, *args) -> Any:
		...

	def GetReference(self) -> Any:
		...

	def SetReference(self, aReference) -> Any:
		...

	def GetReferenceAsString(self) -> Any:
		...

	def IncrementReference(self, aDelta) -> Any:
		...

	def GetValue(self) -> Any:
		...

	def SetValue(self, aValue) -> Any:
		...

	def GetValueAsString(self) -> Any:
		...

	def Value(self, *args) -> Any:
		...

	def Reference(self, *args) -> Any:
		...

	def HasProperty(self, aKey) -> Any:
		...

	def SetProperty(self, aKey, aVal) -> Any:
		...

	def IsBoardOnly(self) -> bool:
		...

	def SetBoardOnly(self, aIsBoardOnly=True) -> Any:
		...

	def IsExcludedFromPosFiles(self) -> bool:
		...

	def SetExcludedFromPosFiles(self, aExclude=True) -> Any:
		...

	def IsExcludedFromBOM(self) -> bool:
		...

	def SetExcludedFromBOM(self, aExclude=True) -> Any:
		...

	def AllowMissingCourtyard(self) -> Any:
		...

	def SetAllowMissingCourtyard(self, aAllow=True) -> Any:
		...

	def SetFileFormatVersionAtLoad(self, aVersion) -> Any:
		...

	def GetFileFormatVersionAtLoad(self) -> Any:
		...

	def FindPadByNumber(self, aPadNumber, aSearchAfterMe=None) -> Any:
		...

	def GetPad(self, *args) -> Any:
		...

	def GetPadCount(self, *args) -> Any:
		...

	def GetUniquePadCount(self, *args) -> Any:
		...

	def GetNextPadNumber(self, aLastPadName) -> Any:
		...

	def GetTypeName(self) -> Any:
		...

	def GetArea(self, aPadding=0) -> Any:
		...

	def GetLink(self) -> Any:
		...

	def SetLink(self, aLink) -> Any:
		...

	def DuplicateItem(self, aItem, aAddToFootprint=False) -> Any:
		...

	def Add3DModel(self, a3DModel) -> Any:
		...

	def RunOnChildren(self, aFunction) -> Any:
		...

	def ViewGetLOD(self, aLayer, aView) -> Any:
		...

	def FootprintNeedsUpdate(self, aLibFootprint) -> Any:
		...

	def SetInitialComments(self, aInitialComments) -> Any:
		...

	def CoverageRatio(self, aCollector) -> Any:
		...

	def GetInitialComments(self) -> Any:
		...

	def GetCourtyard(self, aLayer) -> Any:
		...

	def BuildCourtyardCaches(self, aErrorHandler=None) -> Any:
		...

	def GetEffectiveShape(self, *args) -> Any:
		...

	def GetProperties(self) -> Mapping[str, str]:
		...

	def GetProperty(self, key) -> Any:
		...

	def SetProperties(self, properties) -> Any:
		...
