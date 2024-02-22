# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsort(RPackage):
	"""uSORT: A self-refining ordering pipeline for gene selection

	This package is designed to uncover the intrinsic cell progression path from single-cell RNA-seq data. It incorporates data pre-processing, preliminary PCA gene selection, preliminary cell ordering, feature selection, refined cell ordering, and post-analysis interpretation and visualization.
	"""
	
	bioc = "uSORT" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/uSORT_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/uSORT/uSORT_1.28.0.tar.gz"]

	version("1.28.0", md5="0c89e7d86bb2f37b99ce32989b121110")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-monocle", type=("build", "run"))
