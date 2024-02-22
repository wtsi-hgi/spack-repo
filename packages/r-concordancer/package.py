# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcordancer(RPackage):
	"""An 'Rcpp' Implementation of Lin's Concordance Correlation
Coefficient (CCC)

	Lin's Concordance Correlation Coefficient (CCC) is a statistic 
  which measures the degree of agreement between two variables. The CCC is 
  useful for assessing (i) the measurement agreement between two variables 
  (typically outputs between two devices); (ii) the reproducibility between 
  two measurements obtained from the same device; and (iii) inter-rater 
  reliability. The 'concordancer' package provides a 'C++' implementation of 
  Lin's CCC via 'Rcpp'. In so doing, the ccc() function contained herein is 
  a much faster implementation than those contained in other R packages. For
  more details on Lin's CCC, please see <https://en.wikipedia.org/wiki/Concordance_correlation_coefficient>.
	"""
	
	homepage = "https://github.com/troyjcross/concordancer"
	cran = "concordancer" 

	version("1.0.2", md5="c2dd8a287a7365f8ed497b92311d9bc0")

	depends_on("r-rcpp", type=("build", "run"))
