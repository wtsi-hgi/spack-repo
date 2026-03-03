# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaiccalc(RPackage):
	"""R-Language Based Calculus Operations for Teaching

	Software to support the introductory *MOSAIC Calculus* 
    textbook <https://www.mosaic-web.org/MOSAIC-Calculus/>),
    one of many data- and modeling-oriented educational resources developed by 
    Project MOSAIC (<https://www.mosaic-web.org/>). Provides symbolic and
    numerical differentiation and integration, as well as support for 
    applied linear algebra (for data science), and differential equations/dynamics.
    Includes grammar-of-graphics-based functions for drawing vector fields, trajectories, etc.
    The software is suitable for general use, but intended mainly for teaching calculus.
	"""
	
	homepage = "https://github.com/ProjectMOSAIC/mosaicCalc"
	cran = "mosaicCalc" 

	version("0.6.1", md5="7bec3d89cad3030211dd76beb3e982e3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mosaic", type=("build", "run"))
	depends_on("r-mosaiccore@0.9.2:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggformula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-metr@0.11:", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
