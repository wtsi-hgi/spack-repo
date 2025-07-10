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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OGRE_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OGRE/OGRE_1.6.0.tar.gz"]

	version("1.6.0", sha256="7124b0ba410224f0602ed7775daabc97b80a91ebb2bdbcd67b4a2ac78fc0f6d4")

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
