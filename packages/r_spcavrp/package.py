# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcavrp(RPackage):
	"""Sparse Principal Component Analysis via Random Projections
(SPCAvRP)

	Implements the SPCAvRP algorithm, developed and analysed in "Sparse principal component analysis via random projections" Gataric, M., Wang, T. and Samworth, R. J. (2018) <arXiv:1712.05630>. The algorithm is based on the aggregation of eigenvector information from carefully-selected random projections of the sample covariance matrix.
	"""
	
	homepage = "https://arxiv.org/abs/1712.05630"
	cran = "SPCAvRP" 

	version("0.4", md5="e825a0ba7945b11bb833d9071ef08c04")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
