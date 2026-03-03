# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdmpredictors(RPackage):
	"""Species Distribution Modelling Predictor Datasets

	Terrestrial and marine predictors for species distribution modelling
    from multiple sources, including WorldClim <https://www.worldclim.org/>,,
    ENVIREM <https://envirem.github.io/>, Bio-ORACLE <https://bio-oracle.org/>
    and MARSPEC <http://www.marspec.org/>.
	"""
	
	homepage = "http://lifewatch.github.io/sdmpredictors/"
	cran = "sdmpredictors" 

	version("0.2.15", md5="a0a1f002895644e104b3d6db913bc951")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-r-utils@2.4:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
