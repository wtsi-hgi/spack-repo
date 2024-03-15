# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clusterProfiler_4.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clusterProfiler/clusterProfiler_4.10.1.tar.gz"]

	version("4.10.1", md5="9c7eeb69f8cc22b6712b75069a4b0fc9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-dose@3.23.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-enrichplot@1.9.3:", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
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
