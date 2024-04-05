# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYamlet(RPackage):
	"""Versatile Curation of Table Metadata

	A YAML-based
 mechanism for working with table metadata. Supports
 compact syntax for creating, modifying, viewing, exporting,
 importing, displaying, and plotting metadata coded as column 
 attributes. The 'yamlet' dialect is valid 'YAML' with
 defaults and conventions chosen to improve readability. 
 See ?yamlet, ?decorate, ?modify, ?io_csv, and ?ggplot.decorated.
	"""
	
	cran = "yamlet" 

	version("1.0.3", md5="f49f81a9588c7e7b579c49767cc40350")
	version("1.0.0", md5="2244b5574fd728cc3a547bcf0a9595c9")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-csv@0.6.2:", type=("build", "run"))
	depends_on("r-encode", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-spork@0.3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
