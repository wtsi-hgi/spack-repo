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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ggsc_1.0.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ggsc/ggsc_1.0.2.tar.gz"]

	version("1.0.2", md5="4c0a1656e9943cadf436244c65b18242")

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
