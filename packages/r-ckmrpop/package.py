# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCkmrpop(RPackage):
	"""Forward-in-Time Simulation and Tallying of Pairwise
Relationships

	Provides an R wrapper around the program 'spip'
    (<https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1471-8286.2005.00884.x>), a C
    program for the simulation of pedigrees within age-structured populations
    with user-specified life histories.  Also includes a variety
    of functions to parse 'spip' output to compile information about
    related pairs amongst simulated, sampled individuals, to assess
    the feasibility and potential accuracy of close-kin mark-recapture (CKMR).
    Full documentation
    and vignettes are mirrored at <https://eriqande.github.io/CKMRpop/index.html>
    and can be read online there.
	"""
	
	cran = "CKMRpop" 

	version("0.1.3", md5="3b350687e75ed9cf19bb2df25899dbc8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
