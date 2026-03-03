# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsht(RPackage):
	"""Applied Statistical Hypothesis Tests

	Gives some hypothesis test functions (sign test, median and other quantile tests, Wilcoxon signed rank test, coefficient of variation test, test of normal variance, test on weighted sums of Poisson [see Fay and Kim <doi:10.1002/bimj.201600111>], sample size for t-tests with different variances and non-equal n per arm, Behrens-Fisher test, nonparametric ABC intervals, Wilcoxon-Mann-Whitney test [with effect estimates and confidence intervals, see Fay and Malinovsky <doi:10.1002/sim.7890>], two-sample melding tests [see Fay, Proschan, and Brittain <doi:10.1111/biom.12231>], one-way ANOVA allowing var.equal=FALSE [see Brown and Forsythe, 1974, Biometrics]), prevalence confidence intervals that adjust for sensitivity and specificity [see Lang and Reiczigel, 2014 <doi:10.1016/j.prevetmed.2013.09.015>] or Bayer, Fay, and Graubard, 2023 <doi:10.48550/arXiv.2205.13494>). The focus is on hypothesis tests that have compatible confidence intervals, but some functions only have confidence intervals (e.g., prevSeSp).
	"""
	
	cran = "asht" 

	version("1.0.1", md5="ba6e7268525f87b2eb843ceb7043fd74")

	depends_on("r-exact2x2@1.6.4:", type=("build", "run"))
	depends_on("r-exactci", type=("build", "run"))
	depends_on("r-bpcp", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-perm", type=("build", "run"))
	depends_on("r-ssanv", type=("build", "run"))
