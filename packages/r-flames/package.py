# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlames(RPackage):
	"""FLAMES: Full Length Analysis of Mutations and Splicing in long read RNA-seq data

	Semi-supervised isoform detection and annotation from both bulk and single-cell long read RNA-seq data. Flames provides automated pipelines for analysing isoforms, as well as intermediate functions for manual execution.
	"""
	
	homepage = "https://github.com/OliverVoogd/FLAMES"
	bioc = "FLAMES" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/FLAMES_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/FLAMES/FLAMES_1.8.0.tar.gz"]

	version("2.2.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="da12030c47ad7d766a7a76ed97e5fb089af15fd1c78846afba7b11089efa6724")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-bambu", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dropletutils", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rhtslib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
