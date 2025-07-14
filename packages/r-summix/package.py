# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummix(RPackage):
	"""Summix: A method to estimate and adjust for population structure in genetic summary data

	This package contains the Summix method for estimating and adjusting for ancestry in genetic summary allele frequency data. The function summix estimates reference ancestry proportions using a mixture model. The adjAF function produces ancestry adjusted allele frequencies for an observed sample with ancestry proportions matching a target person or sample.
	"""
	
	bioc = "Summix" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Summix_2.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Summix/Summix_2.8.0.tar.gz"]

	version("2.14.0", tag="RELEASE_3_21")
	version("2.8.0", sha256="776e29e4eaf7fa3d24180bb656f9543a6fabd83095adfa109279425af8827125")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
