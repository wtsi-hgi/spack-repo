# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskparityportfolio(RPackage):
	"""Design of Risk Parity Portfolios

	Fast design of risk parity portfolios for financial investment.
    The goal of the risk parity portfolio formulation is to equalize or distribute
    the risk contributions of the different assets, which is missing if we simply
    consider the overall volatility of the portfolio as in the mean-variance
    Markowitz portfolio. In addition to the vanilla formulation, where the risk
    contributions are perfectly equalized subject to no shortselling and budget
    constraints, many other formulations are considered that allow for box
    constraints and shortselling, as well as the inclusion of additional
    objectives like the expected return and overall variance. See vignette for
    a detailed documentation and comparison, with several illustrative examples.
    The package is based on the papers:
    Y. Feng, and D. P. Palomar (2015). SCRIP: Successive Convex Optimization Methods
    for Risk Parity Portfolio Design. IEEE Trans. on Signal Processing, vol. 63,
    no. 19, pp. 5285-5300. <doi:10.1109/TSP.2015.2452219>.
    F. Spinu (2013), An Algorithm for Computing Risk Parity Weights.
    <doi:10.2139/ssrn.2297383>.
    T. Griveau-Billion, J. Richard, and T. Roncalli (2013). A fast algorithm for computing
    High-dimensional risk parity portfolios. <arXiv:1311.4057>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=riskParityPortfolio"
	cran = "riskParityPortfolio" 

	version("0.2.2", md5="df7c1c869f9c1eb209d9e55efc02d224")

	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
