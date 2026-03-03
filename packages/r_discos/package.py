# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscos(RPackage):
	"""Distributional Synthetic Controls Estimation

	The method of synthetic controls is a widely-adopted tool for evaluating causal effects of policy changes in settings with observational data. In many settings where it is applicable, researchers want to identify causal effects of policy changes on a treated unit at an aggregate level while having access to data at a finer granularity. This package implements a simple extension of the synthetic controls estimator, developed in Gunsilius (2023) <doi:10.3982/ECTA18260>, that takes advantage of this additional structure and provides nonparametric estimates of the heterogeneity within the aggregate unit. The idea is to replicate the quantile function associated with the treated unit by a weighted average of quantile functions of the control units. The package contains tools for aggregating and plotting the resulting distributional estimates, as well as for carrying out inference on them. 
	"""
	
	homepage = "<link"
	cran = "DiSCos" 

	version("0.0.1", md5="039424c137b09039917e11458efdbf0f")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-evmix", type=("build", "run"))
	depends_on("r-extremestat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
