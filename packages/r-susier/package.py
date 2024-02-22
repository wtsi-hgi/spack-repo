# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSusier(RPackage):
	"""Sum of Single Effects Linear Regression

	Implements methods for variable selection in linear
    regression based on the "Sum of Single Effects" (SuSiE) model, as
    described in Wang et al (2020) <DOI:10.1101/501114> and Zou et al
    (2021) <DOI:10.1101/2021.11.03.467167>. These methods provide
    simple summaries, called "Credible Sets", for accurately
    quantifying uncertainty in which variables should be selected.
    The methods are motivated by genetic fine-mapping applications,
    and are particularly well-suited to settings where variables are
    highly correlated and detectable effects are sparse. The fitting
    algorithm, a Bayesian analogue of stepwise selection methods
    called "Iterative Bayesian Stepwise Selection" (IBSS), is simple
    and fast, allowing the SuSiE model be fit to large data sets
    (thousands of samples and hundreds of thousands of variables).
	"""
	
	homepage = "https://github.com/stephenslab/susieR"
	cran = "susieR" 

	version("0.12.35", md5="fc23e4b323b0bf1df46818aae69ade3a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mixsqp", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
