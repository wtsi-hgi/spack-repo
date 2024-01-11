# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGosemsim(RPackage):
	"""GO-terms Semantic Similarity Measures.

	The semantic comparisons of Gene Ontology (GO) annotations provide
	quantitative ways to compute similarities between genes and gene groups,
	and have became important basis for many bioinformatics analysis
	approaches. GOSemSim is an R package for semantic similarity computation
	among GO terms, sets of GO terms, gene products and gene clusters.
	GOSemSim implemented five methods proposed by Resnik, Schlicker, Jiang,
	Lin and Wang respectively."""

	bioc = "GOSemSim"

	version("2.28.0", commit="c4646cf8ce5aa51689c02b09a435cec75042fa67")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
