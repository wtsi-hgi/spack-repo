# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScifer(RPackage):
	"""Scifer: Single-Cell Immunoglobulin Filtering of Sanger Sequences

	Have you ever index sorted cells in a 96 or 384-well plate and then sequenced using Sanger sequencing? If so, you probably had some struggles to either check the electropherogram of each cell sequenced manually, or when you tried to identify which cell was sorted where after sequencing the plate. Scifer was developed to solve this issue by performing basic quality control of Sanger sequences and merging flow cytometry data from probed single-cell sorted B cells with sequencing data. scifer can export summary tables, 'fasta' files, electropherograms for visual inspection, and generate reports.
	"""
	
	homepage = "https://github.com/rodrigarc/scifer"
	bioc = "scifer"

	version("1.10.0", commit="ecb014a1f9af4eb3b01abaeeff9c9c1a5685c231")
	version("1.4.0", commit="8f38aee692cc4fd9826d3944205843601e15bc8d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-decipher", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sangerseqr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
