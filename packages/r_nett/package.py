# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNett(RPackage):
	"""Network Analysis and Community Detection

	Features tools for the network data analysis and community detection. 
    Provides multiple methods for fitting, model selection and goodness-of-fit testing in degree-corrected stochastic blocks models. 
    Most of the computations are fast and scalable for sparse networks, esp. for Poisson versions of the models.
    Implements the following: 
    Amini, Chen, Bickel and Levina (2013) <doi:10.1214/13-AOS1138>
    Bickel and Sarkar (2015) <doi:10.1111/rssb.12117>
    Lei (2016) <doi:10.1214/15-AOS1370>
    Wang and Bickel (2017) <doi:10.1214/16-AOS1457>
    Zhang and Amini (2020) <arXiv:2012.15047>
    Le and Levina (2022) <doi:10.1214/21-EJS1971>.
	"""
	
	homepage = "https://github.com/aaamini/nett"
	cran = "nett" 

	version("1.0.0", md5="c4320cd75c82ad4de3e5b1364bb2a044")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
