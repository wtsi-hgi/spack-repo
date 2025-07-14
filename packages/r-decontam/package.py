# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecontam(RPackage):
	"""Identify Contaminants in Marker-gene and Metagenomics Sequencing Data

	Simple statistical identification of contaminating sequence features in marker-gene or metagenomics data. Works on any kind of feature derived from environmental sequencing data (e.g. ASVs, OTUs, taxonomic groups, MAGs,...). Requires DNA quantitation data or sequenced negative control samples.
	"""
	
	homepage = "https://github.com/benjjneb/decontam"
	bioc = "decontam"

	version("1.28.0", commit="24a4a1904b0cb81a073a31c788520b3daaa924e0")
	version("1.22.0", commit="239188dfb6b9ea30996caf876d3095c3b5d55529")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
