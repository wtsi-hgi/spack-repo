# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDendrosync(RPackage):
	"""A Set of Tools for Calculating Spatial Synchrony Between
Tree-Ring Chronologies

	Provides functions for the calculation and plotting of synchrony in 
      tree growth from tree-ring width chronologies (TRW index). It combines
      variance-covariance (VCOV) mixed modelling with functions that quantify 
      the degree to which the TRW chronologies contain a common temporal 
      signal. It also implements temporal trends in spatial synchrony using a 
      moving window. These methods can also be used with other kind of ecological
      variables that have temporal autocorrelation corrected.
	"""
	
	homepage = "https://bitbucket.org/josucham/dendrosync/src/issues/"
	cran = "DendroSync" 

	version("0.1.4", md5="60581074b1e4e0b7fe3cb51df3d446ca")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
