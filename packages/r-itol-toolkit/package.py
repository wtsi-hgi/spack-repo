# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItolToolkit(RPackage):
	"""Helper Functions for 'Interactive Tree Of Life'

	
    The 'Interactive Tree Of Life' <https://itol.embl.de/> online server can 
    edit and annotate trees interactively. The 'itol.toolkit' package can 
    support all types of annotation templates.
	"""
	
	cran = "itol.toolkit" 

	version("1.1.7", md5="d3a7fa94a437d7f3a7e63d9df869348f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-wesanderson", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
