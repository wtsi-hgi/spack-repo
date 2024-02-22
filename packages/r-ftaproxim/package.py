# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFtaproxim(RPackage):
	"""Fault Tree Analysis Based on Proxel Simulation

	Calculation and plotting of instantaneous unavailabilities of basic events along with the top event of fault trees are issues important in reliability analysis of complex systems. Here, a fault tree is provided in terms of its minimal cut sets, along with reliability and maintainability distribution functions of the basic events. All the methods are derived from Horton (2002, ISBN: 3-936150-21-4), Niloofar and Lazarova-Molnar (2022).
	"""
	
	cran = "ftaproxim" 

	version("0.0.1", md5="73ef56e25e739264d52da9e54a45e6cb")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
