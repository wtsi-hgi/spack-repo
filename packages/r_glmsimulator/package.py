# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmsimulator(RPackage):
	"""Creates Ideal Data for Generalized Linear Models

	Creates ideal data for all distributions in the generalized
    linear model framework.
	"""
	
	cran = "GlmSimulatoR" 

	version("1.0.0", md5="fad2ddac574071055b8058a4caeba46c")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tweedie", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cplm", type=("build", "run"))
