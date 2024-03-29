# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcHeterogeneity(RPackage):
	"""A Monte Carlo Based Heterogeneity Test for Meta-Analysis

	Implements a Monte Carlo Based Heterogeneity Test for standardized mean differences (d), Fisher-transformed Pearson's correlations (r), and natural-logarithm-transformed odds ratio (OR) in Meta-Analysis Studies. Depending on the presence of moderators, this Monte Carlo Based Test can be implemented in the random or mixed-effects model. This package uses rma() function from the R package 'metafor' to obtain parameter estimates and likelihood, so installation of R package 'metafor' is required. This approach refers to the studies of Hedges (1981) <doi:10.3102/10769986006002107>, Hedges & Olkin (1985, ISBN:978-0123363800), Silagy, Lancaster, Stead, Mant, & Fowler (2004) <doi:10.1002/14651858.CD000146.pub2>, Viechtbauer (2010) <doi:10.18637/jss.v036.i03>, and Zuckerman (1994, ISBN:978-0521432009).
	"""
	
	cran = "mc.heterogeneity" 

	version("0.1.2", md5="786a8333a3752f4944812a94c014d39c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-boot-heterogeneity", type=("build", "run"))
