# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocgraph(RPackage):
	"""Graph examples and use cases in Bioinformatics

	This package provides examples and code that make use of the different graph related packages produced by Bioconductor.
	"""
	
	bioc = "biocGraph" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biocGraph_1.64.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biocGraph/biocGraph_1.64.0.tar.gz"]

    version("1.70.0", tag="RELEASE_3_21")
	version("1.64.0", sha256="b4e686f6cadec0ac555f86a2cc5fde8da1d749cb3caeba65186515e5365fc0fb")

	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
