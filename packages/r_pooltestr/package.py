# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPooltestr(RPackage):
	"""Prevalence and Regression for Pool-Tested (Group-Tested) Data

	An easy-to-use tool for working with presence/absence tests on 'pooled'
    or 'grouped' samples. The primary application is for estimating prevalence of 
    a marker in a population based on the results of tests on pooled specimens.
    This sampling method is often employed in surveillance of rare conditions in
    humans or animals (e.g. molecular xenomonitoring). The package was initially
    conceived as an R-based alternative to the molecular xenomonitoring software,
    'PoolScreen' <https://sites.uab.edu/statgenetics/software/>. However, it goes
    further, allowing for estimates of prevalence to be adjusted for hierarchical
    sampling frames, and perform flexible mixed-effect regression analyses
    (McLure et al. Environmental Modelling and Software.
    <DOI:10.1016/j.envsoft.2021.105158>). The package is currently in early stages,
    however more features are planned or in the works: e.g. adjustments for
    imperfect test specificity/sensitivity, functions for helping with optimal
    experimental design, and functions for spatial modelling.
	"""
	
	homepage = "https://github.com/AngusMcLure/PoolTestR"
	cran = "PoolTestR" 

	version("0.1.3", md5="6f5f267cf3128ce6a98161f58dfe3a65")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
