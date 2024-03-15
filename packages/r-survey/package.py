# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvey(RPackage):
	"""Analysis of Complex Survey Samples.

	Summary statistics, two-sample tests, rank tests, generalised linear
	models, cumulative link models, Cox models, loglinear models, and general
	maximum pseudolikelihood estimation for multistage stratified,
	cluster-sampled, unequally weighted survey samples. Variances by Taylor
	series linearisation or replicate weights. Post-stratification,
	calibration, and raking. Two-phase subsampling designs. Graphics. PPS
	sampling without replacement. Principal components, factor analysis."""

	cran = "survey"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("4.4-1", md5="06574ba74a051c98255e363584da7a36")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mitools@2.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
