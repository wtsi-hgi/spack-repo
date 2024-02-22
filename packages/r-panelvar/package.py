# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelvar(RPackage):
	"""Panel Vector Autoregression

	We extend two general methods of moment estimators to panel vector 
    autoregression models (PVAR) with p lags of endogenous variables, predetermined 
    and strictly exogenous variables. This general PVAR model contains the first 
    difference GMM estimator by Holtz-Eakin et al. (1988) <doi:10.2307/1913103>, 
    Arellano and Bond (1991) <doi:10.2307/2297968> and the system GMM estimator 
    by Blundell and Bond (1998) <doi:10.1016/S0304-4076(98)00009-8>. We also 
    provide specification tests (Hansen overidentification test, lag selection 
    criterion and stability test of the PVAR polynomial) and classical structural 
    analysis for PVAR models such as orthogonal and generalized impulse response 
    functions, bootstrapped confidence intervals for impulse response analysis and 
    forecast error variance decompositions.
	"""
	
	cran = "panelvar" 

	version("0.5.5", md5="841d7f28f429f6024e6ce2b02aa8f8ee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.2.11:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
