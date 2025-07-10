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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fgga_1.10.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fgga/fgga_1.10.2.tar.gz"]

	version("1.10.2", sha256="d7356dea18ec53ffac06f2e2231a814ec054f786b21cb1a4ab2410a1d71b6db1")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
