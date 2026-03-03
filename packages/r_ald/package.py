# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAld(RPackage):
	"""The Asymmetric Laplace Distribution

	It provides the density, distribution function, quantile function, 
             random number generator, likelihood function, moments and Maximum Likelihood estimators for a given sample, all this for
             the three parameter Asymmetric Laplace Distribution defined 
             in Koenker and Machado (1999). This is a special case of the skewed family of distributions
             available in Galarza et.al. (2017) <doi:10.1002/sta4.140> useful for quantile regression. 
	"""
	
	cran = "ald" 

	version("1.3.1", md5="54c9f82920947c640196ff87df799b14")

