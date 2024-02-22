# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSf(RPackage):
	"""Simple Features for R.

	Support for simple features, a standardized way to encode spatial vector
	data. Binds to 'GDAL' for reading and writing data, to 'GEOS' for
	geometrical operations, and to 'PROJ' for projection conversions and datum
	transformations. Optionally uses the 's2' package for spherical geometry
	operations on geographic coordinates."""

	cran = "sf"

	version("1.0-15", md5="b3c5d978da86e8da20f577b65c4eaaff")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-classint@0.4.1:", type=("build", "run"))
	depends_on("r-dbi@0.8:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s2@1.1:", type=("build", "run"))
	depends_on("r-units@0.7.0:", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))
