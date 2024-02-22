# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParty(RPackage):
	"""A Laboratory for Recursive Partytioning.

	A computational toolbox for recursive partitioning. The core of the package
	is ctree(), an implementation of conditional inference trees which embed
	tree-structured  regression models into a well defined theory of
	conditional inference procedures. This non-parametric class of regression
	trees is applicable to all kinds of regression problems, including nominal,
	ordinal, numeric, censored as well as multivariate response variables and
	arbitrary measurement scales of the covariates.  Based on conditional
	inference trees, cforest() provides an implementation of Breiman's random
	forests. The function mob() implements an algorithm for recursive
	partitioning based on parametric models (e.g. linear models, GLMs or
	survival regression) employing parameter instability tests for split
	selection. Extensible functionality for visualizing tree-structured
	regression models is available. The methods are described in Hothorn et al.
	(2006) <doi:10.1198/106186006X133933>, Zeileis et al. (2008)
	<doi:10.1198/106186008X319331> and  Strobl et al. (2007)
	<doi:10.1186/1471-2105-8-25>."""

	cran = "party"

	version("1.3-14", md5="cd2b68d326658acdc0d67a6c923042ce")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-modeltools@0.2.21:", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-survival@2.37.7:", type=("build", "run"))
	depends_on("r-coin@1.1.0:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-sandwich@1.1.1:", type=("build", "run"))
