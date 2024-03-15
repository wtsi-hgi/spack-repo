# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMousefm(RPackage):
	"""In-silico methods for genetic finemapping in inbred mice

	This package provides methods for genetic finemapping in inbred mice by taking advantage of their very high homozygosity rate (>95%).
	"""
	
	bioc = "MouseFM" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MouseFM_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MouseFM/MouseFM_1.12.0.tar.gz"]

	version("1.12.0", md5="02947a619a95abf1ad58bb781953a22d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
