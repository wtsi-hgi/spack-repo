# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecr(RPackage):
	"""Spatially Explicit Capture-Recapture

	Functions to estimate the density and size of a spatially 
  distributed animal population sampled with an array of passive detectors, 
  such as traps, or by searching polygons or transects. Models incorporating 
  distance-dependent detection are fitted by maximizing the likelihood. 
  Tools are included for data manipulation and model selection.
	"""
	
	homepage = "https://www.otago.ac.nz/density/"
	cran = "secr" 

	version("4.6.6", md5="5815a808aa311e42b46de1156fec135e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-raster@3.5.15:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra@1.5.12:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
