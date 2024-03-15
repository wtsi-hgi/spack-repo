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

	version("0.2.1", md5="a1fc3275769d99edf4adc340a9635129")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-netmeta", type=("build", "run"))
