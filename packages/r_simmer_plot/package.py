# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimmerPlot(RPackage):
	"""Plotting Methods for 'simmer'

	A set of plotting methods for 'simmer' trajectories and simulations.
	"""
	
	homepage = "https://r-simmer.org"
	cran = "simmer.plot" 

	version("0.1.18", md5="bdbab11d5f1b9997367479b28cf9c7d9")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-simmer@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tidyr@0.7:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
