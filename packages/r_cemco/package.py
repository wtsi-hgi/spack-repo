# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCemco(RPackage):
	"""Fit 'CemCO' Algorithm

	'CemCO' algorithm, a model-based (Gaussian) clustering algorithm that removes/minimizes the effects of undesirable covariates during the clustering process both in cluster centroids and in cluster covariance structures (Relvas C. & Fujita A., (2020) <arXiv:2004.02333>).
	"""
	
	cran = "cemco" 

	version("0.2", md5="bf74bb2e5606a9413da0863aacffe968")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
