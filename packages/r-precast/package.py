# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecast(RPackage):
	"""Embedding and Clustering with Alignment for Spatial Datasets

	An efficient data integration method is provided for multiple spatial transcriptomics data with non-cluster-relevant effects such as the complex batch effects. It unifies spatial factor analysis simultaneously with spatial clustering and embedding alignment, requiring only partially shared cell/domain clusters across datasets. More details can be referred to Wei Liu, et al. (2023) <doi:10.1038/s41467-023-35947-w>.
	"""
	
	homepage = "https://github.com/feiyoung/PRECAST"
	cran = "PRECAST" 

	version("1.6.4", md5="e3c0b20ba6460445b5bc83abd28e004c")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-giraf", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dr-sc", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
