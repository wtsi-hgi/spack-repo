# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvpd(RPackage):
	"""Multivariate Product Distributions for Elliptically Contoured
Distributions

	Estimates multivariate subgaussian stable densities 
    and probabilities as well as generates random variates using product 
    distribution theory.  A function for estimating the parameters from 
    data to fit a distribution to data is also provided, using the 
    method from Nolan (2013) <doi:10.1007/s00180-013-0396-7>.
	"""
	
	homepage = "https://github.com/swihart/mvpd"
	cran = "mvpd" 

	version("0.0.4", md5="0d38d4d68589dceec313d9c34f6b566e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-stabledist", type=("build", "run"))
	depends_on("r-libstable4u", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
