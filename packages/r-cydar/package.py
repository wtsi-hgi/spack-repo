# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCydar(RPackage):
	"""Using Mass Cytometry for Differential Abundance Analyses

	Identifies differentially abundant populations between samples and groups in mass cytometry data. Provides methods for counting cells into hyperspheres, controlling the spatial false discovery rate, and visualizing changes in abundance in the high-dimensional marker space.
	"""
	
	bioc = "cydar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cydar_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cydar/cydar_1.26.0.tar.gz"]

	version("1.26.0", sha256="da61e1f9a394d64538070bf084fdfceaf4bf43e6ab18389ede54da058f5ee305")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
