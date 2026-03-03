# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvospat(RPackage):
	"""Convolution-Based Nonstationary Spatial Modeling

	Fits convolution-based nonstationary
    Gaussian process models to point-referenced spatial data. The nonstationary
    covariance function allows the user to specify the underlying correlation
    structure and which spatial dependence parameters should be allowed to
    vary over space: the anisotropy, nugget variance, and process variance.
    The parameters are estimated via maximum likelihood, using a local
    likelihood approach. Also provided are functions to fit stationary spatial
    models for comparison, calculate the Kriging predictor and standard errors,
    and create various plots to visualize nonstationarity.
	"""
	
	homepage = "http://github.com/markdrisser/convoSPAT"
	cran = "convoSPAT" 

	version("1.2.7", md5="f950d23c1a06d1ef9b02f0b8fdc6e58a")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-statmatch", type=("build", "run"))
