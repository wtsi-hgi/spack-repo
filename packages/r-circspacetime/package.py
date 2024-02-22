# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircspacetime(RPackage):
	"""Spatial and Spatio-Temporal Bayesian Model for Circular Data

	Implementation of Bayesian models for spatial and spatio-temporal
             interpolation of circular data using Gaussian Wrapped and Gaussian Projected distributions.
             We developed the methods described in Jona Lasinio G. et al. (2012) <doi: 10.1214/12-aoas576>, 
             Wang F. et al. (2014) <doi: 10.1080/01621459.2014.934454> and 
             Mastrantonio G. et al. (2016) <doi: 10.1007/s11749-015-0458-y>.
	"""
	
	homepage = "https://github.com/santoroma/CircSpaceTime"
	cran = "CircSpaceTime" 

	version("0.9.0", md5="a7ae19dae9bed39bbe58a2346dd9abb8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-rinside", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
