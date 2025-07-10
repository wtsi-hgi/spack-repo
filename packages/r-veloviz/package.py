# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVeloviz(RPackage):
	"""VeloViz: RNA-velocity informed 2D embeddings for visualizing cell state trajectories

	VeloViz uses each cell’s current observed and predicted future transcriptional states inferred from RNA velocity analysis to build a nearest neighbor graph between cells in the population. Edges are then pruned based on a cosine correlation threshold and/or a distance threshold and the resulting graph is visualized using a force-directed graph layout algorithm. VeloViz can help ensure that relationships between cell states are reflected in the 2D embedding, allowing for more reliable representation of underlying cellular trajectories.
	"""
	
	bioc = "veloviz" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/veloviz_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/veloviz/veloviz_1.8.0.tar.gz"]

	version("1.8.0", sha256="5f6f26e29f060419668bf968491c96cbba1eb470a16ae4d0885731fc19909987")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
