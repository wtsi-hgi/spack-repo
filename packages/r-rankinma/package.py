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

	version("0.2.2", md5="07c5b189d7f2847d2c8cc68738521ff9")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-netmeta", type=("build", "run"))
