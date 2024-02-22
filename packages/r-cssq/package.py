# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCssq(RPackage):
	"""Chip-seq Signal Quantifier Pipeline

	This package is desgined to perform statistical analysis to identify statistically significant differentially bound regions between multiple groups of ChIP-seq dataset.
	"""
	
	bioc = "CSSQ" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CSSQ_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CSSQ/CSSQ_1.14.0.tar.gz"]

	version("1.14.0", md5="d9a6f6200f67cc06173c30dcd6775e5a")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
