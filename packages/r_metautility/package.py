# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetautility(RPackage):
	"""Utility Functions for Conducting and Interpreting Meta-Analyses

	Contains functions to estimate the proportion of effects stronger than a threshold
    of scientific importance (function prop_stronger), to nonparametrically characterize the distribution of effects in a meta-analysis (calib_ests, pct_pval),
    to make effect size conversions (r_to_d, r_to_z, z_to_r, d_to_logRR), to compute and format inference in a meta-analysis (format_CI, format_stat, tau_CI), to scrape results from 
    existing meta-analyses for re-analysis (scrape_meta, parse_CI_string, ci_to_var).
	"""
	
	cran = "MetaUtility" 

	version("2.1.2", md5="74d80acb2117fe045e57545ba831fa50")

	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-metadat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
