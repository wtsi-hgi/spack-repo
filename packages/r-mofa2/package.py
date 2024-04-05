# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMofa2(RPackage):
	"""Multi-Omics Factor Analysis v2

	The MOFA2 package contains a collection of tools for training and analysing multi-omic factor analysis (MOFA). MOFA is a probabilistic factor model that aims to identify principal axes of variation from data sets that can comprise multiple omic layers and/or groups of samples. Additional time or space information on the samples can be incorporated using the MEFISTO framework, which is part of MOFA2. Downstream analysis functions to inspect molecular features underlying each factor, vizualisation, imputation etc are available.
	"""
	
	homepage = "https://biofam.github.io/MOFA2/index.html"
	bioc = "MOFA2" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MOFA2_1.12.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MOFA2/MOFA2_1.12.1.tar.gz"]

	version("1.12.1", md5="becb5f2af1cc6aad6f9fa826cd9d1ba9", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/MOFA2_1.12.1.tar.gz")
	version("1.12.1", md5="becb5f2af1cc6aad6f9fa826cd9d1ba9", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MOFA2_1.12.1.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("python@3:", type=("build", "link", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
	depends_on("py-pandas", type=("build", "link", "run"))
	depends_on("py-h5py", type=("build", "link", "run"))
	depends_on("py-scipy", type=("build", "link", "run"))
	depends_on("py-scikit-learn", type=("build", "link", "run"))
	depends_on("py-mofapy2", type=("build", "link", "run"))
