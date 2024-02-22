# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplancs(RPackage):
	"""Spatial and Space-Time Point Pattern Analysis.

	The Splancs package was written as an enhancement to S-Plus for display and
	analysis of spatial point pattern data; it has been ported to R and is in
	"maintenance mode"."""

	cran = "splancs"

	version("2.01-44", md5="44e5896425648e699fb0fe15fef191fc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp@0.9:", type=("build", "run"))
