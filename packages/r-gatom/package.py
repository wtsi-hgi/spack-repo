# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGatom(RPackage):
	"""Finding an Active Metabolic Module in Atom Transition Network

	This package implements a metabolic network analysis pipeline to identify an active metabolic module based on high throughput data. The pipeline takes as input transcriptional and/or metabolic data and finds a metabolic subnetwork (module) most regulated between the two conditions of interest. The package further provides functions for module post-processing, annotation and visualization.
	"""
	
	homepage = "https://github.com/ctlab/gatom/"
	bioc = "gatom" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gatom_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gatom/gatom_1.0.0.tar.gz"]

	version("1.0.0", md5="0e86773c5bafed3a4c13b7db82015463")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-bionet", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mwcsr", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinycyjs@1:", type=("build", "run"))
