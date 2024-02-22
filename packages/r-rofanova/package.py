# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRofanova(RPackage):
	"""Robust Functional Analysis of Variance

	Implements the robust functional analysis of variance (RoFANOVA), described in Centofanti et al. (2021) <arXiv:2112.10643>. 
    It allows testing mean differences among groups of  functional data by being robust against the presence of outliers.
	"""
	
	homepage = "https://github.com/unina-sfere/rofanova"
	cran = "rofanova" 

	version("1.0.0", md5="9856e13e57b6cc552bd13c5ac4a10029")

	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
