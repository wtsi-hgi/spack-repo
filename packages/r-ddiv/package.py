# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdiv(RPackage):
	"""Data Driven I-v Feature Extraction

	The Data Driven I-V Feature Extraction is used to extract 
    Current-Voltage (I-V) features from I-V curves. I-V curves indicate the 
    relationship between current and voltage for a solar cell or Photovoltaic (PV) 
    modules. The I-V features such as maximum power point (Pmp), shunt resistance (Rsh), 
    series resistance (Rs),short circuit current (Isc), open circuit voltage (Voc), 
    fill factor (FF), current at maximum power (Imp) and voltage at maximum power(Vmp) 
    contain important information of the performance for PV modules. The traditional 
    method uses the single diode model to model I-V curves and extract I-V features. 
    This package does not use the diode model, but uses data-driven a method which 
    select different linear parts of the I-V curves to extract I-V features. 
    This method also uses a sampling method to calculate uncertainties when extracting 
    I-V features. Also, because of the partially shaded array, "steps" occurs in 
    I-V curves. The "Segmented Regression" method is used to identify steps in I-V curves.
    This material is based upon work supported by the U.S. Department of Energy’s 
    Office of Energy Efficiency and Renewable Energy (EERE) under Solar Energy 
    Technologies Office (SETO) Agreement Number DE-EE0007140. Further information can be 
    found in the following paper.
    [1] Ma, X. et al, 2019. 
    <doi:10.1109/JPHOTOV.2019.2928477>.
	"""
	
	cran = "ddiv" 

	version("0.1.1", md5="3b664f41795c4c964ff3dddac2b6da15")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass@0.5.3:", type=("build", "run"))
	depends_on("r-segmented@0.5.3:", type=("build", "run"))
	depends_on("r-qpdf@1.1:", type=("build", "run"))
