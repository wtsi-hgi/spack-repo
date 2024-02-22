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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TCseq_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TCseq/TCseq_1.26.0.tar.gz"]

	version("1.26.0", md5="f5b63a6d1b40c82f8ddc86cc2abdb89b")

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
