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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/pickgene_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/pickgene/pickgene_1.74.0.tar.gz"]

	version("1.74.0", md5="250b3649eff783447f1d2c34f67bf3ca")

	depends_on("r-mass", type=("build", "run"))
