# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArtms(RPackage):
	"""Analytical R tools for Mass Spectrometry

	artMS provides a set of tools for the analysis of proteomics label-free datasets. It takes as input the MaxQuant search result output (evidence.txt file) and performs quality control, relative quantification using MSstats, downstream analysis and integration. artMS also provides a set of functions to re-format and make it compatible with other analytical tools, including, SAINTq, SAINTexpress, Phosfate, and PHOTON. Check [http://artms.org](http://artms.org) for details.
	"""
	
	homepage = "http://artms.org"
	bioc = "artMS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/artMS_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/artMS/artMS_1.20.0.tar.gz"]

	version("1.20.0", md5="d52a9405bcf6f4a3920ecb70be49c1d9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-getopt", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-msstats", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
