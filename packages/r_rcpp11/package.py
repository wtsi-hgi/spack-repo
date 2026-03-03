# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpp11(RPackage):
	"""R and C++11

	Rcpp11 includes a header only C++11 library that facilitates 
  integration between R and modern C++. 
	"""
	
	cran = "Rcpp11" 

	version("3.1.2.0.1", md5="a6f73c04f4fe896e1b3fed5e5f5cbd52", url="https://cran.r-project.org/src/contrib/Rcpp11_3.1.2.0.1.tar.gz")

	depends_on("r@3.1.2:", type=("build", "run"))
