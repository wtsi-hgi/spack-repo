# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExgaussestim(RPackage):
	"""Quantile Maximization Likelihood Estimation and Bayesian
Ex-Gaussian Estimation

	Presents two methods to estimate the parameters 'mu', 'sigma', and 'tau' of an ex-Gaussian distribution. Those methods are Quantile Maximization Likelihood Estimation ('QMLE') and Bayesian. The 'QMLE' method allows a choice between three different estimation algorithms for these parameters : 'neldermead' ('NEMD'), 'fminsearch' ('FMIN'), and 'nlminb' ('NLMI'). For more details about the methods you can refer at the following list: Brown, S., & Heathcote, A. (2003) <doi:10.3758/BF03195527>; McCormack, P. D., & Wright, N. M. (1964) <doi:10.1037/h0083285>; Van Zandt, T. (2000) <doi:10.3758/BF03214357>; El Haj, A., Slaoui, Y., Solier, C., & Perret, C. (2021) <doi:10.19139/soic-2310-5070-1251>; Gilks, W. R., Best, N. G., & Tan, K. K. C. (1995) <doi:10.2307/2986138>.
	"""
	
	cran = "ExGaussEstim" 

	version("0.1.2", md5="1e392fdd964478dc95990a98cf1650d4")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
