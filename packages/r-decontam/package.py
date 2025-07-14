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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/decontam_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/decontam/decontam_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="736b270861e029e47b7b9958fe38bda6c6b833ebe8e98b54e2e766ddb1699f54")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
