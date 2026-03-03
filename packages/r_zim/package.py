# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZim(RPackage):
	"""Zero-Inflated Models (ZIM) for Count Time Series with Excess
Zeros

	Analyze count time series with excess zeros. 
    Two types of statistical models are supported: Markov regression by Yang et al.
    (2013) <doi:10.1016/j.stamet.2013.02.001> and state-space models by Yang et al. 
    (2015) <doi:10.1177/1471082X14535530>. They are also known as observation-driven and 
    parameter-driven models respectively in the time series literature. The functions used for 
    Markov regression or observation-driven models can also be used to fit ordinary regression models 
    with independent data under the zero-inflated Poisson (ZIP) or zero-inflated negative binomial (ZINB) 
    assumption. Besides, the package contains some miscellaneous functions to compute density, distribution, 
    quantile, and generate random numbers from ZIP and ZINB distributions.
	"""
	
	homepage = "https://github.com/biostatstudio/ZIM"
	cran = "ZIM" 

	version("1.1.0", md5="f3a4edd2ac79ddc17ec273facc01b801")

	depends_on("r-mass", type=("build", "run"))
