# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRac(RPackage):
	"""R Package for Aqua Culture

	Solves the individual bioenergetic balance for different aquaculture sea fish (Sea Bream and Sea Bass; Brigolin et al., 2014 <doi:10.3354/aei00093>) and shellfish (Mussel and Clam; Brigolin et al., 2009 <doi:10.1016/j.ecss.2009.01.029>; Solidoro et al., 2000 <doi:10.3354/meps199137>). Allows for spatialized model runs and population simulations.
	"""
	
	cran = "RAC" 

	version("1.5.5", md5="d97420f67da6febcb38b23b6997e8c85")

	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
