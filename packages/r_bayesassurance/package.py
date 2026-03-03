# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesassurance(RPackage):
	"""Bayesian Assurance Computation

	Computes Bayesian assurance under various 
    settings characterized by different assumptions and objectives, including 
    precision-based conditions, credible intervals, and goal functions. 
    All simulation-based functions included in this package rely on a two-stage 
    Bayesian method that assigns two distinct priors to evaluate the 
    probability of observing a positive outcome, which addresses subtle 
    limitations that take place when using the standard single-prior approach. 
    For more information, please refer to Pan and Banerjee (2021)
    <arXiv:2112.03509>.
	"""
	
	homepage = "https://github.com/jpan928/bayesassurance_rpackage"
	cran = "bayesassurance" 

	version("0.1.0", md5="b4cc4ab36e32d2673c1644835a9a5d05")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-plotly@4.10:", type=("build", "run"))
	depends_on("r-plot3d@1.4:", type=("build", "run"))
	depends_on("r-pbapply@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-mass@7.3.55:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-mathjaxr@1.5.2:", type=("build", "run"))
