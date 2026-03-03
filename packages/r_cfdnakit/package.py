# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfdnakit(RPackage):
	"""Fragmen-length analysis package from high-throughput sequencing of cell-free DNA (cfDNA)

	This package provides basic functions for analyzing shallow whole-genome sequencing (~0.3X or more) of cell-free DNA (cfDNA). The package basically extracts the length of cfDNA fragments and aids the vistualization of fragment-length information. The package also extract fragment-length information per non-overlapping fixed-sized bins and used it for calculating ctDNA estimation score (CES).
	"""
	
	bioc = "cfdnakit" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cfdnakit_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cfdnakit/cfdnakit_1.0.0.tar.gz"]

	version("1.0.0", md5="967a84e96d20af4a0256e117afe272b7")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pscbs", type=("build", "run"))
	depends_on("r-qdnaseq", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
