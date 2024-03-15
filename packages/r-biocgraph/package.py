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

	version("1.64.0", md5="5deb3ff8596eaf678592ad9ae15defe2")

	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
