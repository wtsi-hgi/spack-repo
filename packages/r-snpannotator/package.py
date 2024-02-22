# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpannotator(RPackage):
	"""Investigating the Functional Characteristics of Selected SNPs
and Their Vicinity Genomic Region

	To investigate the functional characteristics of selected SNPs and their vicinity genomic region. Linked SNPs in moderate to high linkage disequilibrium (e.g. r2>0.50) with the corresponding index SNPs will be selected for further analysis.
	"""
	
	cran = "SNPannotator" 

	version("0.2.6.0", md5="db44d5c4af50fb756c31d0fcc6130b1e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
