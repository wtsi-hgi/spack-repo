# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvinecopulib(RPackage):
	"""High Performance Algorithms for Vine Copula Modeling

	Provides an interface to 'vinecopulib', a C++ library for vine 
 copula modeling. The 'rvinecopulib' package implements the core features of the
 popular 'VineCopula' package, in particular inference algorithms for both vine 
 copula and bivariate copula models. Advantages over 'VineCopula' are a sleeker 
 and more modern API, improved performances, especially in high dimensions, 
 nonparametric and multi-parameter families, and the ability to model discrete 
 variables. The 'rvinecopulib' package includes 'vinecopulib' as header-only 
 C++ library (currently version 0.6.2). Thus users do not need to install 
 'vinecopulib' itself in order to use 'rvinecopulib'. Since their initial 
 releases, 'vinecopulib' is licensed under the MIT License, and 'rvinecopulib' 
 is licensed under the GNU GPL version 3.
	"""
	
	cran = "rvinecopulib" 

	version("0.6.3.1.1", md5="a4b38ea99d4a5a6dc167a34b84028b15")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-kde1d", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppthread@2.1.2:", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
