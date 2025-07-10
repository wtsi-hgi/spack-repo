# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimona(RPackage):
	"""Semantic Similarity in Bio-Ontologies

	This package implements infrastructures for ontology analysis by offering efficient data structures, fast ontology traversal methods, and elegant visualizations. It provides a robust toolbox supporting over 70 methods for semantic similarity analysis.
	"""
	
	homepage = "https://github.com/jokergoo/simona"
	bioc = "simona" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/simona_1.0.10.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/simona/simona_1.0.10.tar.gz"]

	version("1.0.10", sha256="bd149c1909877b03d79442f1f363ae3c05487605a7344d95b7976a9093f47eab")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
	depends_on("r-globaloptions", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-xml2@1.3.3:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
	depends_on("java", type=("build", "link", "run"))
