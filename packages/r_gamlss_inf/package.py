# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssInf(RPackage):
	"""Fitting Mixed (Inflated and Adjusted) Distributions

	This is an add-on package to 'gamlss'. The purpose of this package is to allow users to fit GAMLSS (Generalised Additive Models for Location Scale and Shape) models when the response variable is defined either in the intervals [0,1), (0,1] and [0,1] (inflated at zero and/or one distributions), or in the positive real line including zero (zero-adjusted distributions). The mass points at zero and/or one are treated as extra parameters with the possibility to include a linear predictor for both. The package also allows transformed or truncated distributions from the GAMLSS family to be used for the continuous part of the distribution. Standard methods and GAMLSS diagnostics can be used with the resulting fitted object. 
	"""
	
	homepage = "http://www.gamlss.com/"
	cran = "gamlss.inf" 

	version("1.0-1", md5="7568f8ce89f016acff72f6e4db227fa8")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
