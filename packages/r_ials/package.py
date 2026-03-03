# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIals(RPackage):
	"""Iterative Alternating Least Square Estimation for
Large-Dimensional Matrix Factor Model

	The matrix factor model has drawn growing attention for its advantage in achieving two-directional dimension reduction simultaneously for matrix-structured observations. In contrast to the Principal Component Analysis (PCA)-based methods, we propose a simple Iterative Alternating Least Squares (IALS) algorithm for matrix factor model, see the details in He et al. (2023) <arXiv:2301.00360>.
	"""
	
	cran = "IALS" 

	version("0.1.3", md5="d4ef80c52e02b717141308fdaf9269d3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-hdmfa", type=("build", "run"))
