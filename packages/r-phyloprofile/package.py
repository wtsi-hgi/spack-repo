# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyloprofile(RPackage):
	"""PhyloProfile

	PhyloProfile is a tool for exploring complex phylogenetic profiles. Phylogenetic profiles, presence/absence patterns of genes over a set of species, are commonly used to trace the functional and evolutionary history of genes across species and time. With PhyloProfile we can enrich regular phylogenetic profiles with further data like sequence/structure similarity, to make phylogenetic profiling more meaningful. Besides the interactive visualisation powered by R-Shiny, the package offers a set of further analysis features to gain insights like the gene age estimation or core gene identification.
	"""
	
	homepage = "https://github.com/BIONF/PhyloProfile/"
	bioc = "PhyloProfile" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PhyloProfile_1.16.4.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PhyloProfile/PhyloProfile_1.16.4.tar.gz"]

	version("1.16.4", md5="e8c11595842347bd6ace0bdb57426311")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-biodist", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-omadb", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
