# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBuysetest(RPackage):
	"""Generalized Pairwise Comparisons

	Implementation of the Generalized Pairwise Comparisons (GPC) as defined in Buyse (2010) <doi:10.1002/sim.3923> for complete observations, and extended in Peron (2018) <doi:10.1177/0962280216658320> to deal with right-censoring. GPC compare two groups of observations (intervention vs. control group) regarding several prioritized endpoints to estimate the probability that a random observation drawn from one group performs better than a random observation drawn from the other group (Mann-Whitney parameter). The net benefit and win ratio statistics, i.e. the difference and ratio between the probabilities relative to the intervention and control groups, can then also be estimated. Confidence intervals and p-values are obtained based on asymptotic results (Ozenne 2021 <doi:10.1177/09622802211037067>), non-parametric bootstrap, or permutations. The software enables the use of thresholds of minimal importance difference, stratification, non-prioritized endpoints (O Brien test), and can handle right-censoring and competing-risks.
	"""
	
	homepage = "https://github.com/bozenne/BuyseTest"
	cran = "BuyseTest" 

	version("3.0.2", md5="2a71d8189f74ec50c4f8516d2240a200")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lava", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-riskregression", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
