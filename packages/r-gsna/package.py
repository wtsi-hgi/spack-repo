# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsna(RPackage):
	"""Gene Set Networking Analysis Package

	Create networks of gene sets, infer clusters of functionally-related gene sets based
  on similarity statistics, and visualize the results. This package simplifies and accelerates
  interpretation of pathways analysis data sets. It is designed to work in tandem with standard
  pathways analysis methods, such as the 'GSEA' program (Gene Set Enrichment Analysis), CERNO
  (Coincident Extreme Ranks in Numerical Observations, implemented in the 'tmod' package) and others.
  Inputs to 'GSNA' are the outputs of pathways analysis methods: a list of gene sets (or "modules"),
  pathways or GO-terms with associated p-values. Since pathways analysis methods may be used to
  analyze many different types of data including transcriptomic, epigenetic, and high-throughput
  screen data sets, the 'GSNA' pipeline is applicable to these data as well. The use of 'GSNA' has
  been described in the following papers: 
  Collins DR, Urbach JM, Racenet ZJ, Arshad U, Power KA, Newman RM, et al. (2021) <doi:10.1016/j.immuni.2021.08.007>,
  Collins DR, Hitschfel J, Urbach JM, Mylvaganam GH, Ly NL, Arshad U, et al. (2023) <doi:10.1126/sciimmunol.ade5872>.
	"""
	
	cran = "GSNA" 

	version("0.1.4.1", md5="961452b459f967c6e323b552d27b1ac6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tmod", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
