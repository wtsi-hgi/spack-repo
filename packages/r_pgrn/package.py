# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgrn(RPackage):
	"""Single-Cell RNA Sequencing Pseudo-Time Based Gene Regulatory
Network Inference

	Inference and visualize gene regulatory network based on single-cell RNA sequencing pseudo-time information.
	"""
	
	cran = "pGRN" 

	version("0.3.5", md5="98df5dc0493e5dd455f7ae7bb07ca35d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
