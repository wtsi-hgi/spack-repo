# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdavec(RPackage):
	"""Vector Summaries of Persistence Diagrams

	Tools for computing various vector summaries of persistence diagrams 
    studied in Topological Data Analysis. For improved computational efficiency, 
    all code for the vector summaries is written in 'C++' using the 'Rcpp' package.
	"""
	
	cran = "TDAvec" 

	version("0.1.3", md5="263d8b33321ef9bb6042196c2c0d3ab3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tda", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
