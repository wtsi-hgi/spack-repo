# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgspatial(RPackage):
	"""Fitting the Centered Autologistic and Sparse Spatial Generalized
Linear Mixed Models for Areal Data

	Provides tools for analyzing spatial data, especially non-
    Gaussian areal data. The current version supports the sparse restricted
    spatial regression model of Hughes and Haran (2013) <DOI:10.1111/j.1467-9868.2012.01041.x>,
	the centered autologistic model of Caragea and Kaiser (2009) <DOI:10.1198/jabes.2009.07032>,
	and the Bayesian spatial filtering model of Hughes (2017) <arXiv:1706.04651>.
	"""
	
	cran = "ngspatial" 

	version("1.2-2", md5="ae6fa41d9eaf1211807bff56317b7f9b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-batchmeans", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
