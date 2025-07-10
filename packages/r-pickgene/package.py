# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPickgene(RPackage):
	"""Adaptive Gene Picking for Microarray Expression Data Analysis

	Functions to Analyze Microarray (Gene Expression) Data.
	"""
	
	homepage = "http://www.stat.wisc.edu/~yandell/statgen"
	bioc = "pickgene" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pickgene_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pickgene/pickgene_1.74.0.tar.gz"]

	version("1.74.0", sha256="5da2bf657c69351c8f2b78e8f4da800ccbfb1e4cf6eb686b57beeb648030e836")

	depends_on("r-mass", type=("build", "run"))
