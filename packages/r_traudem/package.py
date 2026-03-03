# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraudem(RPackage):
	"""Use TauDEM

	Simple trustworthy utility functions to use TauDEM 
    (Terrain Analysis Using Digital Elevation Models <https://hydrology.usu.edu/taudem/taudem5/>) command-line interface.
    This package provides a guide to installation of TauDEM and its dependencies GDAL (Geopatial Data Abstraction Library) 
    and MPI (Message Passing Interface) for different operating systems.
    Moreover, it checks that TauDEM and its dependencies are correctly installed and included to the PATH, 
    and it provides wrapper commands for calling TauDEM methods from R.
	"""
	
	homepage = "https://lucarraro.github.io/traudem/"
	cran = "traudem" 

	version("1.0.2", md5="d59393626544a500d5756b2f7ff2b094")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sys", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
