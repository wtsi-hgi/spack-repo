# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicefast(RPackage):
	"""Fast Imputations Using 'Rcpp' and 'Armadillo'

	
  Fast imputations under the object-oriented programming paradigm. 	
  Moreover there are offered a few functions built to work with popular R packages such as 'data.table' or 'dplyr'.
  The biggest improvement in time performance could be achieve for a calculation where a grouping variable have to be used.
  A single evaluation of a quantitative model for the multiple imputations is another major enhancement.
  A new major improvement is one of the fastest predictive mean matching in the R world because of presorting and binary search.
	"""
	
	homepage = "https://github.com/Polkas/miceFast"
	cran = "miceFast" 

	version("0.8.2", md5="f0fec87a5224b10d929803ee99762164")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
