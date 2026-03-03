# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodaBase(RPackage):
	"""A Basic Set of Functions for Compositional Data Analysis

	A minimum set of functions to perform compositional data analysis
    using the log-ratio approach introduced by John Aitchison (1982). Main functions
    have been implemented in c++ for better performance.
	"""
	
	homepage = "https://mcomas.net/coda.base/"
	cran = "coda.base" 

	version("0.5.5", md5="d409dc2b511a6a740dc20f76f2da4cae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
