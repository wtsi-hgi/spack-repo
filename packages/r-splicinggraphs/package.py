# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplicinggraphs(RPackage):
	"""Create, manipulate, visualize splicing graphs, and assign RNA-seq reads to them

	This package allows the user to create, manipulate, and visualize splicing graphs and their bubbles based on a gene model for a given organism. Additionally it allows the user to assign RNA-seq reads to the edges of a set of splicing graphs, and to summarize them in different ways.
	"""
	
	homepage = "https://bioconductor.org/packages/SplicingGraphs"
	bioc = "SplicingGraphs" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SplicingGraphs_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SplicingGraphs/SplicingGraphs_1.42.0.tar.gz"]

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="645c7406148182200352240d554df82b1fdf24a4a69a092a26b8357589695ed9")

	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.17.5:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-iranges@2.21.2:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges@1.23.21:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
