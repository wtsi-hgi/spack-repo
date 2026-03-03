# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcmodelsets(RPackage):
	"""Regression with a Large Number of Potential Explanatory
Variables

	Software for performing the reduction, exploratory and model selection phases of the procedure proposed by Cox, D.R. and Battey, H.S. (2017) <doi:10.1073/pnas.1703764114> for sparse regression when the number of potential explanatory variables far exceeds the sample size. The software supports linear regression, likelihood-based fitting of generalized linear regression models and the proportional hazards model fitted by partial likelihood.
	"""
	
	cran = "HCmodelSets" 

	version("1.1.3", md5="9edfbfd2af2a35fff4377df74bd7a0fe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
