# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRampath(RPackage):
	"""Structural Equation Modeling Using the Reticular Action Model
(RAM) Notation

	We rewrite of RAMpath software developed by John McArdle and Steven Boker as an R package. In addition to performing regular SEM analysis through the R package lavaan, RAMpath has unique features.  First, it can generate path diagrams according to a given model. Second, it can display path tracing rules through path diagrams and decompose total effects into their respective direct and indirect effects as well as decompose variance and covariance into individual bridges. Furthermore, RAMpath can fit dynamic system models automatically based on latent change scores and generate vector field plots based upon results obtained from a bivariate dynamic system. Starting version 0.4, RAMpath can conduct power analysis for both univariate and bivariate latent change score models.
	"""
	
	homepage = "https://nd.psychstat.org"
	cran = "RAMpath" 

	version("0.5.1", md5="60b69ce0018751c816b548120479e6b5")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
