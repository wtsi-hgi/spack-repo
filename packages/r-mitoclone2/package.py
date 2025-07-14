# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMitoclone2(RPackage):
	"""Clonal Population Identification in Single-Cell RNA-Seq Data using Mitochondrial and Somatic Mutations

	This package primarily identifies variants in mitochondrial genomes from BAM alignment files. It filters these variants to remove RNA editing events then estimates their evolutionary relationship (i.e. their phylogenetic tree) and groups single cells into clones. It also visualizes the mutations and providing additional genomic context.
	"""
	
	homepage = "https://github.com/benstory/mitoClone2"
	bioc = "mitoClone2"

	version("1.14.0", commit="9f9dee682be0aaaf22e2e5ed47cc1936a3d898fa")
	version("1.8.1", commit="e22b9da48dcaeeeb2d55a3631ca32521c8d705bc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-deepsnv", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rhtslib@1.13.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("phiscs", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
