# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetomics(RPackage):
	"""Multi-Omics (time-course) network-based integration and interpretation

	netOmics is a multi-omics networks builder and explorer. It uses a combination of network inference algorithms and and knowledge-based graphs to build multi-layered networks. The package can be combined with timeOmics to incorporate time-course expression data and build sub-networks from multi-omics kinetic clusters. Finally, from the generated multi-omics networks, propagation analyses allow the identification of missing biological functions (1), multi-omics mechanisms (2) and molecules between kinetic clusters (3). This helps to resolve complex regulatory mechanisms.
	"""
	
	homepage = "https://github.com/abodein/netOmics"
	bioc = "netOmics" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/netOmics_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/netOmics/netOmics_1.8.0.tar.gz"]

	version("1.8.0", md5="8ab3cf60546da2beea2e9c3630340c12")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-randomwalkrestartmh", type=("build", "run"))
	depends_on("r-gprofiler2", type=("build", "run"))
