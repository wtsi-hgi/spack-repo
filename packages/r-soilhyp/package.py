# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoilhyp(RPackage):
	"""Soil Hydraulic Properties

	Provides functions for (1) soil water retention (SWC) and unsaturated hydraulic conductivity (Ku) (van Genuchten-Mualem (vGM or vG) [1, 2], Peters-Durner-Iden (PDI) [3, 4, 5], Brooks and Corey (bc) [8]), (2) fitting of parameter for SWC  and/or Ku using Shuffled Complex Evolution (SCE) optimisation and (3) calculation of soil hydraulic properties (Ku and soil water contents) based on the simplified evaporation method (SEM) [6, 7].
    Main references:
    [1] van Genuchten (1980) <doi:10.2136/sssaj1980.03615995004400050002x>, 
    [2] Mualem (1976) <doi:10.1029/WR012i003p00513>, 
    [3] Peters (2013) <doi:10.1002/wrcr.20548>, 
    [4] Iden and Durner (2013) <doi:10.1002/2014WR015937>, 
    [5] Peters (2014) <doi:10.1002/2014WR015937>,
    [6] Wind G. P. (1966),
    [7] Peters and Durner (2008) <doi:10.1016/j.jhydrol.2008.04.016> and
    [8] Brooks and Corey (1964).
	"""
	
	cran = "SoilHyP" 

	version("0.1.7", md5="838696a62c6caf604b5c60b7e2e9544a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
