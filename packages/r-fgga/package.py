# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgga(RPackage):
	"""Hierarchical ensemble method based on factor graph

	Package that implements the FGGA algorithm. This package provides a hierarchical ensemble method based ob factor graphs for the consistent cross-ontology annotation of protein coding genes. FGGA embodies elements of predicate logic, communication theory, supervised learning and inference in graphical models.
	"""
	
	homepage = "https://github.com/fspetale/fgga"
	bioc = "fgga" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/fgga_1.10.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/fgga/fgga_1.10.2.tar.gz"]

	version("1.10.2", md5="593ff20d3098840f42f7a5c657da4c9c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
