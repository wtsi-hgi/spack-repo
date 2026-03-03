# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpgraph(RPackage):
	"""Estimation of genetic and molecular regulatory networks from high-throughput genomics data

	Estimate gene and eQTL networks from high-throughput expression and genotyping assays.
	"""
	
	homepage = "https://github.com/rcastelo/qpgraph"
	bioc = "qpgraph" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/qpgraph_2.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/qpgraph/qpgraph_2.36.0.tar.gz"]

	version("2.36.0", md5="10be7ba90f9349fb4de4aa84e6fecaa4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-graph@1.45.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
