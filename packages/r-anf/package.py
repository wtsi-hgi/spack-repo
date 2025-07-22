# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnf(RPackage):
	"""Affinity Network Fusion for Complex Patient Clustering

	This package is used for complex patient clustering by integrating multi-omic data through affinity network fusion.
	"""
	
	bioc = "ANF" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ANF_1.24.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ANF/ANF_1.24.1.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.1", sha256="331371f7fd1d93638227e59b1446ed129193d33cb3b12ce21f12521a17455479")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
