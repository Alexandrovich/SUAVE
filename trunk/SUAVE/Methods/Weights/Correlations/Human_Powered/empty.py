# empty.py
# 
# Created:  Emilio Botero, Jun 2014
# Modified:  

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUave imports
import SUAVE

# package imports
import numpy as np
import tail as tail
import wing as wing
import fuselage as fuselage
import warnings

from SUAVE.Core import Units
from SUAVE.Core import (
    Data, Container, Data_Exception, Data_Warning,
    )

def empty(vehicle):
    """ weight = SUAVE.Methods.Weights.Correlations.Solar_HPA_weights.empty(wing,aircraft,horizontal,vertical): 
            
        Inputs:
            wing - a data dictionary with the fields:
                Sw -       wing area [m**2]
                bw -       wing span [m]
                cw -       average wing chord [m]
                deltaw -   average rib spacing to average chord ratio
                Nwr -      number of wing surface ribs (bw**2)/(deltaw*Sw)
                t_cw -     wing airfoil thickness to chord ratio
                Nwer -     number of wing end ribs (2*number of individual wing panels -2)
                
            horizontal - a data dictionary with the fields:
                Sts -      tail surface area (m)
                bts -      tail surface span (m)
                cts -      average tail surface chord (m)
                deltawts - average rib spacing to average chord ratio
                Ntsr -     number of tail surface ribs (bts^2)/(deltats*Sts)
                t_cts -    tail airfoil thickness to chord ratio
                
            vertical - a data dictionary with the fields:
                Sts -      tail surface area (m)
                bts -      tail surface span (m)
                cts -      average tail surface chord (m)
                deltawts - average rib spacing to average chord ratio
                Ntsr -     number of tail surface ribs (bts**2)/(deltats*Sts)
                t_cts -    tail airfoil thickness to chord ratio
                
            aircraft - a data dictionary with the fields:    
                nult -     ultimate load factor
                GW -       aircraft gross weight
                qm -       dynamic pressure at maneuvering speed (N/m2)
                Ltb -      tailboom length (m)
        
            Outputs:
                Wws -      weight of wing spar (kg)
                Wtss -     weight of tail surface spar (kg)
                Wwr -      weight of wing ribs (kg)
                Wtsr -     weight of tail surface ribs (kg)
                Wwer -     weight of wing end ribs (kg)
                WwLE -     weight of wing leading edge (kg)
                WtsLE -    weight of tail surface leading edge (kg)
                WwTE -     weight of wing trailing edge (kg)
                Wwc -      weight of wing covering (kg)
                Wtsc -     weight of tail surface covering (kg)
                Wtb -      tailboom weight (kg)
                    
            Assumptions:
                All of this is from AIAA 89-2048, units are in kg. These weight estimates
                are from the MIT Daedalus and are valid for very lightweight
                carbon fiber composite structures. This may need to be solved iteratively since
                gross weight is an input.
                
        """
    
    #Unpack
    
    nult   = vehicle.envelope.ultimate_load
    gw     = vehicle.mass_properties.max_takeoff
    qm     = vehicle.qm
    
    # Wing weight
    if not vehicle.wings.has_key('main_wing'):
        wt_wing = 0.0
        warnings.warn("There is no Wing Weight being added to the Configuration", stacklevel=1)
    else:
        Sw      = vehicle.wings['main_wing'].areas.reference
        bw      = vehicle.wings['main_wing'].spans.projected
        cw      = vehicle.wings['main_wing'].chords.mean_aerodynamic
        Nwr     = vehicle.wings['main_wing'].number_ribs
        t_cw    = vehicle.wings['main_wing'].thickness_to_chord
        Nwer    = vehicle.wings['main_wing'].number_end_ribs
        wt_wing = wing.wing(Sw,bw,cw,Nwr,t_cw,Nwer,nult,gw)
        vehicle.wings['main_wing'].mass_properties.mass = wt_wing
    
    # Horizontal Tail weight
    if not vehicle.wings.has_key('horizontal_stabilizer'):
        wt_ht = 0.0
        warnings.warn("There is no Horizontal Tail Weight being added to the Configuration", stacklevel=1)
    else:      
        S_h    = vehicle.wings['horizontal_stabilizer'].areas.reference
        b_h    = vehicle.wings['horizontal_stabilizer'].spans.projected
        chs    = vehicle.wings['horizontal_stabilizer'].chords.mean_aerodynamic
        Nhsr   = vehicle.wings['horizontal_stabilizer'].number_ribs
        t_ch   = vehicle.wings['horizontal_stabilizer'].thickness_to_chord
        wt_ht  = tail.tail(S_h,b_h,chs,Nhsr,t_ch,qm)
        vehicle.wings['horizontal_stabilizer'].mass_properties.mass = wt_ht
    
    # Vertical Tail weight
    if not vehicle.wings.has_key('vertical_stabilizer'):   
        wt_vt = 0.0
        warnings.warn("There is no Vertical Tail Weight being added to the Configuration", stacklevel=1)    
    else:    
        S_v    = vehicle.wings['vertical_stabilizer'].areas.reference
        b_v    = vehicle.wings['vertical_stabilizer'].spans.projected
        cvs    = vehicle.wings['vertical_stabilizer'].chords.mean_aerodynamic
        Nvsr   = vehicle.wings['vertical_stabilizer'].number_ribs
        t_cv   = vehicle.wings['vertical_stabilizer'].thickness_to_chord
        wt_vt   = tail.tail(S_v,b_v,cvs,Nvsr,t_cv,qm)
        vehicle.wings['vertical_stabilizer'].mass_properties.mass = wt_vt

    ##Fuselage weight
    #Ltb     = vehicle.Ltb  
    #wt_tb   = fuselage.fuselage(S_h,qm,Ltb)
    #vehicle.Fuselages['fuselage'].mass_properties.mass = wt_tb
    
    weight                 = Data()
    weight.wing            = wt_wing
    #weight.fuselage        = wt_tb
    weight.horizontal_tail = wt_ht
    weight.vertical_tail   = wt_vt
    
    return weight
    
    
    
    
    
    
    
    
    