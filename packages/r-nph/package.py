# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNph(RPackage):
	"""Planning and Analysing Survival Studies under Non-Proportional
Hazards

	Piecewise constant hazard functions are used to flexibly model survival distributions with non-proportional hazards and 
	to simulate data from the specified distributions. A function to calculate weighted log-rank tests for the comparison of two
	hazard functions is included. Also, a function to calculate a test using the maximum of a set of test statistics from weighted
	log-rank tests (MaxCombo test) is provided. This test utilizes the asymptotic multivariate normal joint distribution of the
	separate test statistics. The correlation is estimated from the data. These methods are described in Ristl et al. (2021) 
	<doi:10.1002/pst.2062>.
	Finally, a function is provided for the estimation and inferential statistics of various parameters that quantify the difference
	between two survival curves. Eligible parameters are differences in survival probabilities, log survival probabilities,
	complementary log log (cloglog) transformed survival probabilities, quantiles of the survival functions, log transformed quantiles,
	restricted mean survival times, as well as an average hazard ratio, the Cox model score statistic (logrank statistic), and the
	Cox-model hazard ratio. Adjustments for multiple testing and simultaneous confidence intervals are calculated using a multivariate
	normal approximation to the set of selected parameters.
	"""
	
	cran = "nph" 

	version("2.1", md5="aa0380aed5a7d42db216d2f0d237796b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-muhaz", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
