# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlstac(RPackage):
	"""An R Package for Fitting Separable Nonlinear Models

	Set of functions implementing the algorithm described in Fernandez 
    Torvisco et al. (2018) for fitting separable nonlinear regression curves. 
    See Fernandez Torvisco, Rodriguez-Arias Fernandez and Cabello Sanchez (2018)
    <doi:10.2298/FIL1812233T>. 
	"""
	
	cran = "nlstac" 

	version("0.2.0", md5="b67fa4efe2d76ffc937b56f5f62bcad1")

	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
