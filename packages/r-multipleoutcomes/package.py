# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultipleoutcomes(RPackage):
	"""Asymptotic Covariance Matrix of Regression Models for Multiple
Outcomes

	Regression models can be fitted for multiple outcomes simultaneously. This package computes estimates of parameters across fitted models and returns the matrix of asymptotic covariance. Various applications of this package, including CUPED (Controlled Experiments Utilizing Pre-Experiment Data), multiple comparison adjustment, are illustrated. 
	"""
	
	cran = "multipleOutcomes" 

	version("0.2", md5="868546c10726ab8feefb228bb08c8268")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
