# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicinteractions(RPackage):
	"""Utilities for handling genomic interaction data

	Utilities for handling genomic interaction data such as ChIA-PET or Hi-C, annotating genomic features with interaction information, and producing plots and summary statistics.
	"""
	
	homepage = "https://github.com/ComputationalRegulatoryGenomicsICL/GenomicInteractions/"
	bioc = "GenomicInteractions"

	version("1.42.0", commit="76a090b6f6dc5b064da3e2face684fb41d06e2cb")
	version("1.36.0", commit="879441ec76a6b4de794826ef706500130c646570")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges@1.29.6:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics@0.15.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-s4vectors@0.13.13:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
