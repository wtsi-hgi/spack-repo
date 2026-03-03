# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoundecology(RPackage):
	"""Soundscape Ecology

	Functions to calculate indices for soundscape ecology and other ecology research that uses audio recordings.
	"""
	
	homepage = "http://ljvillanueva.github.io/soundecology/"
	cran = "soundecology" 

	version("1.3.3", md5="8cd1ed26aefbb86cd07b4c15410c285c")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-oce", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
