# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrouphmap(RPackage):
	"""'Grouphmap' is an Automated One-Step Common Analysis of Batch
Expression Profile

	The 'Grouphmap' was implemented in R, an open-source programming environment, and was released under the provided website. The difference analysis is based on the 'limma' package, which can cover gene and protein expression profiles (Reference: Matthew E Ritchie , Belinda Phipson , Di Wu , Yifang Hu , Charity W Law , Wei Shi , Gordon K Smyth (2015) <doi:10.1093/nar/gkv007>). The GO enrichment analysis is based on the 'clusterProfiler' package and supports three common species: human, mouse, and yeast (Reference: Guangchuang Yu, Li-Gen Wang, Yanyan Han, Qing-Yu He (2012) <doi:10.1089/omi.2011.0118>). The results of batch difference analysis and enrichment analysis are output in separate folders for easy viewing and further visualization of the results during the process. The results returned a heatmap in R and exported to 3 folders named DEG, go, and merge.
	"""
	
	cran = "Grouphmap" 

	version("1.0.0", md5="cb0a9cb2e8bcb15b368d76dc0cb8a317")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
