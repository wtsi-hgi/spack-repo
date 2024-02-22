# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfba(RPackage):
	"""Distribution-Free Bayesian Analysis

	A set of functions to perform distribution-free Bayesian analyses. 
             Included are Bayesian analogues to the frequentist Mann-Whitney U 
             test, the Wilcoxon Signed-Ranks test, Kendall's Tau Rank 
             Correlation Coefficient, Goodman and Kruskal's Gamma, McNemar's
             Test, the binomial test, the sign test, the median test, as well as 
             distribution-free methods for testing contrasts among condition and 
             for computing Bayes factors for hypotheses. The package also
             includes procedures to estimate the power of distribution-free
             Bayesian tests based on data simulations using various probability 
             models for the data. The set of functions provide data analysts 
             with a set of Bayesian procedures that avoids requiring parametric 
             assumptions about measurement error and is robust to problem of 
             extreme outlier scores.
	"""
	
	cran = "DFBA" 

	version("0.1.0", md5="95271b65193650d50ea27705f59da6b6")

	depends_on("r@2.10:", type=("build", "run"))
