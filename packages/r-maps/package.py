# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaps(RPackage):
	"""Draw Geographical Maps.

	Display of maps. Projection code and larger maps are in separate packages
	('mapproj' and 'mapdata')."""

	cran = "maps"

	version("3.4.2", md5="78e2f51ccf17274313305b0916edee7b")

	depends_on("r@3.5:", type=("build", "run"))
