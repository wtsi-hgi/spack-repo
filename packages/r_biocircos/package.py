# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocircos(RPackage):
	"""Interactive Circular Visualization of Genomic Data using
'htmlwidgets' and 'BioCircos.js'

	Implement in 'R' interactive Circos-like visualizations of genomic data, to map information
	such as genetic variants, genomic fusions and aberrations to a circular genome, as proposed by the
	'JavaScript' library 'BioCircos.js', based on the 'JQuery' and 'D3' technologies. The output is by 
	default displayed in stand-alone HTML documents or in the 'RStudio' viewer pane. Moreover it can be
	integrated in 'R Markdown' documents and 'Shiny' applications.
	"""
	
	homepage = "https://github.com/lvulliard/BioCircos.R"
	cran = "BioCircos" 

	version("0.3.4", md5="6dda56278e39a0601266022b5394f7eb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
