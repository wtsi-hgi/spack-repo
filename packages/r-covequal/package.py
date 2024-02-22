# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovequal(RPackage):
	"""Test for Equality of Covariance Matrices

	Computes p-values using the largest root test using 
    an approximation to the null distribution by Johnstone (2008) <DOI:10.1214/08-AOS605>.
	"""
	
	homepage = "http://github.com/turgeonmaxime/covequal"
	cran = "covequal" 

	version("0.1.0", md5="fedfcdfe806836b93442af31e596cdf4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmtstat", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
