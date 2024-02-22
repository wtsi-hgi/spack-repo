# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinyarray(RPackage):
	"""Expression Data Analysis and Visualization

	Gene Expression Omnibus(GEO) and The Cancer Genome Atlas(TCGA) are common bioinformatics public databases. We integrate the regular analysis and charts for expression data, to analyze and display the data concisely and intuitively.
	"""
	
	homepage = "https://github.com/xjsun1221/tinyarray"
	cran = "tinyarray" 

	version("2.3.2", md5="65152b6f79e576783da67bd79765386a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
