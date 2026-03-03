# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGinivarci(RPackage):
	"""Gini Indices, Variances and Confidence Intervals for Finite and
Infinite Populations

	Estimates the Gini index and computes variances and confidence intervals for finite and infinite populations, using different methods; also computes Gini index for continuous probability distributions, draws samples from continuous probability distributions with Gini indices set by the user; uses 'Rcpp'.
    References: 
    Muñoz et al. (2023) <doi:10.1177/00491241231176847>.
    Álvarez et al. (2021) <doi:10.3390/math9243252>.
    Giorgi and Gigliarano (2017) <doi:10.1111/joes.12185>.
    Langel and Tillé (2013) <doi:10.1111/j.1467-985X.2012.01048.x>.
	"""
	
	cran = "giniVarCI" 

	version("0.0.1-3", md5="215deaf624d6c980836722e2c2f42250")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
