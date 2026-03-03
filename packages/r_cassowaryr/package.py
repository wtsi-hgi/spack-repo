# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCassowaryr(RPackage):
	"""Compute Scagnostics on Pairs of Numeric Variables in a Data Set

	Computes a range of scatterplot diagnostics (scagnostics) on pairs
  of numerical variables in a data set. A range of scagnostics, including graph
  and association-based scagnostics described by Leland Wilkinson and Graham
  Wills (2008) <doi:10.1198/106186008X320465> and association-based
  scagnostics described by Katrin Grimm (2016,ISBN:978-3-8439-3092-5) can be 
  computed. Summary and plotting functions are provided.
	"""
	
	homepage = "https://github.com/numbats/cassowaryr"
	cran = "cassowaryr" 

	version("2.0.0", md5="ae8be2debe4553c9063b93a075ad6330")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-alphahull@2.5:", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
