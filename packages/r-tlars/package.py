# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTlars(RPackage):
	"""The T-LARS Algorithm: Early-Terminated Forward Variable
Selection

	Computes the solution path of the Terminating-LARS (T-LARS) algorithm. The T-LARS algorithm 
    is a major building block of the T-Rex selector (see R package 'TRexSelector').
    The package is based on the papers Machkour, Muma, and Palomar (2022) <arXiv:2110.06048>, Efron, Hastie, Johnstone, 
    and Tibshirani (2004) <doi:10.1214/009053604000000067>, and Tibshirani (1996) <doi:10.1111/j.2517-6161.1996.tb02080.x>.
	"""
	
	homepage = "https://github.com/jasinmachkour/tlars"
	cran = "tlars" 

	version("1.0.1", md5="17f61641263a6a24a6271706b6f55252")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
