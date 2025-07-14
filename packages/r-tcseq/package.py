# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcseq(RPackage):
	"""Time course sequencing data analysis

	Quantitative and differential analysis of epigenomic and transcriptomic time course sequencing data, clustering analysis and visualization of the temporal patterns of time course data.
	"""
	
	bioc = "TCseq"

	version("1.32.0", commit="7813ead0cc56b31554f884e79a6272c848614035")
	version("1.26.0", commit="9f773246518c4bd9272864864912bf16c5d445ac")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
