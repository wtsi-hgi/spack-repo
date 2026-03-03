# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsxtreme(RPackage):
	"""Bayesian Modelling of Extremal Dependence in Time Series

	Characterisation of the extremal dependence structure of time series, avoiding pre-processing and filtering as done typically with peaks-over-threshold methods. It uses the conditional approach of Heffernan and Tawn (2004) <DOI:10.1111/j.1467-9868.2004.02050.x> which is very flexible in terms of extremal and asymptotic dependence structures, and Bayesian methods improve efficiency and allow for deriving measures of uncertainty. For example, the extremal index, related to the size of clusters in time, can be estimated and samples from its posterior distribution obtained.
	"""
	
	cran = "tsxtreme" 

	version("0.3.3", md5="23b4d1b608826be80f325f5b4d310d76")

	depends_on("r-evd", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
