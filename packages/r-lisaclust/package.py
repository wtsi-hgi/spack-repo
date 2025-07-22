# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLisaclust(RPackage):
	"""lisaClust: Clustering of Local Indicators of Spatial Association

	lisaClust provides a series of functions to identify and visualise regions of tissue where spatial associations between cell-types is similar. This package can be used to provide a high-level summary of cell-type colocalization in multiplexed imaging data that has been segmented at a single-cell resolution.
	"""
	
	homepage = "https://ellispatrick.github.io/lisaClust/"
	bioc = "lisaClust" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lisaClust_1.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lisaClust/lisaClust_1.10.1.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.1", sha256="f3d511fa8af7260b76849c13a2e1d7c495548f1bf003d202588638b0a8deb8b2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-spicyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
