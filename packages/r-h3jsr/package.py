# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH3jsr(RPackage):
	"""Access Uber's H3 Library

	Provides access to Uber's H3 library for geospatial indexing via its JavaScript transpile 'h3-js' <https://github.com/uber/h3-js> and 'V8' <https://github.com/jeroen/v8>.
	"""
	
	homepage = "https://obrl-soil.github.io/h3jsr/"
	cran = "h3jsr" 

	version("1.3.1", md5="ea978ecab1ab2a63934f5461519eae86")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-v8@4:", type=("build", "run"))
