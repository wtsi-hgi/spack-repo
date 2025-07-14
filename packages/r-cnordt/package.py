# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnordt(RPackage):
	"""Add-on to CellNOptR: Discretized time treatments

	This add-on to the package CellNOptR handles time-course data, as opposed to steady state data in CellNOptR. It scales the simulation step to allow comparison and model fitting for time-course data. Future versions will optimize delays and strengths for each edge.
	"""
	
	bioc = "CNORdt"

	version("1.50.0", commit="47e128708297b92a022005fd2fe6c3065a161420")
	version("1.44.0", commit="3806f4e37488ed6823be33cd850c006e1df1f91d")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-cellnoptr@0.99:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
