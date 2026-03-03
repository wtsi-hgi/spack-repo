# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTadcompare(RPackage):
	"""TADCompare: Identification and characterization of differential TADs

	TADCompare is an R package designed to identify and characterize differential Topologically Associated Domains (TADs) between multiple Hi-C contact matrices. It contains functions for finding differential TADs between two datasets, finding differential TADs over time and identifying consensus TADs across multiple matrices. It takes all of the main types of HiC input and returns simple, comprehensive, easy to analyze results.
	"""
	
	homepage = "https://github.com/dozmorovlab/TADCompare"
	bioc = "TADCompare" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TADCompare_1.12.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TADCompare/TADCompare_1.12.1.tar.gz"]

	version("1.12.1", md5="bf2880cfb4ff92e40345c7764c9a5077")
	version("1.12.0", md5="92966a38a0c202cfe7dbd09bb83b23b1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-primme", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-hiccompare", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
