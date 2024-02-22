# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBirdring(RPackage):
	"""Methods to Analyse Ring Re-Encounter Data

	R functions to read EURING data and analyse re-encounter data of birds marked by metal rings. For a tutorial, go to <doi:10.1080/03078698.2014.933053>.
	"""
	
	cran = "birdring" 

	version("1.6", md5="c7bf5473c389c3d0ff2452031d97f5f7")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-lazydata", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
