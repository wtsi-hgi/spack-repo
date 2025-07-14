# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImcrtools(RPackage):
	"""Methods for imaging mass cytometry data analysis

	This R package supports the handling and analysis of imaging mass cytometry and other highly multiplexed imaging data. The main functionality includes reading in single-cell data after image segmentation and measurement, data formatting to perform channel spillover correction and a number of spatial analysis approaches. First, cell-cell interactions are detected via spatial graph construction; these graphs can be visualized with cells representing nodes and interactions representing edges. Furthermore, per cell, its direct neighbours are summarized to allow spatial clustering. Per image/grouping level, interactions between types of cells are counted, averaged and compared against random permutations. In that way, types of cells that interact more (attraction) or less (avoidance) frequently than expected by chance are detected.
	"""
	
	homepage = "https://github.com/BodenmillerGroup/imcRtools"
	bioc = "imcRtools"

	version("1.14.0", commit="baf3056ba611378f8ebc8c1c5d45fec059758234")
	version("1.8.0", commit="5dc066a4de1eba5df9a1b7a2f96b4ef8a91c97a2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-cytomapper", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-rtriangle", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-distances", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
