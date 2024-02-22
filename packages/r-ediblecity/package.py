# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdiblecity(RPackage):
	"""Modeling Urban Agriculture at City Scale

	The purpose of this package is to estimate the potential of urban agriculture to contribute to addressing several urban challenges at the city-scale. Within this aim, we selected 8 indicators directly related to one or several urban challenges. Also, a function is provided to compute new scenarios of urban agriculture. Methods are described by Pueyo-Ros, Comas & Corominas (2023) <doi:10.12688/openreseurope.16054.1>.
	"""
	
	homepage = "https://github.com/icra/ediblecity"
	cran = "ediblecity" 

	version("0.2.1", md5="1c0eb4fae31aa74175558af34f804f8a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf@0.9:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-stars@0.5:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
