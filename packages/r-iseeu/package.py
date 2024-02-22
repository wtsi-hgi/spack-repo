# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseeu(RPackage):
	"""iSEE Universe

	iSEEu (the iSEE universe) contains diverse functionality to extend the usage of the iSEE package, including additional classes for the panels, or modes allowing easy configuration of iSEE applications.
	"""
	
	homepage = "https://github.com/iSEE/iSEEu"
	bioc = "iSEEu" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/iSEEu_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/iSEEu/iSEEu_1.14.0.tar.gz"]

	version("1.14.0", md5="d9349d85759c37c8a971b4ffcebcecea")

	depends_on("r-isee", type=("build", "run"))
	depends_on("r-iseehex", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
