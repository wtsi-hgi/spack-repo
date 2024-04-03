# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarestr(RPackage):
	"""Rarefaction-Based Species Richness Estimator

	Calculate rarefaction-based alpha- and beta-diversity. Offer parametric extrapolation to estimate the total expected species in a single community and the total expected shared species between two communities. Visualize the curve-fitting for these estimators.
	"""
	
	homepage = "https://github.com/pzhaonet/rarestR"
	cran = "rarestR" 

	version("1.0.0", md5="9556770724c35e308f706f99a06383ee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
