# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConstrainedkriging(RPackage):
	"""Constrained, Covariance-Matching Constrained and Universal Point
or Block Kriging

	Provides functions for efficient computation of non-linear spatial predictions with local change of support (Hofer, C. and Papritz, A. (2011) "constrainedKriging: An R-package for customary, constrained and covariance-matching constrained point or block kriging" <doi:10.1016/j.cageo.2011.02.009>).  This package supplies functions for two-dimensional spatial interpolation by constrained (Cressie, N. (1993) "Aggregation in geostatistical problems" <doi:10.1007/978-94-011-1739-5_3>), covariance-matching constrained (Aldworth, J. and Cressie, N. (2003) "Prediction of nonlinear spatial functionals" <doi:10.1016/S0378-3758(02)00321-X>) and universal (external drift) Kriging for points or blocks of any shape from data with a non-stationary mean function and an isotropic weakly stationary covariance function.  The linear spatial interpolation methods, constrained and covariance-matching constrained Kriging, provide approximately unbiased prediction for non-linear target values under change of support.  This package extends the range of tools for spatial predictions available in R and provides an alternative to conditional simulation for non-linear spatial prediction problems with local change of support.
	"""
	
	cran = "constrainedKriging" 

	version("0.2-7", md5="51cb6965951fab62af8c9340097c9f13")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-sp@0.9.60:", type=("build", "run"))
	depends_on("r-sf@1.0.14:", type=("build", "run"))
	depends_on("r-spatialcovariance@0.6.4:", type=("build", "run"))
