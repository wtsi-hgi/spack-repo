# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglecellsignalr(RPackage):
	"""Cell Signalling Using Single Cell RNAseq Data Analysis

	Allows single cell RNA seq data analysis, clustering, creates internal network and infers cell-cell interactions.
	"""
	
	bioc = "SingleCellSignalR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SingleCellSignalR_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SingleCellSignalR/SingleCellSignalR_1.14.0.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="10d81f52a70418767e273289b7fbfb8f8ae6ee87bfeb58f5687c2e6083390e79")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
