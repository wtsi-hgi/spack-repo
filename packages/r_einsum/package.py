# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REinsum(RPackage):
	"""Einstein Summation

	The summation notation suggested by Einstein (1916) <doi:10.1002/andp.19163540702> is a 
  concise mathematical notation that implicitly sums over repeated indices of n-dimensional arrays. Many ordinary
  matrix operations (e.g. transpose, matrix multiplication, scalar product, 'diag()', trace etc.)
  can be written using Einstein notation. The notation is particularly convenient for 
  expressing operations on arrays with more than two dimensions because the 
  respective operators ('tensor products') might not have a standardized name.
	"""
	
	homepage = "https://const-ae.github.io/einsum/"
	cran = "einsum" 

	version("0.1.2", md5="c30828dbbf8b07fd8fb319f73caf2cdc")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
