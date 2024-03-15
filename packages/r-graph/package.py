# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraph(RPackage):
	"""A package to handle graph data structures.

	A package that implements some simple graph handling capabilities."""

	bioc = "graph"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/graph_1.80.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/graph/graph_1.80.0.tar.gz"]

	version("1.80.0", md5="735b96df0f7c955806148170220b75b2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.11:", type=("build", "run"))
