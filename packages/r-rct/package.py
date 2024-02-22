# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRct(RPackage):
	"""Assign Treatments, Power Calculations, Balances, Impact
Evaluation of Experiments

	Assists in the whole process of designing and evaluating Randomized Control Trials.
    Robust treatment assignment by strata/blocks, that handles misfits; 
    Power calculations of the minimum detectable treatment effect or minimum populations;
    Balance tables of T-test of covariates; 
    Balance Regression: (treatment ~ all x variables) with F-test of null model; 
    Impact_evaluation: Impact evaluation regressions. This function
    gives you the option to include control_vars, fixed effect variables,
    cluster variables (for robust SE), multiple endogenous variables and
    multiple heterogeneous variables (to test treatment effect heterogeneity)
    summary_statistics: Function that creates a summary statistics table with statistics 
    rank observations in n groups: Creates a factor variable with n groups. Each group has 
    a min and max label attach to each category.
    Athey, Susan, and Guido W. Imbens (2017) <arXiv:1607.00698>.
	"""
	
	cran = "RCT" 

	version("1.2", md5="dceb0c629407b1737278dab0db6e9899")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-estimatr", type=("build", "run"))
	depends_on("r-broom@1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
