# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoundandround(RPackage):
	"""Plot Objects Moving in Orbits

	Visualize the objects in orbits in 2D and 3D. The packages is under developing to plot the orbits of objects in polar coordinate system. See the examples in demo.
	"""
	
	cran = "RoundAndRound" 

	version("0.0.1", md5="9f5435241a7a7f16ade668fe760cb9aa")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
