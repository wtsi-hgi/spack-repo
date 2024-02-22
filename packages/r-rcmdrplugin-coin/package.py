# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginCoin(RPackage):
	"""Rcmdr Coin Plug-in

	Rcmdr GUI extension plug-in for coin package (Conditional Inference Procedures in a Permutation Test Framework).
	"""
	
	cran = "RcmdrPlugin.coin" 

	version("1.0-23", md5="1bf92d52bfc918961bb19dece4b03eb1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcmdr@1.7:", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
