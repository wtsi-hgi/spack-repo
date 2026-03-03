# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountdm(RPackage):
	"""Estimation of Count Data Models

	The maximum likelihood estimation (MLE) of the count data models along with standard error of the estimates and Akaike information model section criterion are provided. The functions allow to compute the MLE for the following distributions such as the Bell distribution, the Borel distribution, the Poisson distribution, zero inflated Bell distribution, zero inflated Bell Touchard distribution, zero inflated Poisson distribution, zero one inflated Bell distribution and zero one inflated Poisson distribution. Moreover, the probability mass function (PMF), distribution function (CDF), quantile function (QF) and random numbers generation of the Bell Touchard and zero inflated Bell Touchard distribution are also provided. 
	"""
	
	cran = "countDM" 

	version("0.1.0", md5="c6945709c26c067d9870266345a316c7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lamw", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
