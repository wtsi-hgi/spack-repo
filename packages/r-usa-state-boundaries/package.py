# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsaStateBoundaries(RPackage):
	"""WGS84 Datum Map of the USA, Including Puerto Rico and the U.S.
Virgin Islands

	Contains a WGS84 datum map of the USA, which includes all
    Commonwealth and State boundaries & also includes Puerto Rico and the U.S.
    Virgin Islands. This map is a reprojection of the NAD83 datum map from the
    USGS National Map. This package contains a subset of the data included in
    the 'USA.state.boundaries.data' package, which is available in a 'drat'
    repository. To install that data package, please follow the instructions at
    <https://gitlab.com/iembry/usa.state.boundaries.data>.
	"""
	
	homepage = "https://gitlab.com/iembry/usa.state.boundaries"
	cran = "USA.state.boundaries" 

	version("1.0.1", md5="d6bfc14ff7daf8a7bc7d5f878316b049")

	depends_on("r@3.5:", type=("build", "run"))
