# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgaworkflow(RPackage):
	"""TCGA Workflow Analyze cancer genomics and epigenomics data using Bioconductor packages

	Biotechnological advances in sequencing have led to an explosion of publicly available data via large international consortia such as The Cancer Genome Atlas (TCGA), The Encyclopedia of DNA Elements (ENCODE), and The NIH Roadmap Epigenomics Mapping Consortium (Roadmap). These projects have provided unprecedented opportunities to interrogate the epigenome of cultured cancer cell lines as well as normal and tumor tissues with high genomic resolution. The Bioconductor project offers more than 1,000 open-source software and statistical packages to analyze high-throughput genomic data. However, most packages are designed for specific data types (e.g. expression, epigenetics, genomics) and there is no one comprehensive tool that provides a complete integrative analysis of the resources and data provided by all three public projects. A need to create an integration of these different analyses was recently proposed. In this workflow, we provide a series of biologically focused integrative analyses of different molecular data. We describe how to download, process and prepare TCGA data and by harnessing several key Bioconductor packages, we describe how to extract biologically meaningful genomic and epigenomic data. Using Roadmap and ENCODE data, we provide a work plan to identify biologically relevant functional epigenomic elements associated with cancer. To illustrate our workflow, we analyzed two types of brain tumors: low-grade glioma (LGG) versus high-grade glioma (glioblastoma multiform or GBM).
	"""
	
	homepage = "https://f1000research.com/articles/5-1542/v2"
	bioc = "TCGAWorkflow" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/TCGAWorkflow_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/TCGAWorkflow/TCGAWorkflow_1.26.0.tar.gz"]

	version("1.26.0", md5="5fae8b85fe7628ac380aca2a1dbd2374")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-elmer", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-c3net", type=("build", "run"))
	depends_on("r-chipseeker", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-downloader@0.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-motifstack", type=("build", "run"))
	depends_on("r-pathview", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rgadem", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-rtcgatoolbox", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-tcgabiolinks", type=("build", "run"))
	depends_on("r-tcgaworkflowdata@1.25.3:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))

