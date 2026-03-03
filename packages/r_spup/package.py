# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpup(RPackage):
	"""Spatial Uncertainty Propagation Analysis

	Uncertainty propagation analysis in spatial environmental  modelling following methodology
         described in Heuvelink et al. (2007) <doi:10.1080/13658810601063951> 
         and Brown and Heuvelink (2007) <doi:10.1016/j.cageo.2006.06.015>. The package provides functions
         for examining the uncertainty propagation starting from input data and model parameters,
         via the environmental model onto model outputs. The functions include uncertainty model specification,
         stochastic simulation and propagation of uncertainty using Monte Carlo (MC) techniques.
         Uncertain variables are described by probability distributions. Both numerical and categorical data types are handled.
         Spatial auto-correlation within an attribute and cross-correlation between attributes is accommodated for.
         The MC realizations may be used as input to the environmental models called from R, or externally.
	"""
	
	cran = "spup" 

	version("1.4-0", md5="f2103ffc092677fe0c2b77e14b98f235")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
