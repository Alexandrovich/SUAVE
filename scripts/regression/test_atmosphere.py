# test_atmosphere.py
# 
# Created:  Mike Colonno, Dec 2013
# Modified: Trent Lukaczyk, Jun 2014

# ----------------------------------------------------------------------        
#   Imports
# ----------------------------------------------------------------------  

import SUAVE
import numpy as np
import matplotlib.pyplot as plt
from SUAVE.Core import Units


# ----------------------------------------------------------------------        
#   Main
# ----------------------------------------------------------------------  

def main():
    
    # ------------------------------------------------------------------
    #   The Tests
    # ------------------------------------------------------------------    

    # initialize atmospheric models
    atm = SUAVE.Attributes.Atmospheres.Earth.International_Standard()
    
    # test elevations -3 km <= z <= 90 km
    z = np.linspace(-3,90,100) * Units.km

    # compute values from each model
    p, T, rho, a, mew = atm.compute_values(z)
    
    # get the comparison values
    p_truth, T_truth, rho_truth, a_truth = get_truth()
    
    # difference
    p_err   = np.max( p_truth  -p   )
    T_err   = np.max( T_truth  -T   )
    rho_err = np.max( rho_truth-rho )
    a_err   = np.max( a_truth  -a   )
    
    print 'Max Pressure Difference       = %.4e' % p_err
    print 'Max Temperature Difference    = %.4e' % T_err
    print 'Max Density Difference        = %.4e' % rho_err
    print 'Max Speed of Sound Difference = %.4e' % a_err
    
    
    # ------------------------------------------------------------------
    #   Plotting
    # ------------------------------------------------------------------    

    # plot data
    title = "International Standard Atmosphere"
    plt.subplot(131)
    plt.plot(p/101325,z)
    plt.xlabel('Pressure (atm)'); plt.xscale('log')
    plt.ylabel('Altitude (km)')
    plt.title(title)
    plt.grid(True)

    plt.subplot(132)
    plt.plot(rho,z)
    plt.xlabel('Density (kg/m^3)'); plt.xscale('log')
    plt.ylabel('Altitude (km)')
    plt.title(title)
    plt.grid(True)

    plt.subplot(133)
    plt.plot(T,z)
    plt.xlabel('Temperature (K)'); 
    plt.ylabel('Altitude (km)')
    plt.title(title)
    plt.grid(True)
    
    # ------------------------------------------------------------------
    #   Check Results
    # ------------------------------------------------------------------    

    assert( p_err   < 1e-1 )
    assert( T_err   < 1e-5 )
    assert( rho_err < 1e-5 )
    assert( a_err   < 1e-5 )    
 
    return

#: def main()


# ----------------------------------------------------------------------        
#   Helper Function
# ---------------------------------------------------------------------- 

def get_truth():
    p_truth = np.array([  1.27774000e+05,   1.27774000e+05,   1.15542264e+05,
             1.03528639e+05,   9.25500085e+04,   8.25367165e+04,
             7.34218760e+04,   6.51421228e+04,   5.76372994e+04,
             5.08503581e+04,   4.47272657e+04,   3.92169091e+04,
             3.42710012e+04,   2.98439888e+04,   2.58929602e+04,
             2.23778855e+04,   1.93071927e+04,   1.66585838e+04,
             1.43739418e+04,   1.24031654e+04,   1.07030616e+04,
             9.23639181e+03,   7.97104925e+03,   6.87935074e+03,
             5.93742612e+03,   5.12501757e+03,   4.42633079e+03,
             3.82545294e+03,   3.30833738e+03,   2.86300514e+03,
             2.47923320e+03,   2.14829089e+03,   1.86271677e+03,
             1.61612965e+03,   1.40306839e+03,   1.21885606e+03,
             1.05948455e+03,   9.21516659e+02,   8.02135612e+02,
             6.99272701e+02,   6.10555965e+02,   5.33911597e+02,
             4.67588202e+02,   4.10103876e+02,   3.60202417e+02,
             3.16817025e+02,   2.79040141e+02,   2.46098337e+02,
             2.17331377e+02,   1.92174713e+02,   1.70144832e+02,
             1.50826965e+02,   1.33864757e+02,   1.18951574e+02,
             1.05813428e+02,   9.41486471e+01,   8.37726447e+01,
             7.45427149e+01,   6.63319955e+01,   5.89893624e+01,
             5.24016325e+01,   4.64972371e+01,   4.12108114e+01,
             3.64827073e+01,   3.22585413e+01,   2.84887737e+01,
             2.51283185e+01,   2.21361804e+01,   1.94751196e+01,
             1.71113398e+01,   1.50142003e+01,   1.31559492e+01,
             1.15114767e+01,   1.00580876e+01,   8.77529094e+00,
             7.64460633e+00,   6.64938511e+00,   5.77464606e+00,
             5.00692418e+00,   4.33413171e+00,   3.74556777e+00,
             3.23267594e+00,   2.78656697e+00,   2.39900048e+00,
             2.06269595e+00,   1.77122761e+00,   1.51893010e+00,
             1.30081393e+00,   1.11248966e+00,   9.50100076e-01,
             8.10259515e-01,   6.89999674e-01,   5.86721242e-01,
             4.98150771e-01,   4.22302265e-01,   3.73400000e-01,
             3.73400000e-01,   3.73400000e-01,   3.73400000e-01,
             3.73400000e-01])    

    T_truth = np.array([ 301.15      ,  301.15      ,  295.43916158,  289.33185191,
        283.22634305,  277.1226342 ,  271.02072458,  264.92061337,
        258.8222998 ,  252.72578307,  246.63106237,  240.53813692,
        234.44700593,  228.3576686 ,  222.27012413,  216.65      ,
        216.65      ,  216.65      ,  216.65      ,  216.65      ,
        216.65      ,  216.65      ,  216.65      ,  216.65      ,
        216.65      ,  217.0691941 ,  218.00243897,  218.93540959,
        219.86810608,  220.80052857,  221.73267717,  222.664552  ,
        223.59615319,  224.52748086,  225.45853512,  226.3893161 ,
        227.31982391,  228.25005869,  230.1340575 ,  232.73718684,
        235.33955266,  237.94115531,  240.54199512,  243.14207242,
        245.74138756,  248.33994086,  250.93773267,  253.5347633 ,
        256.13103311,  258.72654243,  261.32129158,  263.91528091,
        266.50851074,  269.10098141,  270.65      ,  270.65      ,
        270.65      ,  270.65      ,  270.44804097,  267.86011827,
        265.2729524 ,  262.68654302,  260.10088982,  257.51599245,
        254.93185058,  252.34846389,  249.76583204,  247.1839547 ,
        244.60283154,  242.02246223,  239.44284644,  236.86398385,
        234.28587411,  231.7085169 ,  229.1319119 ,  226.55605877,
        223.98095718,  221.4066068 ,  218.83300731,  216.26015838,
        213.96299897,  212.12658644,  210.29070924,  208.45536714,
        206.6205599 ,  204.7862873 ,  202.95254908,  201.11934504,
        199.28667492,  197.4545385 ,  195.62293554,  193.79186581,
        191.96132908,  190.13132511,  188.30185367,  186.95      ,
        186.95      ,  186.95      ,  186.95      ,  186.95      ])
    
    rho_truth = np.array([  1.47808000e+00,   1.47808000e+00,   1.36241969e+00,
         1.24652891e+00,   1.13836338e+00,   1.03756016e+00,
         9.43758932e-01,   8.56612200e-01,   7.75782596e-01,
         7.00942778e-01,   6.31775349e-01,   5.67972775e-01,
         5.09237294e-01,   4.55280834e-01,   4.05824920e-01,
         3.59830899e-01,   3.10454913e-01,   2.67865934e-01,
         2.31129452e-01,   1.99439851e-01,   1.72102600e-01,
         1.48518910e-01,   1.28172513e-01,   1.10618269e-01,
         9.54723528e-02,   8.22498786e-02,   7.07327616e-02,
         6.08702318e-02,   5.24186288e-02,   4.51710430e-02,
         3.89516427e-02,   3.36108971e-02,   2.90215496e-02,
         2.50752225e-02,   2.16795499e-02,   1.87557568e-02,
         1.62366122e-02,   1.40646974e-02,   1.21424131e-02,
         1.04669197e-02,   9.03792338e-03,   7.81695998e-03,
         6.77190312e-03,   5.87586568e-03,   5.10630106e-03,
         4.44426594e-03,   3.87381444e-03,   3.38149900e-03,
         2.95595849e-03,   2.58757744e-03,   2.26820376e-03,
         1.99091425e-03,   1.74981959e-03,   1.53990175e-03,
         1.36198039e-03,   1.21183684e-03,   1.07828185e-03,
         9.59478560e-04,   8.54431641e-04,   7.67191436e-04,
         6.88160825e-04,   6.16633937e-04,   5.51959773e-04,
         4.93538406e-04,   4.40817398e-04,   3.93288449e-04,
         3.50484246e-04,   3.11975515e-04,   2.77368255e-04,
         2.46301151e-04,   2.18443155e-04,   1.93491218e-04,
         1.71168180e-04,   1.51220794e-04,   1.33417883e-04,
         1.17548623e-04,   1.03420942e-04,   9.08600339e-05,
         7.97069675e-05,   6.98174028e-05,   6.09841652e-05,
         5.30890762e-05,   4.61623064e-05,   4.00917815e-05,
         3.47776140e-05,   3.01308650e-05,   2.60724220e-05,
         2.25319839e-05,   1.94471436e-05,   1.67625595e-05,
         1.44292071e-05,   1.24037054e-05,   1.06477088e-05,
         9.12736108e-06,   7.81280375e-06,   6.95792000e-06,
         6.95792000e-06,   6.95792000e-06,   6.95792000e-06,
         6.95792000e-06])
    
    a_truth = np.array([ 347.88555919,  347.88555919,  344.57121859,  340.99113708,
        337.37413972,  333.7190257 ,  330.02452809,  326.2893086 ,
        322.51195186,  318.69095905,  314.82474085,  310.9116096 ,
        306.94977058,  302.93731227,  298.87219538,  295.06949567,
        295.06949567,  295.06949567,  295.06949567,  295.06949567,
        295.06949567,  295.06949567,  295.06949567,  295.06949567,
        295.06949567,  295.35482135,  295.9890494 ,  296.62173558,
        297.25288983,  297.88252196,  298.51064168,  299.13725861,
        299.76238224,  300.38602198,  301.00818714,  301.62888692,
        302.24813042,  302.86592667,  304.1133008 ,  305.82843194,
        307.533499  ,  309.22866868,  310.91410307,  312.58995988,
        314.25639254,  315.9135504 ,  317.56157886,  319.20061955,
        320.83081043,  322.45228591,  324.06517705,  325.66961157,
        327.26571407,  328.85360608,  329.79873342,  329.79873342,
        329.79873342,  329.79873342,  329.67566255,  328.0945345 ,
        326.50621557,  324.91060011,  323.30757988,  321.69704397,
        320.07887873,  318.45296765,  316.81919126,  315.17742704,
        313.52754929,  311.86942903,  310.20293388,  308.52792791,
        306.84427152,  305.15182132,  303.45042995,  301.73994593,
        300.02021354,  298.29107259,  296.55235829,  294.80390101,
        293.23398739,  291.97288378,  290.7066795 ,  289.43530744,
        288.15869903,  286.8767842 ,  285.58949133,  284.2967472 ,
        282.99847695,  281.69460399,  280.38505001,  279.06973485,
        277.7485765 ,  276.421491  ,  275.08839241,  274.09915863,
        274.09915863,  274.09915863,  274.09915863,  274.09915863])

    return p_truth, T_truth, rho_truth, a_truth
    

# ----------------------------------------------------------------------        
#   Call Main
# ---------------------------------------------------------------------- 

if __name__ == '__main__':
    main()
    plt.show()
