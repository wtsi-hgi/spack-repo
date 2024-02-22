# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratifyr(RPackage):
	"""Optimal Stratification of Univariate Populations

	The stratification of univariate populations under stratified sampling designs is implemented according to Khan et al. (2002) <doi:10.1177/0008068320020518> and Khan et al. (2015) <doi:10.1080/02664763.2015.1018674> in this library. It determines the Optimum Strata Boundaries (OSB) and Optimum Sample Sizes (OSS) for the study variable, y, using the best-fit frequency distribution of a survey variable (if data is available) or a hypothetical distribution (if data is not available). The method formulates the problem of determining the OSB as mathematical programming problem which is solved by using a dynamic programming technique. If a dataset of the population is available to the surveyor, the method estimates its best-fit distribution and determines the OSB and OSS under Neyman allocation directly. When the dataset is not available, stratification is made based on the assumption that the values of the study variable, y, are available as hypothetical realizations of proxy values of y from recent surveys. Thus, it requires certain distributional assumptions about the study variable. At present, it handles stratification for the populations where the study variable follows a continuous distribution, namely, Pareto, Triangular, Right-triangular, Weibull, Gamma, Exponential, Uniform, Normal, Log-normal and Cauchy distributions. 
	"""
	
	cran = "stratifyR" 

	version("1.0-3", md5="3bf39bb82e8881e80c1a6efdf57062bb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-zipfr", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
