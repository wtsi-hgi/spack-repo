# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulttest(RPackage):
	"""Resampling-based multiple hypothesis testing.

	Non-parametric bootstrap and permutation resampling-based multiple
	testing procedures (including empirical Bayes methods) for controlling
	the family-wise error rate (FWER), generalized family-wise error rate
	(gFWER), tail probability of the proportion of false positives (TPPFP),
	and false discovery rate (FDR). Several choices of bootstrap-based null
	distribution are implemented (centered, centered and scaled, quantile-
	transformed). Single-step and step-wise methods are available. Tests
	based on a variety of t- and F-statistics (including t-statistics based
	on regression parameters from linear and survival models as well as
	those based on correlation parameters) are included. When probing
	hypotheses with t-statistics, users may also select a potentially faster
	null distribution which is multivariate normal with mean zero and
	variance covariance matrix derived from the vector influence function.
	Results are reported in terms of adjusted p-values, confidence regions
	and test statistic cutoffs. The procedures are directly applicable to
	identifying differentially expressed genes in DNA microarray
	experiments."""

	bioc = "multtest"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/multtest_2.58.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/multtest/multtest_2.58.0.tar.gz"]

	version("2.58.0", md5="7d81a8460781f4a86f01a9df5fcf50d7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
