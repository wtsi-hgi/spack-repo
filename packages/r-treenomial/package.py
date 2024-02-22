# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreenomial(RPackage):
	"""Comparison of Trees using a Tree Defining Polynomial

	Provides functionality for creation and comparison of polynomials that uniquely
  describe trees as introduced in Liu (2019, <arXiv:1904.03332>). The core method
  converts rooted unlabeled phylo objects from 'ape' to the tree defining polynomials 
  described with coefficient matrices. Additionally, a conversion for rooted binary trees 
  with binary trait labels is also provided. Once the polynomials of trees are calculated 
  there are functions to calculate distances, distance matrices and plot different distance 
  trees from a target tree. Manipulation and conversion to the tree defining polynomials is 
  implemented in C++ with 'Rcpp' and 'RcppArmadillo'. Furthermore, parallel programming with 
  'RcppThread' is used to improve performance converting to polynomials and calculating distances. 
	"""
	
	homepage = "https://github.com/gouldmatt/treenomial"
	cran = "treenomial" 

	version("1.1.4", md5="eb2ccf6c75badbca391580bdc52e2f25")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppthread@2.1.3:", type=("build", "run"))
