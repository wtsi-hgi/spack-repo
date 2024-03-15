# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypergraph(RPackage):
	"""A package providing hypergraph data structures.

	A package that implements some simple capabilities for representing and
	manipulating hypergraphs."""

	bioc = "hypergraph"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hypergraph_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hypergraph/hypergraph_1.74.0.tar.gz"]

	version("1.74.0", md5="e97653a8503ba0bcb6da1dbdf1a3552b")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
