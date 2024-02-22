# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShelf(RPackage):
	"""Tools to Support the Sheffield Elicitation Framework

	Implements various methods for eliciting a probability
    distribution for a single parameter from an expert or a group of
    experts. The expert provides a small number of probability judgements,
    corresponding to points on his or her cumulative distribution
    function. A range of parametric distributions can then be fitted and
    displayed, with feedback provided in the form of fitted probabilities
    and percentiles. For multiple experts, a weighted linear pool can be
    calculated. Also includes functions for eliciting beliefs about
    population distributions, eliciting multivariate distributions using a
    Gaussian copula, eliciting a Dirichlet distribution, and eliciting
    distributions for variance parameters in a random effects
    meta-analysis model. R Shiny apps for most of the methods are
    included.
	"""
	
	homepage = "https://github.com/OakleyJ/SHELF"
	cran = "SHELF" 

	version("1.9.0", md5="f445852e462c26ee2ad7304d64021455")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
