# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAep(RPackage):
	"""Statistical Modelling for Asymmetric Exponential Power
Distribution

	Developed for Computing the probability density function, cumulative 
             distribution function, random generation, estimating the parameters of asymmetric
             exponential power distribution, and robust regression analysis with error
             term that follows asymmetric exponential power distribution. The asymmetric
             exponential power distribution studied here is a special case of that introduced
             by Dongming and Zinde-Walsh (2009) <doi:10.1016/j.jeconom.2008.09.038>.
	"""
	
	cran = "AEP" 

	version("0.1.4", md5="a6cda9b21dbc2b294d6454c4ab0cbf70")

	depends_on("r@3.3:", type=("build", "run"))
