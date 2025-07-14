# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROgre(RPackage):
	"""Calculate, visualize and analyse overlap between genomic regions

	OGRE calculates overlap between user defined genomic region datasets. Any regions can be supplied i.e. genes, SNPs, or reads from sequencing experiments. Key numbers help analyse the extend of overlaps which can also be visualized at a genomic level.
	"""
	
	homepage = "https://github.com/svenbioinf/OGRE/"
	bioc = "OGRE"

	version("1.12.0", commit="d2cda3b90712c4140ac744a9845a62a227295baa")
	version("1.6.0", commit="a47cbc35fa9e93585a977a2e854648c0f7aa4f74")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
