# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REster(RPackage):
	"""Efficient Sequential Testing with Evidence Ratios

	An implementation of sequential testing that uses evidence ratios
    computed from the weights of a set of models. These weights correspond either
    to Akaike weights computed from the Akaike Information Criterion (AIC) or the
    Bayesian Information Criterion (BIC) and following Burnham & Anderson
    (2004, <doi:10.1177/0049124104268644>) recommendations, or to pseudo-BMA
    weights computed from the WAIC or the LOO-IC of models fitted
    with 'brms' and following Yao et al. (2017, <arXiv:1704.02030v3>).
	"""
	
	homepage = "https://github.com/lnalborczyk/ESTER"
	cran = "ESTER" 

	version("0.2.0", md5="ee29831edb4387c81ab2af631b65b645")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
