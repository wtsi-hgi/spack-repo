# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountts(RPackage):
	"""Thomson Sampling for Zero-Inflated Count Outcomes

	A specialized tool is designed for assessing contextual bandit algorithms, particularly those aimed at handling overdispersed and zero-inflated count data. It offers a simulated testing environment that includes various models like Poisson, Overdispersed Poisson, Zero-inflated Poisson, and Zero-inflated Overdispersed Poisson. The package is capable of executing five specific algorithms: Linear Thompson sampling with log transformation on the outcome, Thompson sampling Poisson, Thompson sampling Negative Binomial, Thompson sampling Zero-inflated Poisson, and Thompson sampling Zero-inflated Negative Binomial. Additionally, it can generate regret plots to evaluate the performance of contextual bandit algorithms. This package is based on the algorithms by Liu et al. (2023) <arXiv:2311.14359>.
	"""
	
	cran = "countts" 

	version("0.1.0", md5="1848b2a1b33d8727542c5dd028f0adbb")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
