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

	version("1.24.0", commit="1f6ea5455a30d0c69cb80bf5d83e419de36c3e03")
	version("1.18.0", commit="32c93af8af8a899e5f8fd76f3b7799f5aa88a5cf")

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
