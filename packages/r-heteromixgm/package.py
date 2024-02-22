# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeteromixgm(RPackage):
	"""Copula Graphical Models for Heterogeneous Mixed Data

	A multi-core R package that allows for the statistical modeling of multi-group multivariate mixed data using Gaussian graphical models. Combining the Gaussian copula framework with the fused graphical lasso penalty, the 'heteromixgm' package can handle a wide variety of datasets found in various sciences. The package also includes an option to perform model selection using the AIC, BIC and EBIC information criteria, as well as simulate mixed heterogeneous data for exploratory or simulation purposes and one multi-group multivariate mixed agricultural dataset pertaining to maize yields. The package implements the methodological developments found in Hermes et al. (2022) <doi:10.48550/arXiv.2210.13140>.
	"""
	
	cran = "heteromixgm" 

	version("1.0.0", md5="b64bc125dfc7a4314bf2e44c80ac9af5")

	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-bdgraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
