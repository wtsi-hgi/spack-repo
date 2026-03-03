# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMovehmm(RPackage):
	"""Animal Movement Modelling using Hidden Markov Models

	Provides tools for animal movement modelling using hidden Markov
    models. These include processing of tracking data, fitting hidden Markov models
    to movement data, visualization of data and fitted model, decoding of the state
    process, etc. <doi:10.1111/2041-210X.12578>.
	"""
	
	homepage = "https://github.com/TheoMichelot/moveHMM"
	cran = "moveHMM" 

	version("1.9", md5="9dc4aeeb90f424a09310a5856815c723")

	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
