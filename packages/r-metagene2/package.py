# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagene2(RPackage):
	"""A package to produce metagene plots

	This package produces metagene plots to compare coverages of sequencing experiments at selected groups of genomic regions. It can be used for such analyses as assessing the binding of DNA-interacting proteins at promoter regions or surveying antisense transcription over the length of a gene. The metagene2 package can manage all aspects of the analysis, from normalization of coverages to plot facetting according to experimental metadata. Bootstraping analysis is used to provide confidence intervals of per-sample mean coverages.
	"""
	
	homepage = "https://github.com/ArnaudDroitLab/metagene2"
	bioc = "metagene2" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metagene2_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metagene2/metagene2_1.18.0.tar.gz"]

	version("1.18.0", md5="adef0ffd2a7cec30870a2b66eb2cb4f9", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/metagene2_1.18.0.tar.gz")
	version("1.18.0", md5="adef0ffd2a7cec30870a2b66eb2cb4f9", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metagene2_1.18.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
