# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbseqr(RPackage):
	"""Reporting and data analysis functionalities for Rep-Seq datasets of antibody libraries

	AbSeq is a comprehensive bioinformatic pipeline for the analysis of sequencing datasets generated from antibody libraries and abseqR is one of its packages. abseqR empowers the users of abseqPy (https://github.com/malhamdoosh/abseqPy) with plotting and reporting capabilities and allows them to generate interactive HTML reports for the convenience of viewing and sharing with other researchers. Additionally, abseqR extends abseqPy to compare multiple repertoire analyses and perform further downstream analysis on its output.
	"""
	
	homepage = "https://github.com/malhamdoosh/abseqR"
	bioc = "abseqR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/abseqR_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/abseqR/abseqR_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="8865dd4178a451436acd87c3cc76ae5d0b392195b379b9adf00bd407952d0669")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-flexdashboard", type=("build", "run"))
	depends_on("r-biocparallel@1.1.25:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("pandoc@1.19.2.1:", type=("build", "link", "run"))
