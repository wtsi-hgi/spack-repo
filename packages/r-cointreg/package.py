# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCointreg(RPackage):
	"""Parameter Estimation and Inference in a Cointegrating Regression

	Cointegration methods are widely used in empirical macroeconomics
    and empirical finance. It is well known that in a cointegrating
    regression the ordinary least squares (OLS) estimator of the
    parameters is super-consistent, i.e. converges at rate equal to the
    sample size T. When the regressors are endogenous, the limiting
    distribution of the OLS estimator is contaminated by so-called second
    order bias terms, see e.g. Phillips and Hansen (1990) <DOI:10.2307/2297545>.
    The presence of these bias terms renders inference difficult. Consequently,
    several modifications to OLS that lead to zero mean Gaussian mixture
    limiting distributions have been proposed, which in turn make
    standard asymptotic inference feasible. These methods include
    the fully modified OLS (FM-OLS) approach of Phillips and Hansen
    (1990) <DOI:10.2307/2297545>, the dynamic OLS (D-OLS) approach of Phillips
    and Loretan (1991) <DOI:10.2307/2298004>, Saikkonen (1991)
    <DOI:10.1017/S0266466600004217> and Stock and Watson (1993)
    <DOI:10.2307/2951763> and the new estimation approach called integrated
    modified OLS (IM-OLS) of Vogelsang and Wagner (2014)
    <DOI:10.1016/j.jeconom.2013.10.015>. The latter is based on an augmented
    partial sum (integration) transformation of the regression model. IM-OLS is
    similar in spirit to the FM- and D-OLS approaches, with the key difference
    that it does not require estimation of long run variance matrices and avoids
    the need to choose tuning parameters (kernels, bandwidths, lags). However,
    inference does require that a long run variance be scaled out.
    This package provides functions for the parameter estimation and inference
    with all three modified OLS approaches. That includes the automatic
    bandwidth selection approaches of Andrews (1991) <DOI:10.2307/2938229> and
    of Newey and West (1994) <DOI:10.2307/2297912> as well as the calculation of
    the long run variance.
	"""
	
	homepage = "https://github.com/aschersleben/cointReg"
	cran = "cointReg" 

	version("0.2.0", md5="a1156d0f7113da88b75a947922494ce9")

	depends_on("r-checkmate@1.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats@0.14.1:", type=("build", "run"))
