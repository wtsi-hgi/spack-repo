# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmviz(RPackage):
	"""A Package to Visualize Linear Models Features and Play with Them

	Contains a suite of shiny applications
    meant to explore linear model inference feature through simulation
    and games.
	"""
	
	cran = "lmviz" 

	version("0.2.0", md5="84a516b606aee49e853b78ea082f0b93")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
