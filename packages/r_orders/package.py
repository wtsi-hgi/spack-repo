# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrders(RPackage):
	"""Sampling from k-th Order Statistics of New Families of
Distributions

	Set of tools to generate samples of k-th order statistics and others quantities of interest from new families of distributions. 
    The main references for this package are: C. Kleiber and S. Kotz (2003) Statistical size distributions in economics and actuarial sciences; Gentle, J. (2009), Computational Statistics, Springer-Verlag; 
    Naradajah, S. and Rocha, R. (2016), <DOI:10.18637/jss.v069.i10> and Stasinopoulos, M. and Rigby, R. (2015), <DOI:10.1111/j.1467-9876.2005.00510.x>.
    The families of distributions are: Benini distributions, Burr distributions, Dagum distributions, Feller-Pareto distributions, Generalized Pareto distributions, Inverse Pareto distributions, The Inverse Paralogistic distributions, Marshall-Olkin G distributions, exponentiated G distributions, beta G distributions, 
    gamma G distributions, Kumaraswamy G distributions, generalized beta G distributions, 
    beta extended G distributions, gamma G distributions, gamma uniform G distributions, beta exponential G distributions, Weibull G distributions, log gamma G I distributions, log gamma G II distributions, 
    exponentiated generalized G distributions, exponentiated Kumaraswamy G distributions, geometric exponential Poisson G distributions, truncated-exponential skew-symmetric G distributions, modified beta G distributions, 
    exponentiated exponential Poisson G distributions, Poisson-inverse gaussian distributions, Skew normal type 1 distributions, Skew student t distributions, Singh-Maddala distributions, Sinh-Arcsinh distributions, Sichel distributions, Zero inflated Poisson distributions. 
	"""
	
	cran = "orders" 

	version("0.1.8", md5="ea5959f5e5d4f4c6a26181146d1ec798")

	depends_on("r-newdistns", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
