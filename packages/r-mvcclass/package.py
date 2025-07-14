# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvcclass(RPackage):
	"""Model-View-Controller (MVC) Classes

	Creates classes used in model-view-controller (MVC) design
	"""
	
	bioc = "MVCClass"

	version("1.82.0", commit="eb7e11b7dea4c8b2fe9a64432471fbfc80dddb8e")
	version("1.76.0", commit="35611dec85669863dd8ad92c86278f4871e02b9f")

	depends_on("r@2.1:", type=("build", "run"))
