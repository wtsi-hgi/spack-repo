# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsector(RPackage):
	"""Draw Sectors

	Some useful functions that can use 'grid' and 'ggplot2' to plot sectors and interact with 'Seurat' to plot gene expression percentages. Also, there are some examples of how to draw sectors in 'ComplexHeatmap'.
	"""
	
	cran = "ggsector" 

	version("1.6.6", md5="e3cfe66d0d75a3d44c038fc2f62c2dba")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-prettydoc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
