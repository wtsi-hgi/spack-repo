# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdmfa(RPackage):
	"""High-Dimensional Matrix Factor Analysis

	High-dimensional matrix factor models have drawn much attention in view of the fact that observations are usually well structured to be an array such as in macroeconomics and finance. In addition, data often exhibit heavy-tails and thus it is also important to develop robust procedures. We aim to address this issue by replacing the least square loss with Huber loss function. We propose two algorithms to do robust factor analysis by considering the Huber loss. One is based on minimizing the Huber loss of the idiosyncratic error's Frobenius norm, which leads to a weighted iterative projection approach to compute and learn the parameters and thereby named as Robust-Matrix-Factor-Analysis (RMFA), see the details in He et al. (2023)<doi:10.1080/07350015.2023.2191676>. The other one is based on minimizing the element-wise Huber loss, which can be solved by an iterative Huber regression algorithm (IHR), see the details in He et al. (2023) <arXiv:2306.03317>. In this package, we also provide the algorithm for alpha-PCA by Chen & Fan (2021) <doi:10.1080/01621459.2021.1970569>, the Projected estimation (PE) method by Yu et al. (2022)<doi:10.1016/j.jeconom.2021.04.001>. In addition, the methods for determining the pair of factor numbers are also given.
	"""
	
	cran = "HDMFA" 

	version("0.1.1", md5="6d207e0091c960ed478e497ce5037d15")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
