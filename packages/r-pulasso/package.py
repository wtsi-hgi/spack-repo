# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPulasso(RPackage):
	"""High-Dimensional Variable Selection with Presence-Only Data

	Efficient algorithm for solving PU (Positive and Unlabeled) problem in low or high dimensional setting with lasso or group lasso penalty. The algorithm uses Maximization-Minorization and (block) coordinate descent. Sparse calculation and parallel computing are supported for the computational speed-up. See Hyebin Song, Garvesh Raskutti (2018) <arXiv:1711.08129>.
	"""
	
	homepage = "https://arxiv.org/abs/1711.08129"
	cran = "PUlasso" 

	version("3.2.5", md5="0a24fe82eba16ba59a0712ba63dadc85")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
