# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgff(RPackage):
	"""R Utilities for GFF Files

	R utilities for gff files, either general feature format (GFF3) or gene transfer format (GTF) formatted files. This package includes functions for producing summary stats, check for consistency and sorting errors, conversion from GTF to GFF3 format, file sorting, visualization and plotting of feature hierarchy, and exporting user defined feature subsets to SAF format. This tool was developed by the BioinfoGP core facility at CNB-CSIC. 
	"""
	
	cran = "Rgff" 

	version("0.1.6", md5="7dcf7b8083448cdec8c06290e8bb40af")

	depends_on("r-withr@2.4.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.12:", type=("build", "run"))
	depends_on("r-stringi@1.7.6:", type=("build", "run"))
	depends_on("r-data-tree@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-rjsonio@1.3.1.6:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
