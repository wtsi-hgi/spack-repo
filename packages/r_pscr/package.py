# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPscr(RPackage):
	"""Estimation for the Power Series Cure Rate Model

	Provide estimation for particular cases of the power series cure rate model 
             <doi:10.1080/03610918.2011.639971>. For the distribution of the concurrent causes the 
             alternative models are the Poisson, logarithmic, negative binomial and Bernoulli (which 
             are includes in the original work), the polylogarithm model 
             <doi:10.1080/00949655.2018.1451850> and the Flory-Schulz <doi:10.3390/math10244643>. 
             The estimation procedure is based on the EM algorithm discussed in 
             <doi:10.1080/03610918.2016.1202276>.
             For the distribution of the time-to-event the alternative models are slash half-normal, 
             Weibull, gamma and Birnbaum-Saunders distributions.
	"""
	
	cran = "PScr" 

	version("1.1", md5="7136e86bbb39610dc1db5824110759b1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
