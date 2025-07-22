# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrainflowprobes(RPackage):
	"""Plots and annotation for choosing BrainFlow target probe sequence

	Use these functions to characterize genomic regions for BrainFlow target probe design.
	"""
	
	homepage = "https://github.com/LieberInstitute/brainflowprobes"
	bioc = "brainflowprobes"

	version("1.16.0", commit="d92e0fe01813a7e78066cf18117e960562354b7d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biostrings@2.52:", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19@1.4:", type=("build", "run"))
	depends_on("r-bumphunter@1.26:", type=("build", "run"))
	depends_on("r-cowplot@1:", type=("build", "run"))
	depends_on("r-derfinder@1.18.1:", type=("build", "run"))
	depends_on("r-derfinderplot@1.18.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.36:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1:", type=("build", "run"))
	depends_on("r-genomicstate@0.99.7:", type=("build", "run"))
