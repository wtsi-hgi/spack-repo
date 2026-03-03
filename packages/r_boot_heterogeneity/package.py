# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootHeterogeneity(RPackage):
	"""A Bootstrap-Based Heterogeneity Test for Meta-Analysis

	Implements a bootstrap-based heterogeneity test for standardized mean differences (d), Fisher-transformed Pearson's correlations (r), and natural-logarithm-transformed odds ratio (or) in meta-analysis studies. Depending on the presence of moderators, this Monte Carlo based test can be implemented in the random- or mixed-effects model. This package uses rma() function from the R package 'metafor' to obtain parameter estimates and likelihoods, so installation of R package 'metafor' is required. This approach refers to the studies of Anscombe (1956) <doi:10.2307/2332926>, Haldane (1940) <doi:10.2307/2332614>, Hedges (1981) <doi:10.3102/10769986006002107>, Hedges & Olkin (1985, ISBN:978-0123363800), Silagy, Lancaster, Stead, Mant, & Fowler (2004) <doi:10.1002/14651858.CD000146.pub2>, Viechtbauer (2010) <doi:10.18637/jss.v036.i03>, and Zuckerman (1994, ISBN:978-0521432009). 
	"""
	
	homepage = "https://github.com/gabriellajg/boot.heterogeneity/"
	cran = "boot.heterogeneity" 

	version("1.1.5", md5="ed12b5311030a200a29db36e66de31f3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-hsaur3", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
