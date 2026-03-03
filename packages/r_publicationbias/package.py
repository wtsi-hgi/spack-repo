# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPublicationbias(RPackage):
	"""Sensitivity Analysis for Publication Bias in Meta-Analyses

	Performs sensitivity analysis for publication bias in meta-analyses
    (per Mathur & VanderWeele, 2020 [<doi:10.31219/osf.io/s9dp6>]). These analyses
    enable statements such as: "For publication bias to shift the observed point
    estimate to the null, 'significant' results would need to be at least
    30-fold more likely to be published than negative or 'nonsignificant'
    results." Comparable statements can be made regarding shifting to a chosen
    non-null value or shifting the confidence interval. Provides a worst-case
    meta-analytic point estimate under maximal publication bias obtained simply
    by conducting a standard meta-analysis of only the negative and
    "nonsignificant" studies.
	"""
	
	homepage = "https://github.com/mathurlabstanford/PublicationBias"
	cran = "PublicationBias" 

	version("2.4.0", md5="638e060b38fb83832e34fb9baa8cfab2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-metabias", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-robumeta", type=("build", "run"))
