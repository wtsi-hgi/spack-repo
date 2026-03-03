# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrimseq(RPackage):
	"""Differential transcript usage and tuQTL analyses with Dirichlet-multinomial model in RNA-seq

	The package provides two frameworks. One for the differential transcript usage analysis between different conditions and one for the tuQTL analysis. Both are based on modeling the counts of genomic features (i.e., transcripts) with the Dirichlet-multinomial distribution. The package also makes available functions for visualization and exploration of the data and results.
	"""
	
	bioc = "DRIMSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DRIMSeq_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DRIMSeq/DRIMSeq_1.30.0.tar.gz"]

	version("1.30.0", md5="fae7a1b0945b2942ef3f633d68a74fd2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
