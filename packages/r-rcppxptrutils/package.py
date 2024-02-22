# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppxptrutils(RPackage):
	"""XPtr Add-Ons for 'Rcpp'

	Provides the means to compile user-supplied C++ functions with
  'Rcpp' and retrieve an 'XPtr' that can be passed to other C++ components.
	"""
	
	homepage = "https://github.com/Enchufa2/RcppXPtrUtils"
	cran = "RcppXPtrUtils" 

	version("0.1.2", md5="3f646f0d2c93a5bfec9636a7e9b63c26")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
