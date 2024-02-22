# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenbarcode(RPackage):
	"""Analysis and Visualization Tools for Genetic Barcode Data

	Provides the necessary functions to identify and extract a selection of already available barcode constructs (Cornils, K. et al. (2014) <doi:10.1093/nar/gku081>) and freely choosable barcode designs from next generation sequence (NGS) data. Furthermore, it offers the possibility to account for sequence errors, the calculation of barcode similarities and provides a variety of visualisation tools (Thielecke, L. et al. (2017) <doi:10.1038/srep43249>).
	"""
	
	cran = "genBaRcode" 

	version("1.2.7", md5="608118e70179f32c5bfa8939ef75da16")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
