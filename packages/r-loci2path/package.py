# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoci2path(RPackage):
	"""Loci2path: regulatory annotation of genomic intervals based on tissue-specific expression QTLs

	loci2path performs statistics-rigorous enrichment analysis of eQTLs in genomic regions of interest. Using eQTL collections provided by the Genotype-Tissue Expression (GTEx) project and pathway collections from MSigDB.
	"""
	
	homepage = "https://github.com/StanleyXu/loci2path"
	bioc = "loci2path"

	version("1.28.0", commit="4b4e47b04eeff6328e616480a5b257f253195d07")
	version("1.22.0", commit="903e07c3aca93d39988e9faf0b78f395607f593d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
