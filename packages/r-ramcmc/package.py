# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamcmc(RPackage):
	"""Robust Adaptive Metropolis Algorithm

	Function for adapting the shape of the random walk Metropolis proposal
    as specified by robust adaptive Metropolis algorithm by Vihola (2012) <doi:10.1007/s11222-011-9269-5>. 
    The package also includes fast functions for rank-one Cholesky update and downdate.
    These functions can be used directly from R or the corresponding C++ header files 
    can be easily linked to other R packages.
	"""
	
	cran = "ramcmc" 

	version("0.1.2", md5="30fee64ea786fecf9a8cd9446f5c8a89")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
