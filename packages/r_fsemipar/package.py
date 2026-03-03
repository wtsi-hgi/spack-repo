# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsemipar(RPackage):
	"""Estimation, Variable Selection and Prediction for Functional
Semiparametric Models

	Routines for estimation or simultaneous estimation and variable selection of several functional semiparametric models with scalar response, such as the functional single-index model, the semi-functional partial linear model or the semi-functional partial linear single-index model. In addition, it includes algorithms for dealing with scalar covariates with linear effect coming from the discretization of a curve in the cases of the linear model, the multi-functional partial linear model and the multi-functional partial linear single-index model. 
	"""
	
	cran = "fsemipar" 

	version("1.0.1", md5="03fdae3fb0abb1ef9b134aefe128d708")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
