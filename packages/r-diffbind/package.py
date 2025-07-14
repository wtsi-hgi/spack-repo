# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffbind(RPackage):
	"""Differential Binding Analysis of ChIP-Seq Peak Data

	Compute differentially bound sites from multiple ChIP-seq experiments using affinity (quantitative) data. Also enables occupancy (overlap) analysis and plotting functions.
	"""
	
	homepage = "https://www.cruk.cam.ac.uk/core-facilities/bioinformatics-core/software/DiffBind"
	bioc = "DiffBind" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DiffBind_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DiffBind/DiffBind_3.12.0.tar.gz"]

	version("3.18.0", tag="RELEASE_3_21")
	version("3.12.0", sha256="069926f90bef2cf148fa644b01cd63d7ec558e2be526cbd078ecb2401de98cda")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-systempiper", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rsamtools@2.13.1:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-apeglm", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
	depends_on("r-greylistchip", type=("build", "run"))
	depends_on("r-rhtslib@1.99.1:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
