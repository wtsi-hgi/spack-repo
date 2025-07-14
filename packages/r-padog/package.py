# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPadog(RPackage):
	"""Pathway Analysis with Down-weighting of Overlapping Genes (PADOG)

	This package implements a general purpose gene set analysis method called PADOG that downplays the importance of genes that apear often accross the sets of genes to be analyzed. The package provides also a benchmark for gene set analysis methods in terms of sensitivity and ranking using 24 public datasets from KEGGdzPathwaysGEO package.
	"""
	
	bioc = "PADOG"

	version("1.50.0", commit="4f7fb8c75739c7abacaf8276824d9c46e0e1d6d7")
	version("1.44.0", commit="da280c71f1370b8f3913d100a0d2fbcce47444e8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-keggdzpathwaysgeo", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-gsa", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-hgu133plus2-db", type=("build", "run"))
	depends_on("r-hgu133a-db", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
