# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstimatew(RPackage):
	"""Estimation of Spatial Weight Matrices

	Bayesian estimation of spatial weight matrices in spatial econometric panel models. Allows for estimation of spatial autoregressive (SAR), spatial Durbin (SDM), and spatially lagged explanatory variable (SLX) type specifications featuring an unknown spatial weight matrix. Methodological details are given in Krisztin and Piribauer (2022) <doi:10.1080/17421772.2022.2095426>.
	"""
	
	cran = "estimateW" 

	version("0.0.1", md5="5b182302c6968e9581c5fa5353dee735")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-plot-matrix", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
