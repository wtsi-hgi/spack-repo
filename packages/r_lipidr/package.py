# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLipidr(RPackage):
	"""Data Mining and Analysis of Lipidomics Datasets

	lipidr an easy-to-use R package implementing a complete workflow for downstream analysis of targeted and untargeted lipidomics data. lipidomics results can be imported into lipidr as a numerical matrix or a Skyline export, allowing integration into current analysis frameworks. Data mining of lipidomics datasets is enabled through integration with Metabolomics Workbench API. lipidr allows data inspection, normalization, univariate and multivariate analysis, displaying informative visualizations. lipidr also implements a novel Lipid Set Enrichment Analysis (LSEA), harnessing molecular information such as lipid class, total chain length and unsaturation.
	"""
	
	homepage = "https://github.com/ahmohamed/lipidr"
	bioc = "lipidr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lipidr_2.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lipidr/lipidr_2.16.0.tar.gz"]

	version("2.16.0", md5="27b17acc2b4de0439304799e0a7cba2a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-ropls", type=("build", "run"))
	depends_on("r-imputelcmd", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
