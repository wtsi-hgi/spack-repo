# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsinteract(RPackage):
	"""Fast Searches for Interactions

	Performs fast detection of interactions in large-scale data using the
    method of random intersection trees introduced in
    Shah, R. D. and Meinshausen, N. (2014) <http://www.jmlr.org/papers/v15/shah14a.html>. 
    The algorithm finds potentially high-order interactions in high-dimensional binary
    two-class classification data, without requiring lower order interactions
    to be informative.  The search is particularly fast when the matrices of
    predictors are sparse.  It can also be used to perform market basket analysis
    when supplied with a single binary data matrix.  Here it will find collections
    of columns which for many rows contain all 1's.
	"""
	
	homepage = "http://www.jmlr.org/papers/v15/shah14a.html"
	cran = "FSInteract" 

	version("0.1.2", md5="c6b371184c6dccbf19b11a765b28188c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
