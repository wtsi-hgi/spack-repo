# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgm(RPackage):
	"""Advanced Inference with Random Graphical Models

	Implements state-of-the-art Random Graphical Models (RGMs) for multivariate data analysis across multiple environments, offering tools for exploring network interactions and structural relationships. Capabilities include joint inference across environments, integration of external covariates, and a Bayesian framework for uncertainty quantification. Applicable in various fields, including microbiome analysis. Methods based on Vinciotti, V., Wit, E., & Richter, F. (2023). "Random Graphical Model of Microbiome Interactions in Related Environments." <arXiv:2304.01956>.
	"""
	
	cran = "rgm" 

	version("1.0.3", md5="86d0b737069518aa97ebe51e64075418")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-bdgraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
