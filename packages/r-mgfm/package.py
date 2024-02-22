# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgfm(RPackage):
	"""Marker Gene Finder in Microarray gene expression data

	The package is designed to detect marker genes from Microarray gene expression data sets
	"""
	
	bioc = "MGFM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MGFM_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MGFM/MGFM_1.36.0.tar.gz"]

	version("1.36.0", md5="893a9f574fe4e023d3c4d3b99d58ae78")

	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
