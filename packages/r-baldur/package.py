# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaldur(RPackage):
	"""Bayesian Hierarchical Modeling for Label-Free Proteomics

	Statistical decision in proteomics data using a hierarchical
    Bayesian model. There are two regression models for describing the 
    mean-variance trend, a gamma regression or a latent gamma mixture
    regression. The regression model is then used as an Empirical Bayes
    estimator for the prior on the variance in a peptide. Further, it assumes
    that each measurement has an uncertainty (increased variance) associated
    with it that is also inferred. Finally, it tries to estimate the posterior
    distribution (by Hamiltonian Monte Carlo) for the differences in means for
    each peptide in the data. Once the posterior is inferred, it integrates the
    tails to estimate the probability of error from which a statistical decision
    can be made.
    See Berg and Popescu for details (<doi:10.1101/2023.05.11.540411>).
	"""
	
	homepage = "https://github.com/PhilipBerg/baldur"
	cran = "baldur" 

	version("0.0.3", md5="cad37c03e68bac36df5471ea0bb69836")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-stringr@1.0.4:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
	depends_on("r-multidplyr@0.1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-viridislite@0.4.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
