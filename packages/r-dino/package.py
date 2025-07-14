# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDino(RPackage):
	"""Normalization of Single-Cell mRNA Sequencing Data

	Dino normalizes single-cell, mRNA sequencing data to correct for technical variation, particularly sequencing depth, prior to downstream analysis. The approach produces a matrix of corrected expression for which the dependency between sequencing depth and the full distribution of normalized expression; many existing methods aim to remove only the dependency between sequencing depth and the mean of the normalized expression. This is particuarly useful in the context of highly sparse datasets such as those produced by 10X genomics and other uninque molecular identifier (UMI) based microfluidics protocols for which the depth-dependent proportion of zeros in the raw expression data can otherwise present a challenge.
	"""
	
	homepage = "https://github.com/JBrownBiostat/Dino"
	bioc = "Dino" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Dino_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Dino/Dino_1.8.0.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="ce278f24eade2de93026f784dfabb62eea0adaa860ca596d10f7dcc13354a8df")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
