# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsynchlong(RPackage):
	"""Regression Analysis of Sparse Asynchronous Longitudinal Data

	Estimation of regression models for sparse asynchronous 
    longitudinal observations, where time-dependent response and covariates 
    are mismatched and observed intermittently within subjects. Kernel 
    weighted estimating equations are used for generalized linear models 
    with either time-invariant or time-dependent coefficients. Cao, H.,
    Li, J., and Fine, J. P. (2016) <doi:10.1214/16-EJS1141>. Cao, H., 
    Zeng, D., and Fine, J. P. (2015) <doi:10.1111/rssb.12086>.
	"""
	
	cran = "AsynchLong" 

	version("2.3", md5="577e83599a2ca2fe997855b1c83a2d70")

