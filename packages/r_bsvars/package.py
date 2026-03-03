# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsvars(RPackage):
	"""Bayesian Estimation of Structural Vector Autoregressive Models

	Efficient algorithms for Bayesian estimation of Structural Vector Autoregressive (SVAR) models via Markov chain Monte Carlo methods. A wide range of SVAR models is considered, including homo- and heteroskedastic specifications and those with non-normal structural shocks. The heteroskedastic SVAR model setup is similar as in Woźniak & Droumaguet (2015) <doi:10.13140/RG.2.2.19492.55687> and Lütkepohl & Woźniak (2020) <doi:10.1016/j.jedc.2020.103862>. The sampler of the structural matrix follows Waggoner & Zha (2003) <doi:10.1016/S0165-1889(02)00168-9>, whereas that for autoregressive parameters follows Chan, Koop, Yu (2022) <https://www.joshuachan.org/papers/OISV.pdf>. The specification of Markov switching heteroskedasticity is inspired by Song & Woźniak (2021) <doi:10.1093/acrefore/9780190625979.013.174>, and that of Stochastic Volatility model by Kastner & Frühwirth-Schnatter (2014) <doi:10.1016/j.csda.2013.01.002>.
	"""
	
	homepage = "https://bsvars.github.io/bsvars/"
	cran = "bsvars" 

	version("2.1.0", md5="2d136b06fcd9673bcfb134473885c935")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcpptn", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stochvol", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
