# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConf(RPackage):
	"""Visualization and Analysis of Statistical Measures of Confidence

	Enables: (1) plotting two-dimensional confidence regions, (2) coverage analysis
  of confidence region simulations, (3) calculating confidence intervals and the associated 
  actual coverage for binomial proportions, and (4) calculating the support values and the 
  probability mass function of the Kaplan-Meier product-limit estimator. Each is given in 
  greater detail next. 
  (1) Plots the two-dimensional confidence region for probability distribution parameters 
  (supported distribution suffixes: cauchy, gamma, invgauss, logis, llogis, lnorm, norm, unif, 
  weibull) corresponding to a user-given complete or right-censored dataset and level of 
  significance.  The crplot() algorithm plots more points in areas of greater curvature to 
  ensure a smooth appearance throughout the confidence region boundary.  An alternative 
  heuristic plots a specified number of points at roughly uniform intervals along its boundary. 
  Both heuristics build upon the radial profile log-likelihood ratio technique for plotting 
  confidence regions given by Jaeger (2016) <doi:10.1080/00031305.2016.1182946>, and
  are detailed in a publication by Weld et al. (2019) <doi:10.1080/00031305.2018.1564696>. 
  (2) Performs confidence region coverage simulations for a random sample drawn from a user-
  specified parametric population distribution, or for a user-specified dataset and point of 
  interest with coversim(). (3) Calculates confidence interval bounds for a binomial proportion 
  with binomTest(), calculates the actual coverage with binomTestCoverage(), and plots the 
  actual coverage with binomTestCoveragePlot(). Calculates confidence interval bounds for the
  binomial proportion using an ensemble of constituent confidence intervals with 
  binomTestEnsemble(). Calculates confidence interval bounds for the binomial proportion using 
  a complete enumeration of all possible transitions from one actual coverage acceptance curve 
  to another which minimizes the root mean square error for n <= 15 and follows the transitions 
  for well-known confidence intervals for n > 15 using binomTestMSE(). (4) The km.support() 
  function calculates the support values of the Kaplan-Meier product-limit estimator for a given 
  sample size n using an induction algorithm described in Qin et al. (2023) 
  <doi:10.1080/00031305.2022.2070279>. The km.outcomes() function generates a matrix 
  containing all possible outcomes (all possible sequences of failure times and right-censoring 
  times) of the value of the Kaplan-Meier product-limit estimator for a particular sample size 
  n. The km.pmf() function generates the probability mass function for the support values of 
  the Kaplan-Meier product-limit estimator for a particular sample size n, probability of 
  observing a failure h at the time of interest expressed as the cumulative probability 
  percentile associated with X = min(T, C), where T is the failure time and C is the censoring 
  time under a random-censoring scheme. The km.surv() function generates multiple probability 
  mass functions of the Kaplan-Meier product-limit estimator for the same arguments as those 
  given for km.pmf().
	"""
	
	cran = "conf" 

	version("1.8.3", md5="7ad3f95ecfd075e5152e8f8c80553ebc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
