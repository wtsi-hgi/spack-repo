# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankinma(RPackage):
	"""Rank in Network Meta-Analysis

	A supportive collection of functions for gathering and plotting treatment ranking metrics after network meta-analysis.
	"""
	
	homepage = "https://rankinma.shinyapps.io/rankinma/"
	cran = "rankinma" 

	version("0.2.0", md5="e9a16a6beb648a64235ed829de7b15a4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-netmeta", type=("build", "run"))
