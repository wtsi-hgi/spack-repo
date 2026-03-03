# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedgene(RPackage):
	"""Gene-Level Variant Association Tests for Pedigree Data

	Gene-level variant association tests with disease status for pedigree data: kernel and burden association statistics.
	"""
	
	homepage = "https://analytictools.mayo.edu/research/pedgene/"
	cran = "pedgene" 

	version("3.8", md5="5bc22a1c8166b483f7f6af6048ba019a")
	version("3.6", md5="f534b8cc6ecb450be49fcda742a4cab0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
