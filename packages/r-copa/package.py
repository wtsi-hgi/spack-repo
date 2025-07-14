# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopa(RPackage):
	"""Functions to perform cancer outlier profile analysis.

	COPA is a method to find genes that undergo recurrent fusion in a given cancer type by finding pairs of genes that have mutually exclusive outlier profiles.
	"""
	
	bioc = "copa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/copa_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/copa/copa_1.70.0.tar.gz"]

	version("1.76.0", tag="RELEASE_3_21")
	version("1.70.0", sha256="4ef205cdb2bf4125dc689664b4ea84acc102b326dfe13b6201a58622741c0614")

	depends_on("r-biobase", type=("build", "run"))
