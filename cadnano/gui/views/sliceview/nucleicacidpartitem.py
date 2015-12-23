from collections import OrderedDict

from PyQt5.QtCore import QPointF, Qt, QLineF, QRectF, QEvent, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtGui import QBrush, QColor, QPainterPath, QPen
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsEllipseItem
from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtWidgets import QApplication

from cadnano import getReopen, util
from cadnano.enum import PartEdges
from cadnano.gui.controllers.itemcontrollers.nucleicacidpartitemcontroller import NucleicAcidPartItemController
from cadnano.gui.palette import getPenObj, getBrushObj
from cadnano.gui.views.abstractitems.abstractpartitem import AbstractPartItem
from . import slicestyles as styles
from .activesliceitem import ActiveSliceItem
from .virtualhelixitem import VirtualHelixItem
from .sliceextras import PreXoverItemGroup


_RADIUS = styles.SLICE_HELIX_RADIUS
_DEFAULT_RECT = QRectF(0, 0, 2 * _RADIUS, 2 * _RADIUS)
HIGHLIGHT_WIDTH = styles.SLICE_HELIX_MOD_HILIGHT_WIDTH
DELTA = (HIGHLIGHT_WIDTH - styles.SLICE_HELIX_STROKE_WIDTH)/2.
_HOVER_RECT = _DEFAULT_RECT.adjusted(-DELTA, -DELTA, DELTA, DELTA)
_MOD_PEN = getPenObj(styles.BLUE_STROKE, HIGHLIGHT_WIDTH)

_DEFAULT_WIDTH = styles.DEFAULT_PEN_WIDTH
_DEFAULT_ALPHA = styles.DEFAULT_ALPHA
_SELECTED_COLOR = styles.SELECTED_COLOR
_SELECTED_WIDTH = styles.SELECTED_PEN_WIDTH
_SELECTED_ALPHA = styles.SELECTED_ALPHA

_BOUNDING_RECT_PADDING = 10

class NucleicAcidPartItem(QGraphicsRectItem, AbstractPartItem):
    _RADIUS = styles.SLICE_HELIX_RADIUS

    def __init__(self, model_part_instance, active_tool_getter, parent=None):
        """
        Parent should be either a SliceRootItem, or an AssemblyItem.

        Invariant: keys in _empty_helix_hash = range(_nrows) x range(_ncols)
        where x is the cartesian product.

        Order matters for deselector, probe, and setlattice
        """
        super(NucleicAcidPartItem, self).__init__(parent)
        self._model_instance = model_part_instance
        self._model_part = m_p = model_part_instance.reference()
        self._model_props = m_props = m_p.getPropertyDict()

        self._getActiveTool = active_tool_getter

        self._controller = NucleicAcidPartItemController(self, m_p)
        self._active_slice_item = ActiveSliceItem(self, m_p.activeBaseIndex())
        self._scale_factor = self._RADIUS / m_p.radius()

        self._virtual_helix_item_hash = {}

        self.hide() # hide while until after attemptResize() to avoid flicker

        self._rect = QRectF(0, 0, 1000, 1000)
        self._updateGeometry()
        self.setPen(getPenObj(_SELECTED_COLOR, _DEFAULT_WIDTH))
        self.setBrush(getBrushObj(_SELECTED_COLOR, _DEFAULT_WIDTH))
        self.setRect(self._rect)
        self.setAcceptHoverEvents(True)

        # Cache of VHs that were active as of last call to activeSliceChanged
        # If None, all slices will be redrawn and the cache will be filled.
        # Connect destructor. This is for removing a part from scenes.

        # initialize the NucleicAcidPartItem with an empty set of old coords
        # self.setFlag(QGraphicsItem.ItemHasNoContents)  # never call paint
        self.setZValue(styles.ZPARTITEM)

        _p = _BOUNDING_RECT_PADDING
        self._outlinerect = _orect = self.boundingRect().adjusted(-_p, -_p, _p, _p)
        self._outline = QGraphicsRectItem(_orect, self)
        self._outline.setFlag(QGraphicsItem.ItemStacksBehindParent)
        self._outline.setZValue(styles.ZDESELECTOR)
        self._outline.setPen(getPenObj(self.modelColor(), _DEFAULT_WIDTH))
        # self._outline.setPen(QPen(Qt.NoPen))
        # self._drag_handle = DragHandle(QRectF(_orect), self)
        # self._drag_handle.attemptResize(QRectF(441.6, 360, 160, 135.5)) # show 3rows x 6cols
        # if len(m_p.document().children()) > 1:
        #     self._adjustPosition()
        # select upon creation
        for _part in m_p.document().children():
            if _part is m_p:
                _part.setSelected(True)
            else:
                _part.setSelected(False)
        self.show()
    # end def

    def getVHItemList(self):
        return sorted(self._virtual_helix_hash.values(), key=lambda t:t.number())

    def _adjustPosition(self):
        """Find the left-most bottom-most sibling, and reposition below."""
        _p = _BOUNDING_RECT_PADDING
        _visible_topleft_pos = self.visibleTopLeftScenePos()
        _bot_left_sib = self.mapToScene(QPointF(-_p*2,-_p*2)) # choose a starting point
        for sibling in self.parentItem().childItems():
            if sibling is self:
                continue
            _sib = sibling.visibleBottomLeftScenePos()
            if (_sib.x() >= _bot_left_sib.x() and _sib.y() >= _bot_left_sib.y()):
                _bot_left_sib = _sib
        # reposition visible-topleft curner under sibling, plus padding
        self.setPos(-_visible_topleft_pos + _bot_left_sib + QPointF(0, 2*_p) )
    # end def

    def visibleTopLeftScenePos(self):
        return self.mapToScene(self._outlinerect.topLeft())
    # end def

    def visibleBottomLeftScenePos(self):
        return self.mapToScene(self._outlinerect.bottomLeft())
    # end def

    ### SIGNALS ###

    ### SLOTS ###
    def partActiveVirtualHelixChangedSlot(self, part, virtualHelix):
        pass

    def partPropertyChangedSlot(self, model_part, property_key, new_value):
        if self._model_part == model_part:
            if property_key == 'color':
                self._model_props['color'] = new_value
                self._outline.setPen(getPenObj(new_value, _DEFAULT_WIDTH))
                for vhi in self._virtual_helix_hash.items():
                    vhi.updateAppearance()
            elif property_key == 'circular':
                pass
            elif property_key == 'dna_sequence':
                pass
                # self.updateRects()
    # end def

    def partRemovedSlot(self, sender):
        """docstring for partRemovedSlot"""
        self._active_slice_item.removed()
        self.parentItem().removePartItem(self)

        scene = self.scene()

        self._virtual_helix_hash = None

        scene.removeItem(self)

        self._model_part = None
        self.probe = None
        self._mod_circ = None

        self.deselector = None
        self._controller.disconnectSignals()
        self._controller = None
    # end def

    def partVirtualHelicesReorderedSlot(self, sender, ordered_coord_list):
        pass
    # end def

    def partVirtualHelicesTranslatedSlot(self, sender,
                                                vh_set, left_overs,
                                                do_deselect):
        """
        left_overs are neighbors that need updating due to changes
        """
        if do_deselect:
            tool = self._getActiveTool()
            if tool.methodPrefix() == "selectTool":
                if tool.isSelectionActive():
                    tool.deselectItems()

        # 1. move everything that moved
        for vh in vh_set:
            vhi = self._virtual_helix_item_hash[vh]
            vhi.updatePosition()
        # 2. now redraw what makes sense to be redrawn
        for vh in vh_set:
            vhi = self._virtual_helix_item_hash[vh]
            self.refreshVirtualHelixItemGizmos(vh, vhi)
        for vh in left_overs:
            vhi = self._virtual_helix_item_hash[vh]
            self.refreshVirtualHelixItemGizmos(vh, vhi)
    # end def

    def refreshVirtualHelixItemGizmos(self, vh, vhi):
        """Update props and appearance of self & recent neighbors."""
        neighbors = vh.getProperty('neighbors')

        vhi.beginAddWedgeGizmos()
        for nvh in neighbors:
            nvhi = self._virtual_helix_item_hash[nvh]
            vhi.setWedgeGizmo(nvh, nvhi)
        # end for
        vhi.endAddWedgeGizmos()
    # end def

    def partPreDecoratorSelectedSlot(self, sender, row, col, base_idx):
        """docstring for partPreDecoratorSelectedSlot"""
        vhi = self.getVirtualHelixItemByCoord(row, col)
        view = self.window().slice_graphics_view
        view.scene_root_item.resetTransform()
        view.centerOn(vhi)
        view.zoomIn()
        m_c = self._mod_circ
        x,y = self._model_part.latticeCoordToPositionXY(row, col, self.scaleFactor())
        m_c.setPos(x,y)
        if self._can_show_mod_circ:
            m_c.show()
    # end def

    def partVirtualHelixAddedSlot(self, sender, virtual_helix):
        vh = virtual_helix
        # TODO test to see if self._virtual_helix_hash is necessary
        vhi = VirtualHelixItem(vh, self)
        # self._virtual_helix_item_list.append(virtual_helix_item)
        self._virtual_helix_item_hash[virtual_helix] = vhi
    # end def

    def partVirtualHelixRenumberedSlot(self, sender, coord):
        pass
    # end def

    def partVirtualHelixResizedSlot(self, sender, coord):
        pass
    # end def

    def updatePreXoverItemsSlot(self, sender, virtual_helix):
        pass
    # end def

    def partColorChangedSlot(self):
        print("sliceview Dnapart partColorChangedSlot")
    # end def

    def partSelectedChangedSlot(self, model_part, is_selected):
        """Set this Z to front, and return other Zs to default."""
        if is_selected:
            # self._drag_handle.resetAppearance(_SELECTED_COLOR, _SELECTED_WIDTH, _SELECTED_ALPHA)
            self.setZValue(styles.ZPARTITEM+1)
        else:
            # self._drag_handle.resetAppearance(self.modelColor(), _DEFAULT_WIDTH, _DEFAULT_ALPHA)
            self.setZValue(styles.ZPARTITEM)

    ### ACCESSORS ###
    def boundingRect(self):
        return self._rect
    # end def

    def part(self):
        return self._model_part
    # end def

    def modelColor(self):
        return self._model_props['color']
    # end def

    def scaleFactor(self):
        return self._scale_factor
    # end def

    def setPart(self, new_part):
        self._model_part = new_part
    # end def

    def window(self):
        return self.parentItem().window()
    # end def

    def removeVirtualHelixItem(self, virtual_helix_item):
        vh = virtual_helix_item.virtualHelix()
        # self._virtual_helix_item_list.remove(virtual_helix_item)
        del self._virtual_helix_item_hash[vh]
        # del self._virtual_helix_hash[vh.coord()]
        # ztf = not getBatch()
        # self._setVirtualHelixItemList(self._virtual_helix_item_list,
        #     zoom_to_fit=ztf)
        # self._updateBoundingRect()
    # end def



    ### PRIVATE SUPPORT METHODS ###
    def _upperLeftCornerForCoords(self, row, col):
        pass  # subclass
    # end def

    def _updateGeometry(self):
        self._rect = QRectF(*self.part().dimensions(self._scale_factor))
    # end def


    def _setLattice(self, old_coords, new_coords):
        """A private method used to change the number of rows,
        cols in response to a change in the dimensions of the
        part represented by the receiver"""
        old_set = set(old_coords)
        old_list = list(old_set)
        new_set = set(new_coords)
        new_list = list(new_set)
        for coord in old_list:
            if coord not in new_set:
                self._killHelixItemAt(*coord)
        # end for
        for coord in new_list:
            if coord not in old_set:
                self._spawnEmptyHelixItemAt(*coord)
        # end for
        # self._updateGeometry(newCols, newRows)
        # self.prepareGeometryChange()
        # the Deselector copies our rect so it changes too
        self.deselector.prepareGeometryChange()
        if not getReopen():
            self.zoomToFit()
    # end def

    ### PUBLIC SUPPORT METHODS ###
    def getVirtualHelixItemByCoord(self, row, column):
        if (row, column) in self._empty_helix_hash:
            return self._virtual_helix_hash[(row, column)]
        else:
            return None
    # end def

    # def paint(self, painter, option, widget=None):
    #     pass
    # # end def

    def selectionWillChange(self, newSel):
        if self.part() is None:
            return
        if self.part().selectAllBehavior():
            return
        for sh in self._empty_helix_hash.values():
            sh.setSelected(sh.virtualHelix() in newSel)
    # end def

    def setModifyState(self, bool):
        """Hides the mod_rect when modify state disabled."""
        self._can_show_mod_circ = bool
        if bool == False:
            self._mod_circ.hide()

    def updateStatusBar(self, statusString):
        """Shows statusString in the MainWindow's status bar."""
        pass  # disabled for now.
        # self.window().statusBar().showMessage(statusString, timeout)

    def vhAtCoordsChanged(self, row, col):
        self._empty_helix_hash[(row, col)].update()
    # end def

    def zoomToFit(self):
        thescene = self.scene()
        theview = thescene.views()[0]
        theview.zoomToFit()
    # end def

    ### EVENT HANDLERS ###
    def mousePressEvent(self, event):
        self.part().setSelected(True)
        tool = self._getActiveTool()
        tool_method_name = tool.methodPrefix() + "MousePress"
        if hasattr(self, tool_method_name):
            getattr(self, tool_method_name)(tool, event)
        else:
            event.setAccepted(False)
            QGraphicsItem.mousePressEvent(self, event)
    # end def

    def hoverMoveEvent(self, event):
        tool = self._getActiveTool()
        tool_method_name = tool.methodPrefix() + "HoverMove"
        if hasattr(self, tool_method_name):
            getattr(self, tool_method_name)(tool, event)
        else:
            event.setAccepted(False)
            QGraphicsItem.hoverMoveEvent(self, event)
    # end def

    def getModelPos(self, pos):
        """ Y-axis is inverted in Qt +y === DOWN
        """
        sf = self._scale_factor
        x, y = pos.x()/sf, -1.0*pos.y()/sf
        return x, y
    # end def

    def getVirtualHelixItem(self, virtual_helix):
        return self._virtual_helix_item_hash.get(virtual_helix)

    def createToolMousePress(self, tool, event):
        # 1. get point in model coordinates:
        pt = tool.eventToPosition(self, event)
        if pt is None:
            tool.deactivate()
            return QGraphicsItem.mousePressEvent(self, event)

        part_pt_tuple = self.getModelPos(pt)

        mod = Qt.MetaModifier
        if not (event.modifiers() & mod):
            pass
        part = self._model_part

        # don't create a new VirtualHelix if the click overlaps with existing
        # VirtualHelix
        check = part.isVirtualHelixNearPoint(part_pt_tuple)
        tool.setPartItem(self)
        if check:
            virtual_helix = part.getVirtualHelixAtPoint(part_pt_tuple)
            if virtual_helix is not None:
                vhi = self._virtual_helix_item_hash[virtual_helix]
                tool.setVirtualHelixItem(vhi)
                tool.startCreation()
        else:
            part.createVirtualHelix(*part_pt_tuple)
            virtual_helix = part.getVirtualHelixAtPoint(part_pt_tuple)
            neighbors = part.getVirtualHelixNeighbors(virtual_helix)
            # print("neighbors to {}:".format(virtual_helix.number()))
            # for vh in neighbors:
            #     print(vh)
            vhi = self._virtual_helix_item_hash[virtual_helix]
            tool.setVirtualHelixItem(vhi)
            tool.startCreation()
        return QGraphicsItem.mousePressEvent(self, event)
    # end def

    def createToolHoverMove(self, tool, event):
        tool.hoverMoveEvent(self, event)
        return QGraphicsItem.hoverMoveEvent(self, event)
    # end def

    def selectToolMousePress(self, tool, event):
        """
        """
        print("select tool part item")
        tool.setPartItem(self)
        pt = tool.eventToPosition(self, event)
        part_pt_tuple = self.getModelPos(pt)
        part = self._model_part
        if part.isVirtualHelixNearPoint(part_pt_tuple):
            vh = part.getVirtualHelixAtPoint(part_pt_tuple)
            if vh is not None:
                print(vh)
                loc = vh.location()
                print("VirtualHelix #{} at ({:.3f}, {:.3f})".format(vh.number(),
                    loc[0], loc[1] ))
            else:
                tool.deselectItems()
        else:
            tool.deselectItems()
        return QGraphicsItem.mousePressEvent(self, event)
    # end def

    class IntersectionProbe(QGraphicsItem):
        def boundingRect(self):
            return QRectF(0, 0, .1, .1)
        def paint(self, painter, option, widget=None):
            pass


# end class
