# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomemarker(RPackage):
	"""microbiome biomarker analysis toolkit

	To date, a number of methods have been developed for microbiome marker discovery based on metagenomic profiles, e.g. LEfSe. However, all of these methods have its own advantages and disadvantages, and none of them is considered standard or universal. Moreover, different programs or softwares may be development using different programming languages, even in different operating systems. Here, we have developed an all-in-one R package microbiomeMarker that integrates commonly used differential analysis methods as well as three machine learning-based approaches, including Logistic regression, Random forest, and Support vector machine, to facilitate the identification of microbiome markers.
	"""
	
	homepage = "https://github.com/yiluheihei/microbiomeMarker"
	bioc = "microbiomeMarker" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/microbiomeMarker_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/microbiomeMarker/microbiomeMarker_1.8.0.tar.gz"]

	version("1.8.0", md5="facf2f8071da6049b688fe3d16efb0e2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-tidytree", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-ggsignif", type=("build", "run"))
	depends_on("r-metagenomeseq", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-biomformat", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-ancombc", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-aldex2", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-plotroc", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
