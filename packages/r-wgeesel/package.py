# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWgeesel(RPackage):
	"""Weighted Generalized Estimating Equations and Model Selection

	Weighted generalized estimating equations (WGEE) is an extension of generalized linear models to longitudinal clustered data by incorporating the correlation within-cluster when data is missing at random (MAR). The parameters in mean, scale correlation structures are estimated based on quasi-likelihood. Multiple model selection criterion are provided for selection of mean model and working correlation structure based on WGEE/GEE.
	"""
	
	cran = "wgeesel" 

	version("1.5", md5="4ecb0c512ed36b0f3a442017c8ad01ac")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-bindata", type=("build", "run"))
	depends_on("r-poisnor", type=("build", "run"))
	depends_on("r-crtgeedr", type=("build", "run"))
