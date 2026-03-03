# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKcmeans(RPackage):
	"""Conditional Expectation Function Estimation with
K-Conditional-Means

	Implementation of the KCMeans regression estimator studied by 
    Wiemann (2023) <arXiv:2311.17021> for expectation function estimation conditional on 
    categorical variables. Computation leverages the unconditional KMeans 
    implementation in one dimension using dynamic programming algorithm of
    Wang and Song (2011) <doi:10.32614/RJ-2011-015>, allowing for global solutions in time polynomial in 
    the number of observed categories.
	"""
	
	homepage = "https://github.com/thomaswiemann/kcmeans"
	cran = "kcmeans" 

	version("0.1.0", md5="66b766db9404367d18298c45c91e78f1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
