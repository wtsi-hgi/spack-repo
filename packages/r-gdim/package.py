# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdim(RPackage):
	"""Estimate Graph Dimension using Cross-Validated Eigenvalues

	Cross-validated eigenvalues are estimated by
    splitting a graph into two parts, the training and the test graph.
    The training graph is used to estimate eigenvectors, and
    the test graph is used to evaluate the correlation between the training
    eigenvectors and the eigenvectors of the test graph.
    The correlations follow a simple central limit theorem that can
    be used to estimate graph dimension via hypothesis testing, see
    Chen et al. (2021) <arXiv:2108.03336> for details.
	"""
	
	homepage = "https://github.com/RoheLab/gdim"
	cran = "gdim" 

	version("0.1.0", md5="36c395e9e12190a6a240180f0f51768a")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
