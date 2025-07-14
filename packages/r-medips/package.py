# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedips(RPackage):
	"""DNA IP-seq data analysis

	MEDIPS was developed for analyzing data derived from methylated DNA immunoprecipitation (MeDIP) experiments followed by sequencing (MeDIP-seq). However, MEDIPS provides functionalities for the analysis of any kind of quantitative sequencing data (e.g. ChIP-seq, MBD-seq, CMS-seq and others) including calculation of differential coverage between groups of samples and saturation and correlation analysis.
	"""
	
	bioc = "MEDIPS"

	version("1.60.0", commit="31eb178c3e25753a2e409698478aa0ee9c2c085b")
	version("1.54.0", commit="a174f2a0428e3141fa27f7429c6fc9064c24d215")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
