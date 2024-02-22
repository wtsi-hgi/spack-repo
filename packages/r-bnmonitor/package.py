# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnmonitor(RPackage):
	"""An Implementation of Sensitivity Analysis in Bayesian Networks

	An implementation of sensitivity and robustness methods in Bayesian networks in R. It includes methods to perform parameter variations via a variety of co-variation schemes, to compute sensitivity functions and to quantify the dissimilarity of two Bayesian networks via distances and divergences. It further includes diagnostic methods to assess the goodness of fit of a Bayesian networks to data, including global, node and parent-child monitors. References: H. Chan, A. Darwiche (2002) <doi:10.1613/jair.967>; C. Goergen, M. Leonelli (2020) <ArXiv:1809.10794>; M. Leonelli, R. Ramanathan, R.L. Wilkerson (2021) <ArXiv:2107.11785>. 
	"""
	
	homepage = "https://manueleleonelli.github.io/bnmonitor/"
	cran = "bnmonitor" 

	version("0.1.4", md5="b582cd11821202dcd7b4b4010e85d8c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-grain", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
