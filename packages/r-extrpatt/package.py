# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtrpatt(RPackage):
	"""Spatial Dependencies and Indices for Extremes

	An implementation of 
              1) the tail pairwise dependence matrix (TPDM) as described in Jiang & Cooley (2020) <doi:10.1175/JCLI-D-19-0413.1>  
              2) the extremal pattern index (EPI) as described in Szemkus & Friederichs ('Spatial patterns and indices for heatwave and droughts over Europe using a decomposition of extremal dependency'; submitted to ASCMO 2023). 
	"""
	
	cran = "ExtrPatt" 

	version("0.1-4", md5="792838b703ef50f6357d1e2cff63a0aa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
