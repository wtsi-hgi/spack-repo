# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScfeatures(RPackage):
	"""scFeatures: Multi-view representations of single-cell and spatial data for disease outcome prediction

	scFeatures constructs multi-view representations of single-cell and spatial data. scFeatures is a tool that generates multi-view representations of single-cell and spatial data through the construction of a total of 17 feature types. These features can then be used for a variety of analyses using other software in Biocondutor.
	"""
	
	homepage = "https://sydneybiox.github.io/scFeatures/"
	bioc = "scFeatures" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scFeatures_1.3.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scFeatures/scFeatures_1.3.2.tar.gz"]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.3.2", sha256="3d9b93b52e965b5f93ac1b9ee9b12fbd88806c8b0ef46560d267a22d927331a4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-ensdb-hsapiens-v79", type=("build", "run"))
	depends_on("r-ensdb-mmusculus-v79", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-proxyc", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-aucell", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-singlecellsignalr", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
