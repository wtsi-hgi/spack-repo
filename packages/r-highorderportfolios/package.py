# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighorderportfolios(RPackage):
	"""Design of High-Order Portfolios Including Skewness and Kurtosis

	The classical Markowitz's mean-variance portfolio formulation ignores 
    heavy tails and skewness. High-order portfolios use higher order moments to
    better characterize the return distribution. Different formulations and fast 
    algorithms are proposed for high-order portfolios based on the mean, variance, 
    skewness, and kurtosis.
    The package is based on the papers:
    R. Zhou and D. P. Palomar (2021). "Solving High-Order Portfolios via 
    Successive Convex Approximation Algorithms." <arXiv:2008.00863>.
    X. Wang, R. Zhou, J. Ying, and D. P. Palomar (2022). "Efficient and Scalable 
    High-Order Portfolios Design via Parametric Skew-t Distribution." <arXiv:2206.02412>.
	"""
	
	homepage = "https://github.com/dppalomar/highOrderPortfolios"
	cran = "highOrderPortfolios" 

	version("0.1.1", md5="faf97e7ba0dd67de390a766935160dde")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ecosolver", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-fitheavytail@0.1.4:", type=("build", "run"))
