# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsc(RPackage):
	"""Visualizing Single Cell Data

	Useful functions to visualize single cell and spatial data. It supports both 'SingleCellExperiment' and 'Seurat' objects. It also supports visualizing the data using grammar of graphics implemented in 'ggplot2'.
	"""
	
	homepage = "https://github.com/YuLab-SMU/ggsc"
	bioc = "ggsc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggsc_1.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggsc/ggsc_1.0.2.tar.gz"]

	version("1.0.2", sha256="e58a6d076170b9b5cfb7e0033df16e3f42c0cea78f6c37847089cf1802ad48a3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tidydr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
