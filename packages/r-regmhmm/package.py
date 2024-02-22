# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegmhmm(RPackage):
	"""'regmhmm' Fits Hidden Markov Models with Regularization

	Designed for longitudinal data analysis using Hidden Markov Models (HMMs). Tailored for applications in healthcare, social sciences, and economics, the main emphasis of this package is on regularization techniques for fitting HMMs. Additionally, it provides an implementation for fitting HMMs without regularization, referencing Zucchini et al. (2017, ISBN:9781315372488).
	"""
	
	homepage = "https://github.com/HenryLeongStat/regmhmm"
	cran = "regmhmm" 

	version("1.0.0", md5="9c18507886bd0ca2c15923eb717e6912")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-glmnetutils", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
