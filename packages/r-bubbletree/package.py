# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBubbletree(RPackage):
	"""BubbleTree: an intuitive visualization to elucidate tumoral aneuploidy and clonality in somatic mosaicism using next generation sequencing data

	CNV analysis in groups of tumor samples.
	"""
	
	bioc = "BubbleTree" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BubbleTree_2.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BubbleTree/BubbleTree_2.32.0.tar.gz"]

	version("2.32.0", md5="84649d9271ce193051e18a7bb56ff58e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-biocgenerics@0.31.6:", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-biovizbase", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
