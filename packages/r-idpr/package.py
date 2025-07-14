# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdpr(RPackage):
	"""Profiling and Analyzing Intrinsically Disordered Proteins in R

	‘idpr’ aims to integrate tools for the computational analysis of intrinsically disordered proteins (IDPs) within R. This package is used to identify known characteristics of IDPs for a sequence of interest with easily reported and dynamic results. Additionally, this package includes tools for IDP-based sequence analysis to be used in conjunction with other R packages. Described in McFadden WM & Yanowitz JL (2022). "idpr: A package for profiling and analyzing Intrinsically Disordered Proteins in R." PloS one, 17(4), e0266929. <https://doi.org/10.1371/journal.pone.0266929>.
	"""
	
	bioc = "idpr"

	version("1.18.0", commit="4ea9cd7cd7a0c20ae7c4002bce1a637793795e37")
	version("1.12.0", commit="1bbdb6b3f2a04e06590955cad35ec1f43daedf4c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-biostrings@2.56:", type=("build", "run"))
