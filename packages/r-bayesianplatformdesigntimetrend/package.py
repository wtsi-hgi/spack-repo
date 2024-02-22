# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianplatformdesigntimetrend(RPackage):
	"""Simulate and Analyse Bayesian Platform Trial with Time Trend

	Simulating the sequential multi-arm multi-stage or platform trial with Bayesian approach using the 'rstan' package, which provides the R interface for the Stan. 
    This package supports fixed ratio and Bayesian adaptive randomization approaches for randomization. 
    Additionally, it allows for the study of time trend problems in platform trials. 
    There are demos available for a multi-arm multi-stage trial with two different null scenarios, as well as for Bayesian trial cutoff screening.
    The Bayesian adaptive randomisation approaches are described in:
    Trippa et al. (2012) <doi:10.1200/JCO.2011.39.8420> and
    Wathen et al. (2017) <doi:10.1177/1740774517692302>.
    The randomisation algorithm is described in: 
    Zhao W <doi:10.1016/j.cct.2015.06.008>.
    The analysis methods of time trend effect in platform trial are described in:
    Saville et al. (2022) <doi:10.1177/17407745221112013> and
    Bofill Roig et al. (2022) <doi:10.1186/s12874-022-01683-w>.
	"""
	
	homepage = "https://github.com/ZXW834/BayesianPlatformDesignTimeTrend"
	cran = "BayesianPlatformDesignTimeTrend" 

	version("1.2.3", md5="cd9647e2938dfcbce277d10d9bf39441")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rstan@2.26.1:", type=("build", "run"))
	depends_on("r-biocmanager@1.30.19:", type=("build", "run"))
	depends_on("r-boot@1.3.28:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggpubr@0.4:", type=("build", "run"))
	depends_on("r-iterators@1.0.13:", type=("build", "run"))
	depends_on("r-lagp@1.5.9:", type=("build", "run"))
	depends_on("r-lhs@1.1.6:", type=("build", "run"))
	depends_on("r-matrixstats@0.61:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-reshape@0.8.8:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
