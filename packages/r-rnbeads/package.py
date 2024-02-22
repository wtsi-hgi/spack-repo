# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeads(RPackage):
	"""RnBeads

	RnBeads facilitates comprehensive analysis of various types of DNA methylation data at the genome scale.
	"""
	
	bioc = "RnBeads" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RnBeads_2.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RnBeads/RnBeads_2.20.0.tar.gz"]

	version("2.20.0", md5="40a269bbbddeb407ca5c4545cb6852ff")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-ggplot2@0.9.2:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-methylumi", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
