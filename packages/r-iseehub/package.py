# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseehub(RPackage):
	"""iSEE for the Bioconductor ExperimentHub

	This package defines a custom landing page for an iSEE app interfacing with the Bioconductor ExperimentHub. The landing page allows users to browse the ExperimentHub, select a data set, download and cache it, and import it directly into a Bioconductor iSEE app.
	"""
	
	homepage = "https://github.com/iSEE/iSEEhub"
	bioc = "iSEEhub" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iSEEhub_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iSEEhub/iSEEhub_1.4.0.tar.gz"]

	version("1.4.0", md5="6ebb32da66242f608b83522fca1d9a62")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-isee", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
