# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiceview(RPackage):
	"""Methods for Visualization of Computer Experiments Design and
Surrogate

	View 2D/3D sections, contour plots, mesh of excursion sets for computer experiments designs, surrogates or test functions.
	"""
	
	homepage = "https://github.com/IRSN/DiceView"
	cran = "DiceView" 

	version("2.2-0", md5="74f2761379258caf3939a655aefd29b4")

	depends_on("r-dicedesign", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
