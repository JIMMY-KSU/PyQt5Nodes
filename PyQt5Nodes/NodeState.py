# -*- coding: utf-8 -*-
# !/usr/bin/env python3

#from typing import *
from enum import Enum

#from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PortType import *
from NodeData import *
from NodeDataModel import *
from NodeState import *
from Connection import *

#-----------------------------------------------------------------------------
class ReactToConnectionState(Enum):

    REACTING = True
    NOT_REACTING = False

#-----------------------------------------------------------------------------
class NodeState(object):

    def __init__(self, model: NodeDataModel):

        # create a list with one dict for each port of PortType, 
        self._outConnections = []
        for i in range(0, model.nPorts(PortType.Out)):
            self._outConnections.append({})

        # create a list with one dict for each port of PortType, 
        self._inConnections = []
        for i in range(0, model.nPorts(PortType.Out)):
            self._inConnections.append({})

        self._reaction = ReactToConnectionState.NOT_REACTING

        self._reactingPortType = PortType(PortType.No_One)

        self._resizing = False

    #-----------------------------------------------------------------------------
    def getEntries(self, portType: PortType) -> dict:
        if(portType == PortType.In):
            return self._inConnections
        else:
            return self._outConnections

    #-----------------------------------------------------------------------------
    def connections(self, portType: PortType, portIndex: PortIndex) -> dict:
        connections = self.getEntries(PortType)
        return connections[portIndex]        

    #-----------------------------------------------------------------------------
    def setConnection(self, portType: PortType, portIndex: PortIndex,
                         connection: Connection):

        connections = self.getEntries(portType)

        connections[portIndex].update({connection.id(): connection})

    #-----------------------------------------------------------------------------
    def eraseConnection(self, portType: PortType, portIndex: PortIndex,
                        id: QUuid):
        self.getEntries(portType)[portIndex].pop(id)
        
    #-----------------------------------------------------------------------------
    def reaction(self):
        return self._reaction

    #-----------------------------------------------------------------------------
    def reactingPortType(self) -> PortType:
        return self._reactingPortType

    #-----------------------------------------------------------------------------
    def reactingDataType(self) -> NodeDataType:
        return self._reactingDatatype

    #-----------------------------------------------------------------------------
    def setReaction(self, reaction: ReactToConnectionState,
                    reactingPortType: PortType=PortType.No_One, 
                    reactingDataType: NodeDataType =NodeDataType()):
        
        self._reaction = reaction

        self._reactingPortType = reactingPortType

        self._reactingDatatype = reactingDataType

    #-----------------------------------------------------------------------------
    def isReacting(self) -> bool:
        return self._reaction

    #-----------------------------------------------------------------------------
    def setResizing(self, resizing: bool):
        self._resizing = resizing

    #-----------------------------------------------------------------------------
    def resizing(self) -> bool:
        return self._resizing