# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrviaspcn(RPackage):
	"""Drug Repurposing in Cancer via a Subpathway Crosstalk Network

	A systematic biology tool was developed to repurpose drugs via a subpathway crosstalk network. The operation modes include 1) calculating centrality scores of SPs in the context of gene expression data to reflect the influence of SP crosstalk, 2) evaluating drug-disease reverse association based on disease- and drug-induced SPs weighted by the SP crosstalk, 3) identifying cancer candidate drugs through perturbation analysis. There are also several functions used to visualize the results.
	"""
	
	cran = "DRviaSPCN" 

	version("0.1.4", md5="80f90c5774d751a825021adced9ae401")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
