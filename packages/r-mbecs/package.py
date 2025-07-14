# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbecs(RPackage):
	"""Evaluation and correction of batch effects in microbiome data-sets

	The Microbiome Batch Effect Correction Suite (MBECS) provides a set of functions to evaluate and mitigate unwated noise due to processing in batches. To that end it incorporates a host of batch correcting algorithms (BECA) from various packages. In addition it offers a correction and reporting pipeline that provides a preliminary look at the characteristics of a data-set before and after correcting for batch effects.
	"""
	
	homepage = "https://github.com/rmolbrich/MBECS"
	bioc = "MBECS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MBECS_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MBECS/MBECS_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="818a8e43937b8b07c98354a570de272fa4ee4529df4134a72bce3a618d58fbc8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ruv", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
