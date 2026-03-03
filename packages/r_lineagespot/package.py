# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLineagespot(RPackage):
	"""Detection of SARS-CoV-2 lineages in wastewater samples using next-generation sequencing

	Lineagespot is a framework written in R, and aims to identify SARS-CoV-2 related mutations based on a single (or a list) of variant(s) file(s) (i.e., variant calling format). The method can facilitate the detection of SARS-CoV-2 lineages in wastewater samples using next generation sequencing, and attempts to infer the potential distribution of the SARS-CoV-2 lineages.
	"""
	
	homepage = "https://github.com/BiodataAnalysisGroup/lineagespot"
	bioc = "lineagespot" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lineagespot_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lineagespot/lineagespot_1.6.0.tar.gz"]

	version("1.6.0", md5="7a06bfea8fdf81ea88ebe7f4478607f6")

	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
