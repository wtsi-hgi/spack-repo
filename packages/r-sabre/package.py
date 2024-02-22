# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSabre(RPackage):
	"""Spatial Association Between Regionalizations

	Calculates a degree of spatial association between regionalizations 
    or categorical maps using the information-theoretical V-measure 
    (Nowosad and Stepinski (2018) <doi:10.1080/13658816.2018.1511794>). It also
    offers an R implementation of the MapCurve method 
    (Hargrove et al. (2006) <doi:10.1007/s10109-006-0025-x>).
	"""
	
	homepage = "https://jakubnowosad.com/sabre/"
	cran = "sabre" 

	version("0.4.3", md5="ed6b3cccd355c30ac2f2e2d4fed9550c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
