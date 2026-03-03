# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProteobayes(RPackage):
	"""Bayesian Statistical Tools for Quantitative Proteomics

	Bayesian toolbox for quantitative proteomics. In particular, this 
    package provides functions to generate synthetic datasets, execute Bayesian
    differential analysis methods, and display results as, described in the 
    associated article Marie Chion and Arthur Leroy (2023) <arXiv:2307.08975>.
	"""
	
	homepage = "https://mariechion.github.io/ProteoBayes/"
	cran = "ProteoBayes" 

	version("1.0.0", md5="194f01555112e880ab21b1116dbb9693")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
