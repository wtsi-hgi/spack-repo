# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHoarder(RPackage):
	"""Collect and Retrieve Annotation Data for Various Genomic Data
Using Different Webservices

	Cross-species identification of novel gene candidates using the NCBI web service is provided. Further, sets of miRNA target genes can be identified by using the targetscan.org API.
	"""
	
	cran = "hoardeR" 

	version("0.9.4-2", md5="7a0fdf77f10135297e32e22f4dcec84b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-bamsignals@1.10:", type=("build", "run"))
	depends_on("r-biostrings@2.46:", type=("build", "run"))
	depends_on("r-data-table@1.11.4:", type=("build", "run"))
	depends_on("r-genomicranges@1.30.3:", type=("build", "run"))
	depends_on("r-genomictools-filehandler@0.1.4:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.12:", type=("build", "run"))
	depends_on("r-kernsmooth@2.23.15:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-mass@7.3.31:", type=("build", "run"))
	depends_on("r-r-utils@2.6:", type=("build", "run"))
	depends_on("r-rcurl@1.95:", type=("build", "run"))
	depends_on("r-rmarkdown@1.10:", type=("build", "run"))
	depends_on("r-rsamtools@1.30:", type=("build", "run"))
	depends_on("r-s4vectors@0.16:", type=("build", "run"))
	depends_on("r-seqinr@1.0.2:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-xml@3.98.1.1:", type=("build", "run"))
