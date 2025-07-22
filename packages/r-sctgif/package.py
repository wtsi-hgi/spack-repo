# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSctgif(RPackage):
	"""Cell type annotation for unannotated single-cell RNA-Seq data

	scTGIF connects the cells and the related gene functions without cell type label.
	"""
	
	bioc = "scTGIF" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scTGIF_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scTGIF/scTGIF_1.16.0.tar.gz"]

	version("1.16.0", sha256="202714ff5a7bf32b0993a7e88ed2f9c81b107acc3bb743bb0fe2f5f786c6bfe7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tagcloud", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-nntensor", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-schex", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
