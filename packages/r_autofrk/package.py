# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutofrk(RPackage):
	"""Automatic Fixed Rank Kriging

	Automatic fixed rank kriging for (irregularly located)
    spatial data using a class of basis functions with multi-resolution features
    and ordered in terms of their resolutions. The model parameters are estimated
    by maximum likelihood (ML) and the number of basis functions is determined
    by Akaike's information criterion (AIC). For spatial data with either one
    realization or independent replicates, the ML estimates and AIC are efficiently
    computed using their closed-form expressions when no missing value occurs. Details 
    regarding the basis function construction, parameter estimation, and AIC calculation  
    can be found in Tzeng and Huang (2018) <doi:10.1080/00401706.2017.1345701>. For
    data with missing values, the ML estimates are obtained using the expectation-
    maximization algorithm. Apart from the number of basis functions, there are
    no other tuning parameters, making the method fully automatic. Users can also
    include a stationary structure in the spatial covariance, which utilizes
    'LatticeKrig' package.
	"""
	
	cran = "autoFRK" 

	version("1.4.3", md5="22bb3ab9a93495842e7e51359672d746")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-fields@6.9.1:", type=("build", "run"))
	depends_on("r-filehashsqlite", type=("build", "run"))
	depends_on("r-filehash", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-latticekrig@5.4:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-filematrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
