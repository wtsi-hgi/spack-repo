# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiara(RPackage):
	"""Cluster Independent Algorithm for Rare Cell Types Identification

	Identification of markers of rare cell types by looking at genes whose expression is confined in small regions of the expression space <https://github.com/ScialdoneLab>.
	"""
	
	cran = "CIARA" 

	version("0.1.0", md5="406af5322e7cb2d24ac2016b7fb60ebb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
