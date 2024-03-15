# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeojsonsf(RPackage):
	"""GeoJSON to Simple Feature Converter.

	Converts Between GeoJSON and simple feature objects."""

	cran = "geojsonsf"

	license("MIT")

	version("2.0.3", md5="124952e42b4eaba8b046506623ac0242")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-geometries", type=("build", "run"))
	depends_on("r-jsonify@1.1.1:", type=("build", "run"))
	depends_on("r-rapidjsonr@1.2:", type=("build", "run"))
	depends_on("r-sfheaders@0.2.2:", type=("build", "run"))
