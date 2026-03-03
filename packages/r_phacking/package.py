# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhacking(RPackage):
	"""Sensitivity Analysis for p-Hacking in Meta-Analyses

	Fits right-truncated meta-analysis (RTMA), a bias correction for
  the joint effects of p-hacking (i.e., manipulation of results within studies
  to obtain significant, positive estimates) and traditional publication bias
  (i.e., the selective publication of studies with significant, positive
  results) in meta-analyses [see Mathur MB (2022). "Sensitivity analysis for
  p-hacking in meta-analyses." <doi:10.31219/osf.io/ezjsx>.]. Unlike publication
  bias alone, p-hacking that favors significant, positive results (termed
  "affirmative") can distort the distribution of affirmative results. To
  bias-correct results from affirmative studies would require strong assumptions
  on the exact nature of p-hacking. In contrast, joint p-hacking and publication
  bias do not distort the distribution of published nonaffirmative results when
  there is stringent p-hacking (e.g., investigators who hack always eventually
  obtain an affirmative result) or when there is stringent publication bias
  (e.g., nonaffirmative results from hacked studies are never published). This
  means that any published nonaffirmative results are from unhacked studies.
  Under these assumptions, RTMA involves analyzing only the published
  nonaffirmative results to essentially impute the full underlying distribution
  of all results prior to selection due to p-hacking and/or publication bias.
  The package also provides diagnostic plots described in Mathur (2022).
	"""
	
	homepage = "https://github.com/mathurlabstanford/phacking"
	cran = "phacking" 

	version("0.2.1", md5="d45c8a504f4d2292faaf860dea2c5a39")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metabias", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
