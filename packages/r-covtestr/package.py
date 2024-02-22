# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovtestr(RPackage):
	"""Covariance Matrix Tests

	Testing functions for Covariance Matrices. These tests include high-dimension homogeneity of covariance
  matrix testing described by Schott (2007) <doi:10.1016/j.csda.2007.03.004> and high-dimensional one-sample tests of 
  covariance matrix structure described by Fisher, et al. (2010) <doi:10.1016/j.jmva.2010.07.004>. Covariance matrix
  tests use C++ to speed performance and allow larger data sets.
	"""
	
	homepage = "https://covtestr.bearstatistics.com"
	cran = "covTestR" 

	version("0.1.4", md5="f8b25feada8b560333d7f2dab7a97fe5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
