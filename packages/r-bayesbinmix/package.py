# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesbinmix(RPackage):
	"""Bayesian Estimation of Mixtures of Multivariate Bernoulli
Distributions

	Fully Bayesian inference for estimating the number of clusters and related parameters to heterogeneous binary data.
	"""
	
	cran = "BayesBinMix" 

	version("1.4.1", md5="a8d8af1607ba4ad14e318dbf4b9c26c5")

	depends_on("r-label-switching", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
