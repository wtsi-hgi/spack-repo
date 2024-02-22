# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgraphviz(RPackage):
	"""Provides plotting capabilities for R graph objects.

	Interfaces R with the AT and T graphviz library for plotting R graph
	objects from the graph package."""

	bioc = "Rgraphviz"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Rgraphviz_2.46.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Rgraphviz/Rgraphviz_2.46.0.tar.gz"]

	version("2.46.0", md5="b93e5d1c383b1e5cd06e4dec89a43ce8")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("graphviz", type=("build", "link", "run"))
