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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mitoClone2_1.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mitoClone2/mitoClone2_1.8.1.tar.gz"]

	version("1.8.1", md5="22c58ba6ed0a51f10714551935477355", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mitoClone2_1.8.1.tar.gz")

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
