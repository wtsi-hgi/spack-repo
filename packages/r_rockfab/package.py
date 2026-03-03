# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRockfab(RPackage):
	"""Rock Fabric and Strain Analysis Tools

	Provides functions to complete three-dimensional rock fabric and strain analyses following the Rf Phi, Fry, and normalized Fry methods. Also allows for plotting of results and interactive 3D visualization functionality.
	"""
	
	cran = "RockFab" 

	version("1.2.1", md5="24740c76852e58feaca736d17f9a037d")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
