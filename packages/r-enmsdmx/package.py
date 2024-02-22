# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnmsdmx(RPackage):
	"""Species Distribution Modeling and Ecological Niche Modeling

	Implements species distribution modeling and ecological niche
	modeling, including: bias correction, spatial cross-validation, model
	evaluation, raster interpolation, biotic "velocity" (speed and
	direction of movement of a "mass" represented by a raster), interpolating
	across a time series of rasters, and use of spatially imprecise records.
	The heart of the package is a set of "training" functions which
	automatically optimize model complexity based number of available
	occurrences. These algorithms include MaxEnt, MaxNet, boosted regression
	trees/gradient boosting machines, generalized additive models,
	generalized linear models, natural splines, and random forests. To enhance
	interoperability with other modeling packages, no new classes are created.
	The package works with 'PROJ6' geodetic objects and coordinate reference
	systems.
	"""
	
	homepage = "https://github.com/adamlilith/enmSdmX"
	cran = "enmSdmX" 

	version("1.1.2", md5="1c4a8066918ca517a200ae9435f58ff5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dismo", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-maxnet", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-omnibus", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-statisfactory", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
