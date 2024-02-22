# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyngen(RPackage):
	"""A Multi-Modal Simulator for Spearheading Single-Cell Omics
Analyses

	A novel, multi-modal simulation engine for
    studying dynamic cellular processes at single-cell resolution. 'dyngen'
    is more flexible than current single-cell simulation engines. It
    allows better method development and benchmarking, thereby stimulating
    development and testing of novel computational methods. Cannoodt et
    al. (2021) <doi:10.1038/s41467-021-24152-2>.
	"""
	
	homepage = "https://dyngen.dynverse.org"
	cran = "dyngen" 

	version("1.0.5", md5="dff57dee71cbf9be199c462f85785d35")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dynutils@1.0.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph@2:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gillespiessa2@0.2.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lmds", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.4.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
