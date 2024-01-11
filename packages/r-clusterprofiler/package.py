# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterprofiler(RPackage):
	"""statistical analysis and visualization of functional profiles for genes
	and gene clusters.

	This package implements methods to analyze and visualize functional
	profiles (GO and KEGG) of gene and gene clusters."""

	bioc = "clusterProfiler"

	version("4.10.0", commit="fa63cb0a174b3280baacba784bd20483daf24c03")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-dose@3.23.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-enrichplot@1.9.3:", type=("build", "run"))
	depends_on("r-gosemsim@2.27.2:", type=("build", "run"))
	depends_on("r-gson@0.0.7:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yulab-utils@0.0.7:", type=("build", "run"))
