# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiosampler(RPackage):
	"""Biodiversity Index Calculation and Bootstrap Confidence Interval
Estimation

	Provides tools for the calculation of common biodiversity indices from count data. Additionally, it incorporates bootstrapping techniques to generate multiple samples, facilitating the estimation of confidence intervals around these indices. Furthermore, the package allows for the exploration of how variation in these indices changes with differing numbers of sites, making it a useful tool with which to begin an ecological analysis. Methods are based on the following references: Chao et al. (2014) <doi:10.1890/13-0133.1>, Chao and Colwell (2022) <doi:10.1002/9781119902911.ch2>, Hsieh, Ma,` and Chao (2016) <doi:10.1111/2041-210X.12613>.
	"""
	
	homepage = "https://github.com/csim063/biosampleR"
	cran = "biosampleR" 

	version("1.0.4", md5="f594a8b4068d30f9bdd7aa59cfe22e24")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
