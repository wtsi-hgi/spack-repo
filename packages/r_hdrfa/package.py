# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdrfa(RPackage):
	"""High-Dimensional Robust Factor Analysis

	Factor models have been widely applied in areas such as economics and finance, and the well-known heavy-tailedness of macroeconomic/financial data should be taken into account when conducting factor analysis. We propose two algorithms to do robust factor analysis by considering the Huber loss. One is based on minimizing the Huber loss of the idiosyncratic error's L2 norm, which turns out to do Principal Component Analysis (PCA) on the weighted sample covariance matrix and thereby named as Huber PCA. The other one is based on minimizing the element-wise Huber loss, which can be solved by an iterative Huber regression algorithm. In this package we also provide the code for traditional PCA, the Robust Two Step (RTS) method by He et al. (2022) and the Quantile Factor Analysis (QFA) method by Chen et al. (2021) and He et al. (2023).
	"""
	
	cran = "HDRFA" 

	version("0.1.4", md5="87ec12d948a317b88cec5254ba877da0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
