# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetacoder(RPackage):
	"""Tools for Parsing, Manipulating, and Graphing Taxonomic
Abundance Data

	A set of tools for parsing, manipulating, and graphing data
    classified by a hierarchy (e.g. a taxonomy).
	"""
	
	homepage = "https://grunwaldlab.github.io/metacoder_documentation/"
	cran = "metacoder" 

	version("0.3.7", md5="31a51cb7f568b9b51f41640ca002edae")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
