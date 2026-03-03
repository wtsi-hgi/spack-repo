# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpmrob(RPackage):
	"""Robust Estimation of Probit Models with Endogeneity

	Package provides a set of tools for robust estimation and inference for probit model with endogenous covariates. The current version contains a robust two-step estimator. For technical details, see Naghi, Varadi and Zhelonkin (2022), <doi:10.1016/j.ecosta.2022.05.001>. 
	"""
	
	cran = "epmrob" 

	version("0.1", md5="e0f8032f81c416bf9101ffec67ed0c00")

	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
