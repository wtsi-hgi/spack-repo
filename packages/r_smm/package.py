# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmm(RPackage):
	"""Simulation and Estimation of Multi-State Discrete-Time
Semi-Markov and Markov Models

	Performs parametric and non-parametric estimation and simulation for multi-state discrete-time semi-Markov processes. 
	For the parametric estimation, several discrete distributions are considered for the sojourn times: Uniform, Geometric, Poisson, Discrete Weibull and Negative Binomial. The non-parametric estimation concerns the sojourn time distributions, where no assumptions are done on the shape of distributions. 
	Moreover, the estimation can be done on the basis of one or several sample paths, with or without censoring at the beginning or/and at the end of the sample paths. The implemented methods are described in Barbu, V.S., Limnios, N. (2008) <doi:10.1007/978-0-387-73173-5>, Barbu, V.S., Limnios, N. (2008) <doi:10.1080/10485250701261913> and 
	Trevezas, S., Limnios, N. (2011) <doi:10.1080/10485252.2011.555543>. 
	Estimation and simulation of discrete-time k-th order Markov chains are also considered.
	"""
	
	cran = "SMM" 

	version("1.0.2", md5="06028317767e848ffb489cdf1480eb19")

	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-discreteweibull", type=("build", "run"))
