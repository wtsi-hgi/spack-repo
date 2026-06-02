# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimniche(RPackage):
	"""Niche Climate Exposure

	Assesses niche climate exposure by interpreting projected climate
	change relative to the climate conditions a species currently occupies.
	Using occurrence records, range data or thresholded SDM suitability maps,
	current environmental rasters and future projections, the package separates
	climate change amount, change in distance to the current niche centre,
	composition change and exceedance beyond an empirical niche boundary.
	"""

	homepage = "https://github.com/Bohao0813/climniche/"
	cran = "climniche"

	version("0.0.1", md5="d6cc7e67cb333380725679432d70a7e6")

	depends_on("r", type=("build", "run"))
