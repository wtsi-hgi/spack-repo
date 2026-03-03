# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaehbPanel(RPackage):
	"""Small Area Estimation using Hierarchical Bayesian Method for Rao
Yu Model

	We designed this package to provide several functions for area level of small area estimation using hierarchical Bayesian (HB) method. This package provides model using panel data for variable interest.This package also provides a dataset produced by a data generation. The 'rjags' package is employed to obtain parameter estimates. Model-based estimators involves the HB estimators which include the mean and the variation of mean. For the reference, see Rao and Molina (2015).
	"""
	
	homepage = "https://github.com/Veliatrimarliana/saeHB.panel"
	cran = "saeHB.panel" 

	version("0.1.1", md5="a10d07d58244a6cd5fd8a3df0094b265")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
