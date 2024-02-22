# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCluspred(RPackage):
	"""Simultaneous Semi-Parametric Estimation of Clustering and
Regression

	Parameter estimation of regression models with fixed group effects, when the group variable is missing while group-related variables are available. Parametric and semi-parametric approaches described in Marbac et al. (2020) <arXiv:2012.14159> are implemented.
	"""
	
	homepage = "https://arxiv.org/abs/2012.14159"
	cran = "ClusPred" 

	version("1.1.0", md5="36d265f4042ec5e8b5ce71645e5b81f9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-aldqr", type=("build", "run"))
	depends_on("r-ald", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
