# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsomirs(RPackage):
	"""Analyze isomiRs and miRNAs from small RNA-seq

	Characterization of miRNAs and isomiRs, clustering and differential expression.
	"""
	
	bioc = "isomiRs"

	version("1.36.1", commit="f20b655847fce2e3bebd425874d76f3abb2fa357")
	version("1.30.0", commit="ac97130b032cb64c0a6ff06df1e2a780e7afe34f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-assertive-sets", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-degreport", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
