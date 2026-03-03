# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdir(RPackage):
	"""Directional Highest Density Regions

	We provide an R tool for computation and nonparametric plug-in estimation of Highest Density Regions (HDRs) and general level sets in the directional setting. Concretely, circular and spherical HDRs can be reconstructed from a data sample following Saavedra-Nieves and Crujeiras (2021) <doi:10.1007/s11634-021-00457-4>. This library also contains two real datasets in the circular and spherical settings. The first one concerns a problem from animal orientation studies and the second one is related to earthquakes occurrences.
	"""
	
	cran = "HDiR" 

	version("1.1.3", md5="c927577d2340767f433d53f9130f288c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-npcirc", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-directional", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
