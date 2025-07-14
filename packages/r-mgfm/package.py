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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MGFM_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MGFM/MGFM_1.36.0.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="59b0aa7e48246bd7ba63595fd99ef7ce2477f0be9b37004e071a10946ae14109")

	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
