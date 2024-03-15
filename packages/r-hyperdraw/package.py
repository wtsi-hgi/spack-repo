# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyperdraw(RPackage):
	"""Visualizing Hypergaphs

	Functions for visualizing hypergraphs.
	"""
	
	bioc = "hyperdraw" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hyperdraw_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hyperdraw/hyperdraw_1.54.0.tar.gz"]

	version("1.54.0", md5="2b1ec2cf9ea920a241f821baa08bb393")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-hypergraph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("graphviz", type=("build", "link", "run"))
