# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaseqr2(RPackage):
	"""An R package for the analysis and result reporting of RNA-Seq data by combining multiple statistical algorithms

	Provides an interface to several normalization and statistical testing packages for RNA-Seq gene expression data. Additionally, it creates several diagnostic plots, performs meta-analysis by combinining the results of several statistical tests and reports the results in an interactive way.
	"""
	
	homepage = "http://www.fleming.gr"
	bioc = "metaseqR2" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metaseqR2_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metaseqR2/metaseqR2_1.14.0.tar.gz"]

	version("1.14.0", md5="93f754d60de0b3db00aca9ee5eef3a20", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metaseqR2_1.14.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-absseq", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-dss", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-edaseq", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-harmonicmeanp", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-log4r", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nbpseq", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rmdformats", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-survcomp", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
