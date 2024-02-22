# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginFactominer(RPackage):
	"""Graphical User Interface for FactoMineR

	Rcmdr Plugin for the 'FactoMineR' package.
	"""
	
	homepage = "http://factominer.free.fr/graphs/RcmdrPlugin.html"
	cran = "RcmdrPlugin.FactoMineR" 

	version("1.8", md5="6c8091f230ed3534622638b23a87c9fb")

	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-rcmdr@2.0.0:", type=("build", "run"))
