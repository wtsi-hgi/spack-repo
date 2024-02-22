# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNucombog(RPackage):
	"""NUtrient Cycling and COMpetition Model Undisturbed Open Bog
Ecosystems in a Temperate to Sub-Boreal Climate

	Modelling the vegetation, carbon, nitrogen and water dynamics of undisturbed open bog ecosystems in a temperate to sub-boreal climate. The executable of the model can downloaded from <https://github.com/jeroenpullens/NUCOMBog>.
	"""
	
	homepage = "https://github.com/jeroenpullens/NUCOMBog/"
	cran = "NUCOMBog" 

	version("1.0.4.2", md5="4cef856a88073302edba7163fe05b380")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
