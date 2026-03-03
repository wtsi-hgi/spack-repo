# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcscxenatools(RPackage):
	"""Download and Explore Datasets from UCSC Xena Data Hubs

	Download and explore datasets from UCSC Xena data hubs, which
    are a collection of UCSC-hosted public databases such as TCGA, ICGC,
    TARGET, GTEx, CCLE, and others.  Databases are normalized so they can
    be combined, linked, filtered, explored and downloaded.
	"""
	
	homepage = "https://docs.ropensci.org/UCSCXenaTools/"
	cran = "UCSCXenaTools" 

	version("1.4.8", md5="801ed2a741341645c167f6325813826c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
