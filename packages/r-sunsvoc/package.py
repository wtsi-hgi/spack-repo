# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSunsvoc(RPackage):
	"""Constructing Suns-Voc from Outdoor Time-Series I-V Curves

	
    Suns-Voc (or Isc-Voc) curves can provide the current-voltage (I-V) characteristics of the
    diode of photovoltaic cells without the effect of series resistance.
    Here, Suns-Voc curves can be constructed with outdoor time-series I-V
    curves [1,2,3] of full-size photovoltaic (PV) modules instead of having to be measured in the lab.
    Time series of four different power loss modes can be calculated based on obtained Isc-Voc curves.
    This material is based upon work supported by the U.S. Department of
    Energy's Office of Energy Efficiency and Renewable Energy (EERE) under
    Solar Energy Technologies Office (SETO) Agreement Number DE-EE0008172. 
    Jennifer L. Braid is supported by the U.S. Department of Energy (DOE) Office of 
    Energy Efficiency and Renewable Energy administered by the Oak Ridge 
    Institute for Science and Education (ORISE) for the DOE. 
    ORISE is managed by Oak Ridge Associated Universities (ORAU) under DOE
    contract number DE-SC0014664. 
    [1] Wang, M. et al, 2018. 
    <doi:10.1109/PVSC.2018.8547772>. 
    [2] Walters et al, 2018
    <doi:10.1109/PVSC.2018.8548187>. 
    [3] Guo, S. et al, 2016. 
    <doi:10.1117/12.2236939>. 
	"""
	
	cran = "SunsVoc" 

	version("0.1.2", md5="219907f8bf899fef5b21947e53456ec1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ddiv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
