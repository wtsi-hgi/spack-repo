# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnthropmmd(RPackage):
	"""An R Package for the Mean Measure of Divergence (MMD)

	Offers a graphical user interface for the calculation of the mean measure of divergence, with facilities for trait selection and graphical representations <doi:10.1002/ajpa.23336>.
	"""
	
	homepage = "https://gitlab.com/f-santos/anthropmmd/"
	cran = "AnthropMMD" 

	version("4.0.3", md5="a1a557c308b5fcec94278e61b4fd6009")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
