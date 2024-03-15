# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnaquin(RPackage):
	"""Statistical analysis of sequins.

	The project is intended to support the use of sequins (synthetic
	sequencing spike-in controls) owned and made available by the Garvan
	Institute of Medical Research. The goal is to provide a standard open
	source library for quantitative analysis, modelling and visualization of
	spike-in controls."""

	bioc = "Anaquin"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Anaquin_2.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Anaquin/Anaquin_2.26.0.tar.gz"]

	version("2.26.0", md5="a0b480fdac1e56d9b308c2c23518b4a0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
