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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GOSemSim_2.28.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GOSemSim/GOSemSim_2.28.1.tar.gz"]

	version("2.28.1", md5="89d833af368b8fb6592d7acd623e0a45")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
