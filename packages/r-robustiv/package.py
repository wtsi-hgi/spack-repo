# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustiv(RPackage):
	"""Robust Instrumental Variable Methods in Linear Models

	Inference for the treatment effect with possibly invalid instrumental variables via TSHT('Guo et al.' (2016) <arXiv:1603.05224>) and SearchingSampling('Guo' (2021) <arXiv:2104.06911>), which are effective for both low- and high-dimensional covariates and instrumental variables; test of endogeneity in high dimensions ('Guo et al.' (2016) <arXiv:1609.06713>).
	"""
	
	homepage = "https://github.com/zijguo/RobustIV"
	cran = "RobustIV" 

	version("0.2.5", md5="0401be69550bb920982dc8602ad252cb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-intervals", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
